#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import signal

from constants import *
import shlex
from loop_process import disp_cmd

from funct import *

func_map_cmd = {}

def pass_signal(arg):
    pass

def add_map(cmd_name, func_name):
    """
        映射关系增加命令
    """
    func_map_cmd[cmd_name] = func_name

def ini(cmd_name_list = [], func_name_list = []):
    if cmd_name_list == [] or func_name_list == [] :
        return

def test_one(filename):
    body = file(filename, 'rt').read()
    __lex = shlex.shlex(body)
    for x in __lex:
        print x,"\n"
    #  print repr(body)

def test_two():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    while True:
        cmd_get = sys.stdin.readline()
        disp_cmd()

if __name__ == "__main__":
    test_two()
