import webapp2
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import db_defs

class editContactHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		contact_key = ndb.Key(urlsafe=self.request.get('key'))
		contact = contact_key.get()
		#If the user chose to delete the image, set the img property to 'None',
		#otherwise, get the key of the new image and assign it to the img property.
		if self.request.get('image-action') == 'delete':
			contact.img = None
		elif self.request.get('image-action') == 'change':
			upload_files = self.get_uploads('contactImg')
			if upload_files != []:
				blob_info = upload_files[0]
				contact.img = blob_info.key()

		#If the user chose to enter a new value for firstName, lastName, address, or
		#phoneNum, get the value of it from the submitted form data, and assign that
		#new value to the contact object
		if self.request.get('firstname-action') == 'change':
			contact.firstName = self.request.get('newFirstName')
		elif self.request.get('firstname-action') == 'none':
			pass	

		if self.request.get('lastname-action') == 'change':
			contact.lastName = self.request.get('newLastName')
		elif self.request.get('lastname-action') == 'none':
			pass	

		if self.request.get('addressline1-action') == 'change':
			contact.addressLine1 = self.request.get('newAddressLine1')
		elif self.request.get('address-action') == 'none':
			pass	

		if self.request.get('addressline2-action') == 'change':
			contact.addressLine2 = self.request.get('newAddressLine2')
		elif self.request.get('address-action') == 'none':
			pass

		if self.request.get('phone-action') == 'change':
			contact.phoneNum = self.request.get('newPhone')
		elif self.request.get('phone-action') == 'none':
			pass	

		if self.request.get('zip-action') == 'change':
			contact.zipcode = self.request.get('newZip')
		elif self.request.get('zip-action') == 'none':
			pass

		if self.request.get('state-action') == 'change':
			contact.state = self.request.get('state')
		elif self.request.get('state-action') == 'none':
			pass

		if self.request.get('city-action') == 'change':
			contact.city = self.request.get('newCity')
		elif self.request.get('city-action') == 'none':
			pass

		if self.request.get('email-action') == 'change':
			contact.email = self.request.get('newEmail')
		elif self.request.get('email-action') == 'none':
			pass	

		contact.put()
		self.redirect('/edit?key=' + contact_key.urlsafe() + '&type=contact')
