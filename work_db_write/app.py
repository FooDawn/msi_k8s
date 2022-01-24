import mysql.connector
import json
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response
from random import randint
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/home')
def hello():
  return 'Hello, Friend!\n This is possible due to Poocco\n'

@app.route('/', methods =["GET", "POST"])

@app.route('/write_points', methods =["GET", "POST"])
def writting():

  if request.method == "POST":
    # getting input with name = bname in HTML form
    try:
      if request.is_json:
        h_name = request.json.get("bname")
        h_desc = request.json.get("desc")

        mydb_conn = mysql.connector.connect(
          host="mysql",
          user="root",
          password="gesl0",
          database="bullet_points"
        )

        cursor = mydb_conn.cursor()
        sql = "INSERT INTO points (name, description) values (%s, %s)"
        values = (h_name, h_desc)
        cursor.execute(sql, values)
        mydb_conn.commit()

        sql_id = "SELECT * FROM points where name = %s and description = %s;"
        cursor.execute(sql_id, values)
        results = cursor.fetchall()
        cursor.close()

        result = results[0]
        response_body = {
            "return_num" : result[0],
            "return_name": result[1],
            "return_desc" : result[2]
        }
        
        res = make_response(jsonify(response_body), 200)
        return res

    except mysql.connector.Error as error:
      return ("Failed to get record from MySQL table: {}".format(error))

  res = make_response(jsonify({}), 400)
  return res



if __name__ == "__main__":
  app.run(port = 5003)
