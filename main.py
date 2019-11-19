from flask import Flask, render_template, request
import sqlite3 as sql
import math
import time
import redis
import random
from datetime import datetime, timedelta

app = Flask(__name__)
# redis_host = "localhost"
# redis_port = 6379
# redis_password = ""'''

import csv 
import sys
import os

cachename = 'chaitanyaazureredis'
r = redis.StrictRedis(host='chaitanyaazureredis.redis.cache.windows.net', port=6380, db=0, password="nzMD8Sg2yns2JUcCDmEUmRophxQPZEuPALa4VkVohD4=", ssl=True)
conn = sql.connect('db.db')

# coloumn_names = ["time","latitude","longitude","depth","mag","magType","nst","gap","dmin","rms", "id", "place", "depthError", "magError", "magNst", "locationSource"]
# myfile = open("quakes.csv","r")
# csv_reader = csv.DictReader(myfile, fieldnames=coloumn_names)
# next(csv_reader)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
		starttime = time.time()
		con = sql.connect("db.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		# cur.execute("select count(*),locationSource from earthquakes where mag >="+ mag +" group by locationSource limit 0,8")
		cur.execute("select count(*) from earthquakes where mag BETWEEN '0.0' and '2.0'")
		rows = cur.fetchone()
		cur.execute("select count(*) from earthquakes where mag BETWEEN '2.1' and '4.0'")
		rows1 = cur.fetchone()
		cur.execute("select count(*) from earthquakes where mag > '4.0'")
		rows2 = cur.fetchone()
		endtime = time.time()
		duration = endtime - starttime
		colors = ['red','yellow','green','black','purple','gold','orange','blue']
		return render_template('googlechart.html', ci=rows, ci1=rows1, ci2=rows2,  time=duration)


@app.route('/pie')
def pie():
		starttime = time.time()
		con = sql.connect("db.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		# cur.execute("select count(*),locationSource from earthquakes where mag >="+ mag +" group by locationSource limit 0,8")
		cur.execute("select count(*) from earthquakes where mag BETWEEN '0.0' and '2.0'")
		rows = cur.fetchone()
		cur.execute("select count(*) from earthquakes where mag BETWEEN '2.1' and '4.0'")
		rows1 = cur.fetchone()
		cur.execute("select count(*) from earthquakes where mag > '4.0'")
		rows2 = cur.fetchone()
		endtime = time.time()
		duration = endtime - starttime
		colors = ['red','yellow','green','black','purple','gold','orange','blue']
		return render_template('gpiechart.html', ci=rows, ci1=rows1, ci2=rows2,  time=duration)

@app.route('/list_lat')
def list_lat():
		con = sql.connect("db.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		# cur.execute("select count(*),locationSource from earthquakes where mag >="+ mag +" group by locationSource limit 0,8")
		cur.execute("select latitude,longitude from earthquakes where latitude BETWEEN '-100' and '100' and longitude BETWEEN '-100' and '100'")
		rows = cur.fetchall()
		return render_template('gscatter.html', ci=rows)

				

if __name__ == '__main__':
  app.run(debug=True)
