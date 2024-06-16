import mysql.connector as sql
import os
import dotenv

dotenv.load_dotenv()

sql_host = os.getenv("SQL_HOST")
sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")


db = sql.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password
)
