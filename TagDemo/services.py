import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from datetime import datetime

from TagDemo import tagdemo, db, models
 
@tagdemo.route('/')
def default():
	return "{OK}"

@tagdemo.route('/savepoint', methods = ['GET', 'POST'])
def savepoint():
        pointRequest = request.get_json(force=True)

	tagId = pointRequest["tagId"]

	if tagId is None:
		return "{\"Error\":\"No TagId Specified\"}"

	try:
		if pointRequest["lastUpdate"] is not None:
			g.lastUpdate = datetime.strptime(pointRequest["lastUpdate"], '%Y-%m-%dT%H:%M:%S.%fZ')
		else:
			g.lastUpdate = datetime.now()

		g.tag = models.Tag.query.filter(models.Tag.tagId==tagId).one() # g.-global namespace
		g.tag.lastUpdate = g.lastUpdate
		db.session.commit()
		return "{\"Success\":\"Updated tagId: "+g.tag.tagId+"\"}"
	except MultipleResultsFound, e:
		return "{\"Error\":\"DB Corruption - multiple TagId Records\"}"
	except NoResultFound, e:
		g.tag = models.Tag(tagId=pointRequest["tagId"], lastUpdate=g.lastUpdate)
		db.session.add(g.tag)
		db.session.commit()
		return "{\"Success\":\"Added tagId: "+g.tag.tagId+"\"}"	
				

 	return "{\"status\":\"OK\"}"
