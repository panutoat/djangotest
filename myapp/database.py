import psycopg2
from psycopg2 import Error
conn_params = {
    "host": "skr-cleansing-db.cluster-cnuupdm1vvla.ap-southeast-1.rds.amazonaws.com",
    "database": "postgres",
    "user": "postgres",
    "password": "password"
}

def authenticate_user(username, password):
    try:
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


def query_db(query):
    try:
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall() 
        result = []

        for row in rows:
            column_names = [desc[0] for desc in cursor.description]  
            row_dict = dict(zip(column_names, row)) 
            result.append(row_dict)
        return result
    except (Exception, psycopg2.Error) as error:
        return False
    finally:

        if connection:
            cursor.close()
            connection.close()

def query_to_db(query):
    try:
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Record inserted successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
        connection.rollback()
    finally:

        cursor.close()
        connection.close()

