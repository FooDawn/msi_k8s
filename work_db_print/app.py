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
def get_points() :
  if request.method == "POST":
    try:
      if request.is_json:
        h_num_id = request.json.get("num_id")

        mydb_conn = mysql.connector.connect(
          host="database_ms",
          user="root",
          password="gesl0",
          database="bullet_points"
        )
        cursor = mydb_conn.cursor()

        sql = "SELECT * FROM points where id = %s;"
        cursor.execute(sql, (h_num_id,))

        results = cursor.fetchall()
        
        result = results[0]
        response_body = {
            "return_num" : result[0],
            "return_name": result[1],
            "return_desc" : result[2]
        }
        
        res = make_response(jsonify(response_body), 200)   
        cursor.close()
        return res
        
      res = make_response(jsonify({}), 400)    

      return res

    except mysql.connector.Error as error:
      return ("Failed to get record from MySQL table: {}".format(error))

  return "Nic nisi POST-al. Pojdi na /\n"


if __name__ == "__main__":
  app.run(port = 5000)
