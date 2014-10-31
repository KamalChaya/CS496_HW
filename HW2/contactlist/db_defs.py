from google.appengine.ext import ndb

class Contact(ndb.Model):
	firstName = ndb.StringProperty(required=True)
	lastName = ndb.StringProperty(required=True)
	address = ndb.StringProperty(required=True)
	phoneNum = ndb.StringProperty(required=True)

