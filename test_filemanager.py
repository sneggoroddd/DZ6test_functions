from filemanager import  copy_file_or_directory, filenames, author_info, quit
import shutil
import os
import sys


def test_copy_file_or_directory():
    name = bill.py
    new_name = train1
    def copy_file_or_directory(name, new_name):
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copyfile(name, new_name)

    assert  train1 in os.listdir()
    os.rmdir(train1)

