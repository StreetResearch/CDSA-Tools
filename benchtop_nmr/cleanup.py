#!/usr/bin/env python

import fnmatch
import os
import shutil

for root, dirs, files in os.walk('.'):
    for name in dirs:
        if fnmatch.fnmatch(name, '*SHIM*'):
            print('deleting folder: '+ os.path.join(root, name))
            shutil.rmtree(os.path.join(root, name))

for root, dirs, files in os.walk('.'):
    for name in dirs:
        if fnmatch.fnmatch(name, '*STANDBY*'):
            print('deleting folder: '+ os.path.join(root, name))
            shutil.rmtree(os.path.join(root, name))

#for folder in os.listdir('.'):
#    if fnmatch.fnmatch(folder, '*SHIM*'):
#        shutil.rmtree(folder)

#for folder in os.listdir('.'):
#    if fnmatch.fnmatch(folder, '*STANDBY*'):
#        shutil.rmtree(folder)

print('Good evening kind sir or madam. I have deleted those pesky extra folders that the NMR copied. I wish you a pleasant day. Toodle Pip')
os.system("pause")

