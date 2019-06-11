from flask import Flask, request, jsonify, render_template
import sqlite3
import os 
import datetime

app = Flask ('app', template_folder='templates')

def initSQL():
  # os.remove('database.db')
  db = sqlite3.connect('database.db')
  cur = db.cursor()
  cur.execute("CREATE TABLE BLOGPOSTS(POST CHAR(255), DATE CHAR(255));")
initSQL()
def getposts():
  with sqlite3.connect("database.db") as con:
    sql="SELECT * from BLOGPOSTS;"
    cur=con.cursor()
    cur.execute(sql)
    POSTS = []
    while True:
        record=cur.fetchone()
        if record==None:
          break
        POSTS.append(record)
        print (record)
    return POSTS


def save(blogpost):
  # year = datetime.date().year()
  # month = datetime.date().month()
  now = datetime.datetime.now()
  year = now.year
  month = now.month
  day = now.day
  # day = datetime.datetime().day()
  with sqlite3.connect("database.db") as con:
      name = "bob"
      cur = con.cursor()
      cur.execute("INSERT INTO BLOGPOSTS (POST, DATE) VALUES ('{}', '{}-{}-{}')".format(blogpost, str(year), str(month), str(day)))
      con.commit()
      msg = "Done"
      return getposts()

@app.route('/', methods = ["POST", "GET"])
def index():
  blogposts=getposts()
  if(request.method == "POST"):
    blogpost = request.form['blogpost']
    print(blogpost)
    blogposts=save(blogpost)
  blogposts.reverse()
  print(blogposts)
  return render_template("index.html", blogposts=blogposts)



app.run(host="localhost", port=8080)