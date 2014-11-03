# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

import webapp2
import base_page
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
import db_defs

class viewFilterHandler(base_page.baseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, state):
		"""
		Queries the data store to get all the contact objects, and then renders them to the page. 
		This function calls the render function from the base class.
		"""
		#Ancestor key used so that we can make a conistent query across the entity group
		#otherwise, theres a chance not all the contact objects would be returned
		ancestorKey = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

		#Returns a list of contacts (with all of their attributes) and puts it in the template values dictionary under the key name 'contacts'
		self.template_values['contacts'] = [{'firstName':x.firstName, 'lastName':x.lastName, 'addressLine1':x.addressLine1, 'addressLine2':x.addressLine2, 'phoneNum':x.phoneNum, 'state':x.state, 'city':x.city, 'zipcode':x.zipcode, 'email':x.email, 'img_url':images.get_serving_url(x.img, crop=True, size=64), 'key':x.key.urlsafe()} for x in db_defs.Contact.query(ancestor=ancestorKey).fetch() if x.state == state]	
		self.template_values['filterstate'] = [{'state':state}]
		base_page.baseHandler.render(self, page, self.template_values)

	def post(self):
		state = self.request.get('state')
		self.render('viewfiltered.html', state)