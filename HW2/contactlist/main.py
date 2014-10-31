 # Author: Kamal Chaya
# Oregon State University
# CS 496

import webapp2

config = {'default-group':'base-data'}

app = webapp2.WSGIApplication([
 	('/', 'base_page.mainHandler'),
 	('/add', 'add.addHandler')
 	], debug =True, config=config)