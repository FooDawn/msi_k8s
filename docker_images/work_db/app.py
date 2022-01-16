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

@app.route('/')
def hello_world():
  quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
      "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
      "'To understand recursion you must first understand recursion..' -- Unknown",
      "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
      "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
      "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
  randomNumber = randint(0, len(quotes) - 1)
  quote = quotes[randomNumber]
  return render_template('hello.html', **locals())


@app.route('/get_points', methods =["GET", "POST"])
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

  return render_template("print.html")

# flask ma handlarja za errorje
@app.route('/write_points', methods =["GET", "POST"])
def writting():

  if request.method == "POST":
    # getting input with name = bname in HTML form
    
    if request.is_json:
      h_name = request.json.get("bname")
      h_desc = request.json.get("desc")

      mydb_conn = mysql.connector.connect(
        host="database_ms",
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

  res = make_response(jsonify({}), 400)
  return res




if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 5000)
