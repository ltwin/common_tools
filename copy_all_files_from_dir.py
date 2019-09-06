"""
Author: lt
Date: 2019-06-27
Description: 将文件夹下的所有文件（包含子目录中的文件）都拷贝到另一个文件夹中
"""

import fire
import os
import shutil


def main(dirname, output):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            path = os.path.join(root, filename)
            shutil.copy(path, output)

if __name__ == "__main__":
    fire.Fire(main)
