import psycopg2
import time 

while True:
    try:
        conn = psycopg2.connect(database = "History", 
                                user = "user", 
                                host= 'postgres',
                                password = "password",
                                port = 5432)

        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS History (
                    timestamp TIMESTAMP PRIMARY KEY,
                    pred INT,
                    label INT
        );""")

        conn.commit()

        cursor.close()
        conn.close()
        print("Database connection successful")
        break
    except:
        print("Connecting...")
        time.sleep(5)

def add(pred,trueVal):
    conn = psycopg2.connect(database = "History", 
                        user = "user", 
                        host= 'postgres',
                        password = "password",
                        port = 5432)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO History (timestamp,pred,label) VALUES
                   (NOW(), {}, {});""".format(pred,trueVal))
    conn.commit()
    cursor.close()
    conn.close()

def extract():
    conn = psycopg2.connect(database = "History", 
                        user = "user", 
                        host= 'postgres',
                        password = "password",
                        port = 5432)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM History""")
    records = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return records