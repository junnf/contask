#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from os import system


class Task(object):
    """doc Task herit from GraphNode"""

    def __init__(self, task_name, pre = None):
        self.task_name = task_name
        #pre = [a,b,c]
        self.pre = pre
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
    _temp_task = []
    if sys.argv[1] == "-c":
        with open("../test/task.conf") as f:
            for line in f:
                if line[0] == "#":
                    continue
                else:
                    _temp_task.append(line.strip().strip("[").strip("]"))


    else:
        task = Task(sys.argv[1])


if __name__ == "__main__":
    main()
