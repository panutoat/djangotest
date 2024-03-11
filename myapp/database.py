import psycopg2
from psycopg2 import Error

def authenticate_user(username, password):
    try:
        conn_params = {
            "host": "skr-cleansing-db.cluster-cnuupdm1vvla.ap-southeast-1.rds.amazonaws.com",
            "database": "postgres",
            "user": "postgres",
            "password": "password"
        }
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()

        # คำสั่ง SQL สำหรับ query ข้อมูลของผู้ใช้
        sql_query = f'''
        SELECT username,password FROM demo."user" where username = '{username}' and password = '{password}'
        '''
        cursor.execute(sql_query)
        user = cursor.fetchone()  
        if user:
            user_dict = {'username': user[0], 'password': user[1]}
            print (user_dict)
            return user_dict
        else:
            return None
            
    except (Exception, psycopg2.Error) as error:
        print("เกิดข้อผิดพลาดในการเชื่อมต่อ PostgreSQL:", error)
        return False
    finally:
        # ปิดการเชื่อมต่อ
        if connection:
            cursor.close()
            connection.close()
            print("การเชื่อมต่อ PostgreSQL ถูกปิด")
