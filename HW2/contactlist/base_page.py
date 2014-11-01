# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor 

import os 
import jinja2
import webapp2
from google.appengine.ext import ndb

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

class mainHandler(webapp2.RequestHandler):
	template_values = {}


	def get(self):
		template = JINJA_ENV.get_template('main.html')
		self.response.write(template.render())
