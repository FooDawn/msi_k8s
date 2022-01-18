import mysql.connector
import json
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('hello.html')


@app.route('/create_db')
def db_init():
  mydb_conn = mysql.connector.connect(
    host="database_ms",
    user="root",
    password="gesl0"
  )
  cursor = mydb_conn.cursor()

  cursor.execute("DROP DATABASE IF EXISTS bullet_points")
  cursor.execute("CREATE DATABASE bullet_points")
  cursor.close()

  mydb_conn = mysql.connector.connect(
    host="database_ms",
    user="root",
    password="gesl0",
    database="bullet_points"
  )
  cursor = mydb_conn.cursor()

  cursor.execute("DROP TABLE IF EXISTS points")
  cursor.execute("CREATE TABLE points (id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), description text(2000), PRIMARY KEY (id))")
  mydb_conn.commit()
  
  cursor.close()

  return 'Database is created and it is empty.\n'

    
if __name__ == "__main__":
  app.run(host ='0.0.0.0', port=5001)
