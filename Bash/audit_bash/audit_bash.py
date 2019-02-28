#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : GaoJiasheng
# 2016-07-08 08:52:07

# !/usr/bin/python
import os
import re
import time
import pyte
import sys
import select
import operator
import fcntl
import tty
import termios
import struct
import signal
import datetime
import socket
import subprocess
import argparse
import threading
import requests
import json

BUFSIZ = 10240
TIMEOUT = 2
ADMINS = ["gaojiasheng", "kangjingsong"]

parser = argparse.ArgumentParser(description='Input Param for Sven-Client:')
parser.add_argument('--log-path', type=str, default='/home/sven-log',
                    help='The path of log file')
parser.add_argument('--report-key', type=str, default='~',
                    help='The secure key to report message')
parser.add_argument('--report-address', type=str, default='http://10.97.214.16:5014',
                    help='The address to report (with http://)')
parser.add_argument('--audit-model', type=str, default='normal',
                    help='The model of audit : [normal | strict | no-audit]')
parser.add_argument('--ca-path', type=str, default='./ca.pem',
                    help='the address ca certificate')

URL_SESSION_START = "/api/v1/session/start/report"
URL_SESSION_END = "/api/v1/session/end/report"
URL_COMMAND = "/api/v1/command/report"

args = parser.parse_args()
LOG_DIR = args.log_path
REPORT_KEY = args.report_key
REPORT_ADDR = args.report_address
AUDIT_MODEL = args.audit_model
CA_PATH = args.ca_path

if "https" not in REPORT_ADDR:
    CA_PATH = False

if AUDIT_MODEL not in ['normal', 'strict', 'no-audit']:
    print "Your Audit Model is Wrong, Please Reset It ! [normal/strict/no-audit]"
    sys.exit(1)


def mkdir(dir_name, username='', mode=755):
    """
    insure the dir exist and mode ok
    """
    cmd = '[ ! -d %s ] && mkdir -p %s && chmod %s %s' % (dir_name, dir_name, mode, dir_name)
    bash(cmd)
    if username:
        chown(dir_name, username)


def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return subprocess.call(cmd, shell=True)


