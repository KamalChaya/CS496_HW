import webapp2
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
import add

class AddContactFile(blobstore_handlers.BlobstoreUploadHandler):
	"""
	This class is used to store the image uploaded by the user
	"""
	def post(self):
		#
		upload_files = self.get_uploads('contactImg')
		if upload_files != []:
			blob_info = upload_files[0]
			