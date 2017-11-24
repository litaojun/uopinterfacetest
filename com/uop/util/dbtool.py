#!/usr/bin/env python
# coding=utf-8

import MySQLdb
import types 

#http://www.mikusa.com/python-mysql-docs/query.html
def connectdb(host="",user="",passwd="",dbname=""):
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = MySQLdb.connect(host,user,passwd,dbname,charset='utf8')
    print('连接上了!')
    return db


def createtable(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""

    # 创建Sutdent表
    cursor.execute(sql)

def insertdb(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO Student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""

    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print '插入数据失败!'
        db.rollback()

#http://www.mikusa.com/python-mysql-docs/query.html
def querydb(db=None,sql="",data=None):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    results = None
    try:
        if data is None :
            # 执行SQL语句
            cursor.execute(sql)
        else:
            if type(data) is types.TupleType :
                 cursor.execute(sql,data)
        # 获取所有记录列表
        results = cursor.fetchall()
        print type(results),results,results[0][1]
#         for row in results:
#             ID = row[0]
#             Name = row[1]
#             Grade = row[2]
#             # 打印结果
#             print "ID: %s, Name: %s" % \
#                 (ID, Name)
    except:
        print "Error: unable to fecth data"
    return results

def querydbByParam(db=None,sql="",data=None):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    #sql = "SELECT * FROM Student"
    try:
        if data is None :
            # 执行SQL语句
            numrows = cursor.execute(sql)
        else:
            if type(data) is types.TupleType :
                 numrows = cursor.execute(sql,data)
        # 获取所有记录列表
        print "Selected %s rows" % numrows      
        print "Selected %s rows" % cursor.rowcount
    except:
        print "Error: unable to fecth data"
        
def deletedb(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
        print '删除数据失败!'
        # 发生错误时回滚
        db.rollback()

def updatedb(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print '更新数据失败!'
        # 发生错误时回滚
        db.rollback()

def closedb(db):
    db.close()

def main():
    db = connectdb(host="uop-dev-wx.cmcutmukkzyn.rds.cn-north-1.amazonaws.com.cn",user="root",passwd="Bestv001!",dbname="uop")    # 连接MySQL数据库
    querydbByParam(db,"select * from t_attribute c where c.ITEM_ID = %s",("06c8db68-b2f5-4f46-bbc7-e36d1e7062da",))
    querydb(db,"select * from t_attribute c where c.ITEM_ID = %s",("06c8db68-b2f5-4f46-bbc7-e36d1e7062da",))
    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()