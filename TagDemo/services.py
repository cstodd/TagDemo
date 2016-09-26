import os
import sqlite3
import sys
import traceback
import json
from array import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash, Response

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from datetime import datetime

from TagDemo import tagdemo, db, models
 
@tagdemo.route('/')
def default():
	return "{OK}"

@tagdemo.route('/getallpoints', methods = ['GET', 'POST'])
def getallpoints():
	points = models.Point.query.all()

	fullPayload = []  

	for point in points:
		resultObjJSON = json.loads(point.results)
		fullPayload.append(resultObjJSON)
		print("Point:" + point.results)

	result = {"fullPayload" : fullPayload}

	print("Points:" + json.dumps(result))
	return Response(json.dumps(result), mimetype='application/json') 

@tagdemo.route('/savepoint', methods = ['GET', 'POST'])
def savepoint():
        pointRequest = request.get_json(force=True)
	requestText = request.data

	tagId = pointRequest["tagId"]

	if tagId is None:
		return "{\"Error\":\"No TagId Specified\"}"

	try:
		print "Saving tag info..."
		if pointRequest["lastUpdate"] is not None:
			g.lastUpdate = datetime.strptime(pointRequest["lastUpdate"], '%Y-%m-%dT%H:%M:%S.%fZ')
		else:
			g.lastUpdate = datetime.now()

		g.tag = models.Tag.query.filter(models.Tag.tagId==tagId).one() # g.-global namespace
		g.tag.lastUpdate = g.lastUpdate
		print "Updating tag..."
		db.session.commit()
	except MultipleResultsFound, e:
		return "{\"Error\":\"DB Corruption - multiple TagId Records\"}"
	except NoResultFound, e:
		print "New tag..."
		g.tag = models.Tag(tagId=pointRequest["tagId"], lastUpdate=g.lastUpdate)
		db.session.add(g.tag)
		db.session.commit()
	except:
		return "{\"Error\":\"General error with point metadata\"}"
		
		
	try:
		print "Saving point..."
		if pointRequest["results"] is not None:
			result = pointRequest["results"][0]
			lat = result["geometry"]["location"]["lat"]
			lng = result["geometry"]["location"]["lng"]

			point = models.Point(tagId=g.tag.tagId, tagIdNum=g.tag.id, parentTag = g.tag)
			point.sendTime = g.tag.lastUpdate
			point.recvTime = datetime.now()
			point.status = pointRequest["status"]
			point.lat = lat
			point.lon = lng
			point.results = requestText  
			db.session.add(point)
			db.session.commit()
		else:
			return( "{\"Error:\":\"No point result\"}" )

	except NoResultFound, e:
		e = sys.exc_info()[0]
   		traceback.print_exc()
		return( "{\"Error:\":\"%s\"}" % e )
	

 	return "{\"status\":\"OK\"}"
