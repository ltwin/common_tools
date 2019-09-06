"""
从文件中移除重复的行
"""

import fire


def main(path):
    with open(path, 'r') as fr:
        data_list = fr.readlines()
        result_set = {data.strip(' ').strip('\r').
                          strip('\n') for data in data_list}
    with open(path, 'w') as fw:
        for result in result_set:
            fw.write(result + '\n')


if __name__ == '__main__':
    fire.Fire(main)
