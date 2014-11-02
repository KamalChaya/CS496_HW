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

class editFormHandler(base_page.baseHandler):
	"""
	A handler class for when the user wants to edit a contact. All requests which 
	go to a url of "/edit" will invoke the functions in this class, which enable
	the user to add contacts and put them into the datastore. 
	"""
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {} 
		self.template_values['edit_url'] = blobstore.create_upload_url( '/edit/contact' )
	
	def get(self):
		"""
		A function to handle any HTTP GET requests
		"""
		if self.request.get('type') == 'contact':
			contact_key = ndb.Key(urlsafe=self.request.get('key'))
			contact = contact_key.get()
			if contact.img:
				self.template_values['img_url'] = images.get_serving_url(contact.img, crop=True, size=64)
			self.template_values['contact'] = contact 	
		self.render('edit_form.html',self.template_values)
		