class Pty(object):
    """打开虚拟终端，并与之交互
    主类
    """

    def __init__(self):
        self.pty_pid = ""
        self.pty_fd = ""
        self.session_id = 0
        self.username = os.getlogin()
        self.cs_name = socket.gethostname()
        self.role = self.username
        self.hostname = self.cs_name
        self.winsize = self.get_current_win_size()
        self.log_fd = ""
        self.log_file = ""
        self.vim_flag = False
        self.vim_data = ""
        self.err_log_f = ""
        self.vim_end_pattern = re.compile(r'\x1b\[\?1049', re.X)
        self.ps1_pattern = re.compile("[@a-zA-Z0-9-_\.*]+\@[a-zA-Z0-9-_\.]+")
        self.__init_screen_stream()

        try:
            self.pty_pid, self.pty_fd = os.forkpty()

            if self.pty_pid != 0:
                ts = threading.Thread(target=self.wait_child, args=())
                ts.setDaemon(True)
                ts.start()
        except OSError, e:
            print "Open Bash Error! (contact %s)" % (",".join(ADMINS),)
            os.Exit(1)

    def wait_child(self):
        os.waitpid(self.pty_pid, 0)

    def get_current_win_size(self):
        """
        This function use to get the size of the windows!
        """
        if 'TIOCGWINSZ' in dir(termios):
            TIOCGWINSZ = termios.TIOCGWINSZ
        else:
            TIOCGWINSZ = 1074295912L

        s = struct.pack('HHHH', 0, 0, 0, 0)
        size = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
        return size

    def pty_is_alived(self):
        try:
            os.kill(self.pty_pid, 0)
        except OSError:
            return False
        else:
            return True

    def set_window_size(self, sig="", data=""):
        size = self.get_current_win_size()
        fcntl.ioctl(self.pty_fd, termios.TIOCSWINSZ, size)

    def report_session_start(self):
        if AUDIT_MODEL == "no-audit":
            return
        try:
            param = {}
            param["user"] = self.username
            param["cs"] = self.cs_name
            param["log"] = self.log_file
            param["pid"] = self.pty_pid
            tms = datetime.datetime.now()
            time_now = tms.strftime('%Y-%m-%d %H:%M:%S')
            param["time"] = time_now
            param["report_key"] = REPORT_KEY
            r = requests.post("%s%s" % (REPORT_ADDR, URL_SESSION_START), data=param, timeout=TIMEOUT, verify=CA_PATH)
            if r.status_code == 200:
                self.session_id = int(r.text)
            else:
                if AUDIT_MODEL == 'strict':
                    print "\n[STRICT AUDIT]Session Start report Failed! [HTTP ERROR][code:%s][body:%s]" % (
                    r.status_code, r.text)
                    os.kill(os.getpid(), signal.SIGINT)
                else:
                    pass
        except Exception, e:
            if AUDIT_MODEL == 'strict':
                print "\n[STRICT AUDIT]report session start failed ![%s]" % (e,)
                os.kill(os.getpid(), signal.SIGKILL)
            else:
                pass

    def report_session_end(self):
        if AUDIT_MODEL == "no-audit":
            return
        try:
            param = {}
            param["session_id"] = self.session_id
            param["report_key"] = REPORT_KEY
            tms = datetime.datetime.now()
            time_now = tms.strftime('%Y-%m-%d %H:%M:%S')
            param["time"] = time_now
            r = requests.post("%s%s" % (REPORT_ADDR, URL_SESSION_END), data=param, timeout=TIMEOUT, verify=CA_PATH)
            if r.status_code == 200:
                return
            else:
                if AUDIT_MODEL == 'strict':
                    print "\n[STRICT AUDIT]Session End report Failed! [HTTP ERROR][code:%s][body:%s]" % (
                    r.status_code, r.text)
                else:
                    pass

        except Exception, e:
            if AUDIT_MODEL == 'strict':
                print "\n[STRICT AUDIT] report session end failed ![%s]" % (e,)
            else:
                pass

    def report_command(self, command):
        if AUDIT_MODEL == "no-audit" or command == "":
            return
        try:
            param = {}
            param["session_id"] = self.session_id
            param["user"] = self.username
            param["role"] = self.role
            param["hostname"] = self.hostname
            param["command"] = command
            param["report_key"] = REPORT_KEY
            tms = datetime.datetime.now()
            time_now = tms.strftime('%Y-%m-%d %H:%M:%S')
            param["time"] = time_now
            r = requests.post("%s%s" % (REPORT_ADDR, URL_COMMAND), param, timeout=TIMEOUT, verify=CA_PATH)
            if r.status_code == 200:
                pass
            else:
                if AUDIT_MODEL == 'strict':
                    print "\n[STRICT AUDIT]Command Report Failed! [HTTP ERROR][code:%s][body:%s]" % (
                    r.status_code, r.text)
                    os.kill(os.getpid(), signal.SIGINT)
                else:
                    pass

        except Exception, e:
            if AUDIT_MODEL == 'strict':
                print "\n[STRICT AUDIT] report command failed ![%s]" % (e,)
                os.kill(os.getpid(), signal.SIGINT)
            else:
                pass

    def start(self):
        stdin_origin_attr = termios.tcgetattr(sys.stdin.fileno())

        data = ""
        input_mode = False

        pre_timestamp = time.time()
        log_file_f, log_time_f = pty.get_log()
        # signal.signal(signal.SIGCHLD, signal.SIG_IGN)

        try:
            if self.pty_pid == 0:
                os.execlp("/bin/bash", "-i")
                os.kill(os.getpid(), signal.SIGINT)
            else:
                self.set_window_size()
                signal.signal(signal.SIGWINCH, self.set_window_size)

                stdin_fd = sys.stdin.fileno()
                stdout_fd = sys.stdout.fileno()

                stdout_attr = termios.tcgetattr(stdout_fd)
                termios.tcsetattr(self.pty_fd, termios.TCSADRAIN, stdout_attr)

                flag = fcntl.fcntl(sys.stdin, fcntl.F_GETFL, 0)
                fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)

                tty.setraw(stdin_fd)
                tty.setcbreak(stdin_fd)

                ts = threading.Thread(target=self.report_session_start, args=())
                ts.setDaemon(True)
                ts.start()

                epoll = select.epoll()
                epoll.register(stdin_fd, select.POLLIN)
                epoll.register(self.pty_fd, select.POLLIN | select.POLLOUT)

                while self.pty_is_alived():
                    events = epoll.poll(6)

                    if not events:
                        continue

                    rs = []
                    ws = []

                    for fd, event in events:
                        if event & select.EPOLLIN:
                            rs.append(fd)

                        if event & select.EPOLLOUT:
                            ws.append(fd)

                    if self.pty_fd in rs:
                        try:
                            output = os.read(self.pty_fd, BUFSIZ)
                            os.write(stdout_fd, output)

                            now_timestamp = time.time()

                            log_time_f.write('%s %s\n' % (round(now_timestamp - pre_timestamp, 4), len(output)))
                            log_time_f.flush()
                            log_file_f.write(output)
                            log_file_f.flush()
                            pre_timestamp = now_timestamp
                            log_file_f.flush()

                            self.vim_data += output
                            if input_mode:
                                data += output

                            couple = self.ps1_pattern.findall(output)
                            if len(couple) > 0:
                                couple_hit = couple[-1]
                                couple_sp_l = couple_hit.split("@")
                                if len(couple_sp_l) == 2:
                                    self.role = couple_sp_l[0]
                                    self.hostname = couple_sp_l[1]

                        except OSError:
                            pass

                    if stdin_fd in rs:
                        inpt = os.read(stdin_fd, BUFSIZ)
                        os.write(self.pty_fd, inpt)

                        input_mode = True

                        if self.is_output(str(inpt)):
                            # 如果len(str(x)) > 1 说明是复制输入的
                            if len(str(inpt)) > 1:
                                data = inpt
                            match = self.vim_end_pattern.findall(self.vim_data)
                            if match:
                                if self.vim_flag or len(match) == 2:
                                    self.vim_flag = False
                                else:
                                    self.vim_flag = True
                            elif not self.vim_flag:
                                self.vim_flag = False
                                data = self.deal_command(data)[0:200]
                                if data is not None:
                                    # TtyLog(log=log, datetime=datetime.datetime.now(), cmd=data).save()
                                    # TODO: to record command
                                    # ffff.write("%s %s %s\n" % (self.role, self.hostname, data))
                                    tc = threading.Thread(target=self.report_command, args=(data,))
                                    tc.setDaemon(True)
                                    tc.start()

                            data = ''
                            self.vim_data = ''
                            input_mode = False

                    time.sleep(0.01)

        finally:
            termios.tcsetattr(stdin_fd, termios.TCSAFLUSH, stdin_origin_attr)
            log_file_f.write('End time is %s' % datetime.datetime.now())
            log_file_f.close()
            log_time_f.close()
            self.report_session_end()

    def get_log(self):
        """
        Logging user command and output.
        """
        tty_log_dir = os.path.join(LOG_DIR, 'tty')
        date_today = datetime.datetime.now()
        date_start = date_today.strftime('%Y%m%d')
        time_start = date_today.strftime('%H%M%S')
        today_connect_log_dir = os.path.join(tty_log_dir, date_start)
        log_file_path = os.path.join(today_connect_log_dir,
                                     '%s_%s_%s_%s' % (self.username, self.cs_name, date_start, time_start))
        self.log_file = log_file_path

        try:
            mkdir(os.path.dirname(today_connect_log_dir), mode=777)
            mkdir(today_connect_log_dir, mode=777)
        except OSError, e:
            if AUDIT_MODEL == 'strict':
                raise OSError('创建目录 %s 失败，请修改%s目录权限[%s]' % (today_connect_log_dir, tty_log_dir, e))
            else:
                pass

        try:
            os.system("touch %s.log" % (log_file_path,))
            os.system("touch %s.time" % (log_file_path,))
            log_file_f = open(log_file_path + '.log', 'a')
            log_time_f = open(log_file_path + '.time', 'a')
        except IOError, e:
            if AUDIT_MODEL == 'strict':
                raise IOError('创建tty日志文件失败, 请修改目录%s权限[%s]' % (today_connect_log_dir, e))
            else:
                pass

        pid = os.getpid()

        # 往数据库里写了一条登录记录,并获取到该log的id
        # log = Log(user=self.username, host=self.asset_name, remote_ip=self.remote_ip, login_type=self.login_type,
        #          log_path=log_file_path, start_time=date_today, pid=pid)
        # log.save()

        log_file_f.write('Start at %s\r\n' % datetime.datetime.now())
        return log_file_f, log_time_f  # , log

    def deal_command(self, data):
        """
        处理截获的命令
        :param data: 要处理的命令
        :return:返回最后的处理结果
        """
        command = ''
        try:
            self.stream.feed(data)
            # 从虚拟屏幕中获取处理后的数据
            for line in reversed(self.screen.buffer):
                line_data = "".join(map(operator.attrgetter("data"), line)).strip()
                if len(line_data) > 0:
                    parser_result = self.command_parser(line_data)
                    if parser_result is not None:
                        # 2个条件写一起会有错误的数据
                        if len(parser_result) > 0:
                            command = parser_result
                    else:
                        command = line_data
                    break
        except Exception:
            pass
        # 虚拟屏幕清空
        self.screen.reset()
        return command

    def __init_screen_stream(self):
        """
        初始化虚拟屏幕和字符流
        """
        self.stream = pyte.ByteStream()
        self.screen = pyte.Screen(80, 24)
        self.stream.attach(self.screen)

    @staticmethod
    def command_parser(command):
        """
        处理命令中如果有ps1或者mysql的特殊情况,极端情况下会有ps1和mysql
        :param command:要处理的字符传
        :return:返回去除PS1或者mysql字符串的结果
        """
        result = None
        match = re.compile('\[?.*@.*\]?[\$#]\s').split(command)
        if match:
            # 只需要最后的一个PS1后面的字符串
            result = match[-1].strip()
        else:
            # PS1没找到,查找mysql
            match = re.split('mysql>\s', command)
            if match:
                # 只需要最后一个mysql后面的字符串
                result = match[-1].strip()
        return result

    @staticmethod
    def is_output(strings):
        newline_char = ['\n', '\r', '\r\n']
        for char in newline_char:
            if char in strings:
                return True
        return False


if __name__ == "__main__":
    pty = Pty()
    pty.start()
