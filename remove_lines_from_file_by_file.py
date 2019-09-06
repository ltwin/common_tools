"""
Author: lt
Date: 2019-06-29
Description: 根据一个文件中的行删除另一个文件中行
"""

import fire


def main(source, target, output=None, reverse=0):
    add_lines = []
    with open(source, 'r') as fr:
        rm_lines = fr.readlines()
    with open(target, 'r') as fr:
        tg_lines = fr.readlines()
    for rm_line in rm_lines:
        if rm_line in tg_lines:
            add_lines.append(rm_line)
            tg_lines.remove(rm_line)
    if not output:
        output = target
    with open(output, 'w') as fw:
        if reverse:
            for add_line in add_lines:
                fw.write(add_line)
        else:
            for tg_line in tg_lines:
                fw.write(tg_line)


if __name__ == '__main__':
    fire.Fire(main)
