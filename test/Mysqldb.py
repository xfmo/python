#!/usr/bin/env python
#-*-coding:utf-8-*-
import MySQLdb

def main():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="courade")
    conn.select_db("puzhi")
    cursor = conn.cursor()
    print cursor.execute("desc pz_user")
    print cursor.fetchall()

if __name__ == "__main__":
    main()
