import mysql.connector
#创建连接
mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd ='root',
    database = 'gaocun'
)
print(mydb)
#get cursor
mycursor = mydb.cursor()
#create table
ddl_sql ='''
create table if not exists python_test(
id int,
name varchar(20),
age int);
'''
ddl_truncate = 'truncate TABLE python_test;'
mycursor.execute(ddl_sql,params=None,multi=True)
mycursor.execute(ddl_truncate)
mydb.commit()

#insert data way1
insert_sql = '''
insert into python_test values (
1,'高存',22)
'''
mycursor.execute(insert_sql)
mydb.commit()

#insert data way2
insert_sql1 = 'insert into python_test values (%s,%s,%s)'
val = (2,"大王",33)
mycursor.execute(insert_sql1,val)
mydb.commit()

#insert batch data way2
insert_batch_sql = 'insert into python_test values (%s,%s,%s)'
var_batch = [
(3,"小明",33),
(4,"小红",33),
(5,"詹妮",33),
(6,"丹尼佛",33)
]
mycursor.executemany(insert_batch_sql,var_batch)
mydb.commit()

#delete data
delete_sql = 'delete  from python_test  where id = 1'
mycursor.execute(delete_sql)
mydb.commit()

#update data
update_sql = '''
update python_test set name = '大王-更'   where id = 2
'''
mycursor.execute(update_sql)
mydb.commit()

#select data
select_sql = 'select * from python_test'
mycursor.execute(select_sql)
result = mycursor.fetchall()
print('id   ','name    ','age   ')
for re in result:
    print(re[0],'   ',re[1],'   ',re[2])
