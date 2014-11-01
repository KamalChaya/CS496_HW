# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class editHandler(base_page.baseHandler):
	'''
	A handler class for when the user wants to edit a contact. All requests which 
	go to a url of "/edit" will invoke the functions in this class, which enable
	the user to add contacts and put them into the datastore. 
	'''
	def get(self):
		'''
		A function to handle any HTTP GET requests
		'''
		#Render the edit.html page
		self.render('edit.html')