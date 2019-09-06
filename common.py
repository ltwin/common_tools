"""
公用函数
"""
import chardet
import hashlib
import re

from loguru import logger
from urllib import parse


def get_md5(content):
    """
    生成MD5
    :param content: 任意数据
    :return 数据的md5值
    """
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()


def url_parsing_init(url):
    """
    url解析初始化
    """
    if not url:
        return False, False, False, False
    try:
        protocol, rest = parse.splittype(url)
        if protocol is None:
            protocol = 'http'
            rest = '//' + rest
        host, rest = parse.splithost(rest)
        host, port = parse.splitport(host)
        if port is None:
            if protocol == 'https':
                port = '443'
            else:
                port = '80'
    except Exception as err:
        logger.warning('Input url is illegal: {}, error:'
                       ' {}'.format(url, err))
        return False, False, False, False
    return protocol, host, port, rest


def standard_url(url, with_rest=True):
    """
    标准化url数据
    :param url: 需要标准化的url
    :type url: str
    :param with_rest: 是否带上子页面
    :type with_rest: bool
    :return:
    """
    protocol, host, port, rest = url_parsing_init(url)
    if not all([protocol, host, port]):
        return False
    rest = rest.strip('/')
    if with_rest and rest:
        ret = ''.join([protocol, '://', host, ':', port, '/', rest, '/'])
    else:
        ret = ''.join([protocol, '://', host, ':', port, '/'])
    return ret


def get_host_from_url(url, with_port=False, with_type=False):
    """
    获取除去协议和端口的父域名
    :param url: 待解析url
    :type url: str
    :param with_port: 返回时是否加上端口
    :type with_port: bool
    :param with_type: 返回时是否加上protocol
    :type with_type: bool
    :return:
    """
    try:
        protocol, res = parse.splittype(url)
        host, res = parse.splithost(res)
        if not host:
            host = res
        domain, port = parse.splitport(host)
        if with_type:
            domain = ''.join([protocol, '://', domain])
        if with_port:
            domain = ''.join([domain, ':', port])
        return domain
    except Exception as err:
        logger.warning('Get host failed, url: {}, error: {}'.format(url, err))


def guess_and_decode(content):
    """
    猜测并解码
    :param content:
    :return:
    """
    encoding = chardet.detect(content)['encoding']
    if encoding == 'GB2312':
        # 扩大编码范围，防止一些特殊符号导致无法解码
        encoding = 'GB18030'
    try:
        content = content.decode(encoding)
    except AttributeError:
        logger.info('The content is already str type, not need to decode.')
        return content
    except Exception as err:
        logger.warning('Decoding failed, now use utf-8,'
                       ' the error: %s' % err)
        try:
            content = content.decode('utf-8')
        except UnicodeDecodeError:
            logger.warning('Cannot decode the page!')
            return ''
    return content


def is_ip(ip_str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip_str):
        return True
    else:
        return False


def is_url(url_str):
    url_regex = re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)")
    if url_regex.match(url_str) and url_str != "http://" and url_str != "https://":
        return True
    else:
        return False
