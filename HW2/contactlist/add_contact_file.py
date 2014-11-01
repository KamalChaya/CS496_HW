import webapp2
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import add

class AddContactFile(blobstore_handlers.BlobstoreUploadHandler):
	"""
	This class is used to store the image uploaded by the user
	"""
	def post(self):
		#get the uploaded file from the form
		upload_files = self.get_uploads('contactImg')
		if upload_files != []:
			blob_info = upload_files[0]
			add.addHandler(self.request, self.response).post(img_key=blob_info.key())
		else:
			add.addHandler(self.request, self.response).post()