#!/usr/bin/env python
# encoding: utf-8

import os
from constants import *

__all__ = ['cd','exit']

def cd(args):
    if len(args) > 0:
        os.chdir(args[0])
    else:
        os.chdir(os.getenv('HOME'))
    return RUN_STATUS

def exit(args):
    return STOP_STATUS

