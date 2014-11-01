# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

from google.appengine.ext import ndb

class Contact(ndb.Model):
	'''
	This class holds the information for each contact
	that will be put into the datastore. It stores
	the first name, last name, address, and phone
	number of a contact as a string.
	'''
	firstName = ndb.StringProperty(required=True)
	lastName = ndb.StringProperty(required=True)
	address = ndb.StringProperty(required=True)
	phoneNum = ndb.StringProperty(required=True)

