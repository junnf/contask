#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from os import system


class Task(object):
    """doc Task herit from GraphNode"""

    def __init__(self, task_name):
        self.task_name = task_name
        self.run()

    def __run(self):
        #test run in shell
        system(self.task_name)

    def __conf(self):
        pass

    def __load(self, conf):
        pass

    def run(self):
        self.__run()

    def conf(self,conf):
        self.__load(conf)

def main():
    task = Task(sys.argv[1])


if __name__ == "__main__":
    main()
