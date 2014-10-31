# Kamal Chaya
# 
#

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class addHandler(base_page.baseHandler):
	def get(self):
		#Render the add.html page 
		self.render('add.html')

	def post(self):
		action = self.request.get('action')
		if action == 'add_contact':
			#Create a key 
			k = ndb.Key(db_defs.Contact, self.app.config.get('default-group'))

			#Set the contacts parent key. We use parent keys so that 
			#the queries
			contact = db_defs.Contact(parent = k)

			#set all the attributes of the channel to the values inputted by 
			#the user into the form
			contact.firstName = self.request.get('firstname')
			contact.lastName = self.request.get('lastname')
			contact.address = self.request.get('address')
			contact.phoneNum = self.request.get('phone')

			#put contact in data store
			contact.put()

			#render the HTML, printing a message saying the contact was added
			self.render('add.html', {'message':'Added ' + contact.firstName + ' to the database.'})
		else:
			self.render('add.html', {'message':'Action ' + action + ' is unknown.'})
