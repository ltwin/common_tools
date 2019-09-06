"""
按照树形图统计目录下每个层级的文件数
examples:
    |-dir1(50)
        |-subdir1(25)
        |-subdir2(25)
    |-dir2(20)
        |-subdir1(10)
            |-subdir1(5)
            |-subdir2(5)
        |-subdir2(10)
"""

import fire
import os


def get_dir_depth(dir_path):
    path_seg = dir_path.strip('.').strip('/').split('/')
    return len(path_seg)


def tree_count(start_depth, dirs):
    result_list = []
    for dir_path in dirs:
        if not os.path.isdir(dir_path):
            continue
        all_files_sub = []
        for root, dirs, files in os.walk(dir_path):
            all_files_sub.extend(files)
        count = len(all_files_sub)
        result_list.append('{}|-{}: {}'.format('  ' * (
            get_dir_depth(dir_path) - start_depth), dir_path, count))
        subdirs = os.listdir(dir_path)
        subdirs = [os.path.join(dir_path, subdir) for subdir in subdirs]
        if subdirs:
            result_list.extend(tree_count(start_depth, subdirs))
    return result_list


def main(dirname, output=None):
    result_list = tree_count(get_dir_depth(dirname), [dirname])
    if output:
        with open(output, 'w') as fw:
            for result in result_list:
                fw.write(result + '\n')
    else:
        for result in result_list:
            print(result)


if __name__ == "__main__":
    fire.Fire(main)
