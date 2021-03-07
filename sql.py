# -*- coding:utf-8 -*-
# author :wangxiao
# CREATETIME :2021/3/7 下午3:20


import pymysql
import pandas
from sqlalchemy import create_engine
import datetime
# 连接数据库
class SQL:
    def __init__(self):
        self.connect = pymysql.connect(
            host='47.102.113.194',  # 需要连接的主机IP地址
            user='root',  # MySQL数据库用户名
            passwd='123456',  # MySQL数据库密码
            db='karst',  # 数据库
            port=3306,  # 端口
            charset='utf8'  # 字符集
        )
        #self.engine = create_engine(self.connect)

    def python(self):
        today = datetime.datetime.today().strftime("%Y-%m-%d")  # 过去今天时间
        with self.connect.cursor() as cursor:
            sql = 'select date_time, cpu, memory from python;'
            # df = pandas.read_sql(sql, con=self.connect)
            # df.to_sql(today, con=self.connect)
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    def karst(self):
        with self.connect.cursor() as cursor:
            sql = 'select date_time, cpu, memory from karst;'
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    def hplc(self):
        with self.connect.cursor() as cursor:
            sql = 'select date_time, cpu, memory from hplcs;'
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    def data(self):
        with self.connect.cursor() as cursor:
            sql = 'select date_time, cpu, memory from databased;'
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    def cpu(self):
        with self.connect.cursor() as cursor:
            sql = 'select date_time, user, system from cpu;'
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    def memory(self):
        with self.connect.cursor() as cursor:
            sql = 'select date_time, userd, free from memory;'
            cursor.execute(sql)
            result = cursor.fetchall()
        df = pandas.DataFrame(result)
        df.columns
        return df

    # # 生成dataframe
    # def to_Frame_python(self): #KarstServic+
    #     df = pandas.DataFrame(self.python())
    #     df.columns
    #     return df


if __name__ == '__main__':
    print(SQL().cpu())