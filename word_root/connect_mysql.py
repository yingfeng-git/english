#!/usr/bin/python3
# coding = utf-8
import pymysql
from sshtunnel import SSHTunnelForwarder
import json


class ConnectMysql(object):
    def __init__(self):
        with open("db.json", 'r', encoding='utf-8') as db:
            self.conf = json.load(db)

        conf = self.conf
        self.server = SSHTunnelForwarder((conf['ip'], conf['port']),
                                         ssh_username=conf['user'],
                                         ssh_password=conf['pwd'],
                                         remote_bind_address=('localhost', 3306))
        self.server.start()
        self.db_connect = pymysql.connect(host='localhost',
                                          port=self.server.local_bind_port,
                                          user=conf['db_user'],
                                          passwd=conf['db_pwd'],
                                          db=conf['db_name'])
        self.p = self.db_connect.cursor()

    def close(self):
        self.p.close()
        self.connect().close()
        self.server.stop()

    def connect(self):
        return self.p

