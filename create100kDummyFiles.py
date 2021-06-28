#!/usr/bin/env python
import os
import subprocess

test_path = "test_folder"

#put the number as you wish
n = 100000

work_path = os.path.abspath(os.path.dirname(__file__))

# create folder
if not os.path.exists(test_path):
    os.mkdir(test_path)

for i in range(n):
    open(work_path + "\\" + test_path + "\\" + "testFile"+str(i).zfill(len(str(n)))+".test", 'a').close()