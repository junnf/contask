#!/usr/bin/env python
# encoding: utf-8

import getpass
import socket
import os
import sys

#import platform

def disp_cmd():
    user = getpass.getuser()
    host = socket.gethostname()
    pwd = os.path.basename(os.getcwd())
    sys.stdout.write("{}@{} {}>".format(user, host, pwd))
    sys.stdout.flush()

disp_cmd()

