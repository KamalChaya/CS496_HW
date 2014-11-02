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
		if self.request.get('image-action') == 'delete':
			contact.img = None
		elif self.request.get('image-action') == 'change':
			upload_files = self.get_uploads('contactImg')
			if upload_files != []:
				blob_info = upload_files[0]
				contact.img = blob_info.key()
		contact.put()
		self.redirect('/edit?key=' + contact_key.urlsafe() + '&type=contact')
