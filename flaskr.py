import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import psycopg2

def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(host="localhost", port="5432",dbname="textmining", user="postgres",assword="123456")
    cur = conn.cursor()
    cur.execute("select text from documents where document=%s" % (pmid))
    return rv

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Index'
	

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__=='__main__':
    app.run()
