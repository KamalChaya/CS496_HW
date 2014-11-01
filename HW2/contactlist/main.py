# Author: Kamal Chaya
# Oregon State University
# CS 496
# This code is based on and modified from the python videos uploaded by instructor

import webapp2

config = {'default-group':'base-data'}

app = webapp2.WSGIApplication([
 	('/', 'base_page.mainHandler'),
 	('/add', 'add.addHandler'),
 	('/contactfile/add', 'add_contact_file.AddContactFile'),
 	('/edit', 'edit.editHandler'),
 	], debug =True, config=config)