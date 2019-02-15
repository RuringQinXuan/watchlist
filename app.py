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

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
	

@app.route('/hello')
def hello_world():
    return 'Hello, World!'



@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/home/<name>')
def home(name):
    return 'Welcome to %s!' % name


@app.route('/test')
def test_url_for():
    print(url_for('hello_world',name='zyf'))
    print(url_for('home',name='zyf'))
    return 'test page'

if __name__=='__main__':
    app.run()
