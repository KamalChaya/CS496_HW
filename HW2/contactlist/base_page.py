import os 
import jinja2
import webapp2

JINJA_ENV = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
	)

class homepage(webapp2.RequestHandler):
	template_vars = {}

	def get(self):
		template = JINJA_ENV.get_template('base_page.html')
		self.response.write(template.render())

	def post(self):
		self.template_vars['form_content'] = {}
		template = JINJA_ENV.get_template('base_page.html')
		for i in self.request.arguments():
			self.template_vars['form_content'][i] = self.request.get(i)
		self.response.write(template.render(self.template_vars))