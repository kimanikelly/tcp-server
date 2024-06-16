import mysql.connector as sql
import os
import dotenv

dotenv.load_dotenv()

sql_host = os.getenv("SQL_HOST")

sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")
sql_database = os.getenv("SQL_DATABASE")

db = sql.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)
