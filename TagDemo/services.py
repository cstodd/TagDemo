import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

from TagDemo import tagdemo 

@tagdemo.route('/')
def default():
	return "{OK}"

@tagdemo.route('/savepoint', methods = ['GET', 'POST'])
def savepoint():
        point = request.get_json(force=True)

	for i in point:
		print i, point[i]

	

 	return "{\"status\":\"OK\"}"
