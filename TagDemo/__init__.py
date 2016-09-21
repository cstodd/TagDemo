import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash

from flask_sqlalchemy import SQLAlchemy

tagdemo = Flask(__name__)
tagdemo.config.from_object('config')

db = SQLAlchemy(tagdemo)

tagdemo.config.from_envvar('TAGDEMO_SETTINGS', silent=True)

from TagDemo import services, models

def connect_db():
	conn = sqlite3.connect(app.config['DATABASE'])
	conn.row_factory = sqlite3.Row
	return conn


