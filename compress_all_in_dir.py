"""
从一个文件夹中获取所有层级目录中的文件，然后压缩打包，支持zip和tar
"""
import fire
import os
import zipfile
import tarfile


def make_zip(source_dir, output):
    """
    遍历出目录及其子目录中的所有文件，打包成zip
    :param source_dir:
    :param output:
    :return:
    """
    zipf = zipfile.ZipFile(output, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()


def make_targz(source_dir, output):
    """
    将目录整个打包
    :param output:
    :param source_dir:
    :return:
    """
    with tarfile.open(output, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def make_targz_one_by_one(source_dir, output):
    """
    遍历出目录及其子目录中的所有文件，打包成tar.gz
    :param output:
    :param source_dir:
    :return:
    """
    tar = tarfile.open(output, "w:gz")
    for root, dir, files in os.walk(source_dir):
        for file in files:
            pathfile = os.path.join(root, file)
            tar.add(pathfile)
    tar.close()


def main(source_dir, output, ztype='tar.gz'):
    if ztype == 'tar.gz':
        make_targz_one_by_one(source_dir, output)
    elif ztype == 'zip':
        make_zip(source_dir, output)
    else:
        print('Not supported compress type!')
        return

if __name__ == '__main__':
    fire.Fire(main)
