#!/usr/bin/env python
import os
import subprocess

test_path = "test_folder2"

#put the number as you wish
n = 100

work_path = os.path.abspath(os.path.dirname(__file__))

for i in range(n):
    # create folder
    path_name = test_path + str(i).zfill(len(str(n)))
    if not os.path.exists(path_name):
        os.mkdir(path_name)

    # switch folder
    os.chdir(os.path.expanduser(work_path + "/" + path_name))
    
    subprocess.call(['touch', "testFile0001.test"])