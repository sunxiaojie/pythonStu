import pymysql

db = pymysql.connect("192.168.1.2", "root", "", "db_pinpianyi")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT id,vehicle_volume from logistics_vehicle_type")

print(cursor.fetchall())
# 使用 fetchone() 方法获取单条数据.
data = cursor.rowcount

print("Database version : %s " % data)

# 关闭数据库连接
db.close()