#!/usr/bin/python2.7.2
# -*- coding: utf-8 -*-

import sys, math, datetime
import MySQLdb

# constant
DB_HOST = "127.0.0.1"
DB_USER = "user"
DB_PSWD = "pswd"
DB_PORT = 3306

# 時刻表示
def disp_time(prc):
    systime = datetime.datetime.now().strftime(u'%Y/%m/%d %H:%M:%S')
    print prc + ' -> ' + systime

# SQL実行
def execute_sql():

    try:
        conn = MySQLdb.connect(host=DB_HOST, db="test", port=DB_PORT,\
                               user=DB_USER, passwd=DB_PSWD, charset="utf8")    
    
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS hoge")
        cursor.execute("CREATE TABLE hoge(\
                        id INT(11) PRIMARY KEY AUTO_INCREMENT,\
                        com VARCHAR(200))")
        
    except MySQLdb.Error, e:    
        print "SQL ERROR %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        if conn: conn.close
        if cursor: cursor.close

# メイン処理部
if __name__ == "__main__":

    disp_time('start')

    execute_sql()

    disp_time('end  ')
