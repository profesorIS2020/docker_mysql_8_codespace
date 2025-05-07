import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="myuser",
    password="mypass",
    database="testdb",
    port=3306
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
version = cursor.fetchone()
print("MySQL version:", version)

conn.close()

