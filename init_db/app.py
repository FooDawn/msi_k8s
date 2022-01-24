import mysql.connector
import json
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)


@app.route('/')
def db_init():
  try:
    mydb_conn = mysql.connector.connect(
      host="mysql",
      user="root",
      password="gesl0"
    )
    cursor = mydb_conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS bullet_points")
    cursor.execute("CREATE DATABASE bullet_points")
    cursor.close()

    mydb_conn = mysql.connector.connect(
      host="mysql",
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

  except mysql.connector.Error as error:
      return ("Failed to get record from MySQL table: {}".format(error))


if __name__ == "__main__":
  app.run(port=5001)

