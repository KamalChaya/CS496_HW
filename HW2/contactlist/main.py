import webapp2

app = webapp2.WSGIApplication([
 	('/', 'base_page.homepage'),
 	], debug =True)