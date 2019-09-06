"""
Author: lt
Date: 2019-06-26
Description: 根据域名列表对应的hostname移动对应文件夹，
    如从文件中读取到域名http://www.a.com和http://www.b.com，
    那么就从source文件夹中寻找名为www.a.com和www.b.com的文件夹移动到目标目录，
    注意当文件名冲突时会覆盖
"""
import sys
sys.path.append('./..')
import fire
import os
import shutil

from common import get_host_from_url


def main(sites_p, source_d, output_d):
    with open(sites_p, 'r') as fr:
        print("Read sites from file: {}".format(sites_p))
        all_hosts = []
        data = fr.readlines()
        for site in data:
            site = site.replace('\r', '').replace('\n', '').replace(' ', '')
            if site:
                try:
                    host = get_host_from_url(site)
                    all_hosts.append(host)
                except Exception:
                    print("Get host failed, the site: {}".format(site))
                    pass
    print("All dir to move count: {}".format(len(all_hosts)))
    for host in all_hosts:
        print("Move dir: {}".format(host))
        target_dir = os.path.join(source_d, host)
        new_dir = os.path.join(output_d, host)
        if os.path.exists(new_dir):
            print("The dir already exists, now relace it: {}".format(target_dir))
            os.system("rm -rf {}".format(new_dir))
        try:
            shutil.move(target_dir, output_d)
        except Exception as err:
            print(err)
    print("Move successfully!")


if __name__ == "__main__":
    fire.Fire(main)
