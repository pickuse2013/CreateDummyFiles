#!/usr/bin/env python
import os
import subprocess

# test folder (auto create)
test_path = "test_folder2"

# put the number as you wish
n = 100000

work_path = os.path.abspath(os.path.dirname(__file__))

if not os.path.exists(test_path):
    os.mkdir(test_path)

for i in range(n):
    # create folder
    path_name = test_path + "\\test" + str(i).zfill(len(str(n)))
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    open(work_path + "\\" + path_name + "\\" + "testFile001.test", 'a').close()