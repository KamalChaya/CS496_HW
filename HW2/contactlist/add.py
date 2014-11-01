# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class addHandler(base_page.baseHandler):
	"""
	A handler class for when the user wants to add a contact. All requests which 
	go to a url of "/add" will invoke the functions in this class, which enable
	the user to add contacts and put them into the datastore. 
	"""
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {} 

	def render(self, page):
		"""
		Queries the data store to get all the contact objects, and then renders them to the page. 
		This function calls the render function from the base class.
		"""
		#Ancestor key
		ancestorKey = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

		#Returns a list of channels and puts it in the template values dictionary under the key name 'contacts'
		self.template_values['contacts'] = [{'firstName':x.firstName, 'key':x.key.urlsafe()} for x in db_defs.Contact.query(ancestor=ancestorKey).fetch()]	
		base_page.baseHandler.render(self, page, self.template_values)

	def get(self):
		"""
		A function to handle any HTTP GET requests. Renders the add.html page by
		calling the render function in this class. 
		"""
		#Render the add.html page 
		self.render('add.html')

	def post(self):
		"""
		A function to handle any HTTP POST requests.
		"""
		action = self.request.get('action')
		if action == 'add_contact':
			#Create a key 
			k = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

			#Set the contacts parent key. The only way to guarantee that we can
			#get the object from the datastore after we store it is to make it so
			#that all these objects are under the same parent key.
			contact = db_defs.Contact(parent = k)

			#set all the attributes of the channel to the values inputted by 
			#the user into the form
			contact.firstName = self.request.get('firstname')
			contact.lastName = self.request.get('lastname')
			contact.address = self.request.get('address')
			contact.phoneNum = self.request.get('phone')

			#put contact in data store
			contact.put()

			#Set the template values to a message indicating that the contact was added to the datastore
			self.template_values['message'] = 'Added contact ' + contact.firstName + ' to the database.'
		else:
			self.template_values['message'] = 'Unknown action attempted: ' + action
		self.render('add.html') 

