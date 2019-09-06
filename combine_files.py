"""
Author: lt
Date: 2019-06-29
Description: 合并多个文件
"""

import fire
import os


def main(source, output):
    all_combine_paths = []
    all_text_set = set()
    if os.path.isdir(source):
        for root, dirs, files in os.walk(source):
            for filename in files:
                all_combine_paths.append(os.path.join(root, filename))
    else:
        all_combine_paths = source.split(',')
        all_combine_paths = {path.strip(' ').strip('\n').strip('\r')
                             for path in all_combine_paths}
        filter_func = lambda x: os.path.isfile(x)
        all_combine_paths = filter(filter_func, all_combine_paths)

    for path in all_combine_paths:
        with open(path, 'r') as fr:
            lines = fr.readlines()
            for line in lines:
                all_text_set.add(line)
    with open(output, 'w') as fw:
        for text in all_text_set:
            fw.write(text)

if __name__ == '__main__':
    fire.Fire(main)
