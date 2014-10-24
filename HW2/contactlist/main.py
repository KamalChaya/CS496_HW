#!/usr/bin/env python
# 
# CS 496 HW 2
# Kamal Chaya
# Oregon State University
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import wsgiref.handlers

MAIN_PAGE_HTML  = """
	<!DOCTYPE html>
	<html>
		<body>
			<h1>Welcome to the contact list!</h1>
			<h2>View Contacts: </h2>
			
			<form action="/addcontact">
				<input type="submit" value="Add contact">
			</form>
			
		</body>
	</html>
"""

ADD_CONTACT_HTML = """
	<!DOCTYPE html>
	<html>
		<body>
			<h1>Welcome to the contact list!</h1>
		</body>
	</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)
		
class AddContactHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(ADD_CONTACT_HTML)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/addcontact', AddContactHandler),
], debug=True)
    

