'''
这个是几个基本组件，目前组件有：
获取代理ip
数据库的类
'''
import requests
import random
import re
import pymysql


class Sql:
    def __init__(self, host, username, password, database):
        self.con = pymysql.connect(host, username, password, database)
        self.cursor = self.con.cursor()
        print('数据库连接正常')

    def execute(self, command):
        try:
            self.cursor.execute(command)
            fetch = self.cursor.fetchall()
            self.con.commit()
        except ValueError:
            self.con.rollback()
        return "返回值：{}".format(fetch)


def getsdf_proxy():
    '''这个是随机挑一个ip来爬虫用'''
    with open('暂时用不到/ips-static.txt', 'r') as file:
        lines = file.readlines()
        line = random.choice(lines)[:-1]
        line = re.split(':', line)

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": line[0],
        "port": line[1],
        "user": line[2],
        "pass": line[3],
    }

    proxy_handler = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    print(proxy_handler)
    print(requests.get('http://httpbin.org/ip', proxies=proxy_handler).text)


def get_proxy():
    with open('ips-static.txt', 'r') as file:
        lines = file.readlines()
        line = random.choice(lines)[:-1]
        line = re.split(':', line)

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": line[0],
        "port": line[1],
        "user": line[2],
        "pass": line[3],
    }

    proxy_handler = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    return proxy_handler
