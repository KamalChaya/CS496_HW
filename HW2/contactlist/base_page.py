# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor 

import os 
import jinja2
import webapp2
import db_defs
from google.appengine.ext import ndb
from google.appengine.api import images

JINJA_ENV = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
	)

class baseHandler(webapp2.RequestHandler):
	@webapp2.cached_property
	def jinja2(self):
		return jinja2.Environment(
			loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
			extensions = ['jinja2.ext.autoescape'],
			autoescape = True	
			) 

	def render(self, template, template_vars={}):
		template = self.jinja2.get_template(template)
		self.response.write(template.render(template_vars))

class mainHandler(baseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page):
		"""
		Queries the data store to get all the contact objects, and then renders them to the page. 
		This function calls the render function from the base class.
		"""
		#Ancestor key used so that we can make a conistent query across the entity group
		#otherwise, theres a chance not all the contact objects would be returned
		ancestorKey = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

		#Returns a list of contacts (with all of their attributes) and puts it in the template values dictionary under the key name 'contacts'
		self.template_values['contacts'] = [{'firstName':x.firstName, 'lastName':x.lastName, 'address':x.address, 'phoneNum':x.phoneNum, 'img_url':images.get_serving_url(x.img, crop=True, size=64), 'key':x.key.urlsafe()} for x in db_defs.Contact.query(ancestor=ancestorKey).fetch()]	
		baseHandler.render(self, page, self.template_values)


	def get(self):
		"""
		A function to handle any HTTP GET requests
		"""
		self.render('main.html')
