import pymysql
#创建连接
mydb = pymysql.connect(
    host ='localhost',
    user ='root',
    passwd ='root',
    database = 'gaocun'
)
mycursor = mydb.cursor()

def load2mysql(username,password,telephone,email):
    # insert data way2
    insert_sql1 = 'insert into login values (%s,%s,%s,%s)'
    val = (username,password,telephone,email)
    mycursor.execute(insert_sql1, val)
    mydb.commit()
    print('load data end.')
    mydb.close()
