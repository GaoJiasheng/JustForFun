#!/bin/bash
if $(tmux has-session 2>/dev/null); then tmux att; exit; fi
tmux new-session -d -n sh -s 0 -c /Users/gavin/work/apue-practice
tmux send-keys -t 0:1.1 "-zsh" C-m
tmux select-layout -t 0:1 "5bdb,143x39,0,0[143x29,0,0,0,143x9,0,30,1]" > /dev/null
tmux split-window -d -t 0:1 -c /Users/gavin/work/apue-practice
tmux send-keys -t 0:1.2 "-zsh" C-m
tmux select-layout -t 0:1 "5bdb,143x39,0,0[143x29,0,0,0,143x9,0,30,1]" > /dev/null
tmux att
