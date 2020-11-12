from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    db = SQLAlchemy(app) # new instance of db connection
    return db



















# import psycopg2

# connection = psycopg2.connect(
#     database="library_api",
#     user="app",
#     password="app", os.getenv("db_password")
#     host="localhost"
# )

# cursor = connection.cursor()

# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
# connection.commit()