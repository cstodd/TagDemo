from TagDemo import db

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tagId = db.Column(db.String(64),index=True, unique=True)
	lastUpdate = db.Column(db.DateTime(),index=True)
	points = db.relationship('Point', backref='parentTag', lazy='dynamic')

	def __repr__(self):
		return '<tagId %r>' % (self.tagId)

class Point(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tagIdNum = db.Column(db.Integer, db.ForeignKey('tag.id'))
	tagId = db.Column(db.String(64), index=True)
	sendTime = db.Column(db.DateTime(), index=True)
	recvTime = db.Column(db.DateTime(), index=True)
	status = db.Column(db.String(16))
	lat = db.Column(db.Float())
	lon = db.Column(db.Float())
	results = db.Column(db.String(256))

	def ___repr__(self):
		return '<results %r>' % (self.results) 
