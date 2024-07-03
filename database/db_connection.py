import mysql.connector as sql
import os
import dotenv

dotenv.load_dotenv()

sql_host = os.getenv("SQL_HOST")
sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")
sql_database = os.getenv("SQL_DATABASE")

register_query = "INSERT INTO users (username,password,join_date,entries) VALUES (%s, %s, %s, %s)"

db = sql.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)

cursor = db.cursor()
