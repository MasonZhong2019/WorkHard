"""
mysql 操作数据库的基本流程
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
# 获取游标（用于进行数据操作的对象，同时承载操作结果）
cur = db.cursor()

# 执行sql语句,外边用双，里面就用单　
sql = "insert into myclass\
(name,sex,age,score) values\
            ('Lily','F',20,78);"
cur.execute(sql)

db.commit()
cur.close()
db.close()
