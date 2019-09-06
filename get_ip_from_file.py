"""
Author: lt
Date: 2019-06-29
Description: 从文件文本中获取所有ip
"""

import fire
import re


def main(source=None, output='./output.txt', text=None):
    if not text:
        with open(source, 'r') as fr:
            text = fr.read()
    all_ip_list = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
    with open(output, 'w') as fw:
        for ip in all_ip_list:
            fw.write(ip + '\n')


if __name__ == '__main__':
    fire.Fire(main)
