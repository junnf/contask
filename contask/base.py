#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from os import system


class Task(object):
    """doc Task herit from GraphNode"""

    def __init__(self, task_name, _pre = None, _next = None):
        self.task_name = task_name
        self._pre = _pre
        self._next = _next
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

class TaskGraph(object):

    def __init__(self):
        """
            you should add task node in the list,
            and you can use other Persistent-List
        """
        self.graph = []

    def add_node(self, node):
        """

        """
        if isinstance(node, Task) == False:
            import pprint; pprint.pprint("You should add Task-instance ")




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
