# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class editHandler(base_page.baseHandler):
	"""
	A handler class for when the user wants to edit a contact. All requests which 
	go to a url of "/edit" will invoke the functions in this class, which enable
	the user to add contacts and put them into the datastore. 
	"""
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {} 
		self.template_values['edit_url'] = blobstore.create_upload_url( '/edit/contact' )

	def render(self, page):
		"""
		Queries the data store to get all the contact objects, and then renders them to the page. 
		This function calls the render function from the base class.
		"""
		#Ancestor key
		ancestorKey = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

		#Returns a list of contacts and puts it in the template values dictionary under the key name 'contacts'
		self.template_values['contacts'] = [{'firstName':x.firstName, 'key':x.key.urlsafe()} for x in db_defs.Contact.query(ancestor=ancestorKey).fetch()]	
		base_page.baseHandler.render(self, page, self.template_values)
			
	
	def get(self):
		"""
		A function to handle any HTTP GET requests
		"""
		if self.request.get('type') == 'contact':
			contact_key = ndb.Key(urlsafe=self.request.get('key'))
			contact = contact_key.get()
			if contact.img:
				self.template_values['img_url'] = images.get_serving_url(contact.img, crop=True, size=64)
		