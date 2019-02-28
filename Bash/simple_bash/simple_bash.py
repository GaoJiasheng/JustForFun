#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2019/2/28 4:34 PM

# !/usr/bin/env python
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
ADMINS = ["gaojiasheng"]

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
        self.cs_name = socket.gethostname()
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

    def start(self):
        stdin_origin_attr = termios.tcgetattr(sys.stdin.fileno())

        data = ""
        input_mode = False

        pre_timestamp = time.time()

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

                            self.vim_data += output
                            if input_mode:
                                data += output

                        except OSError:
                            pass

                    if stdin_fd in rs:
                        inpt = os.read(stdin_fd, BUFSIZ)
                        os.write(self.pty_fd, inpt)

                        input_mode = True

                    time.sleep(0.01)

        finally:
            termios.tcsetattr(stdin_fd, termios.TCSAFLUSH, stdin_origin_attr)


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
