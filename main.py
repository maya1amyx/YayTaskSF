#webapp2 allows the pages to be opened in the browser. Jinja lets us use html
import webapp2, jinja2, os
from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__), 'templates') #telling where templates are
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory)) #creating jinja objects

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html') #specify which HTML file to serve
        self.response.out.write(template.render())
        #sends the variables to the html as a parameter

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('AboutPage.html') #specify which HTML file to serve
        self.response.out.write(template.render())
        #sends the variables to the html as a parameter
class FindJobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('FindJobs.html')
        self.response.out.write(template.render())

class JobPostHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('JobPosting.html')
        self.response.out.write(template.render())

class HelpPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('HelpPage.html')
        self.response.out.write(template.render())
class PrivacyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('PrivacyPage.html')
        self.response.out.write(template.render())
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('loginpage.html')
        self.response.out.write(template.render())
class FindJobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('FindJobs.html')
        self.response.out.write(template.render())
class MoreInfoHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('morejobinfo.html')
        self.response.out.write(template.render())
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('SignUp.html')
        self.response.out.write(template.render())


class JobPostConfirmHandler(webapp2.RequestHandler):
    def post(self):
        title = self.request.get('jtitle')
        disc = self.request.get('jdisc')
        wage = self.request.get('jwage')
        hours = self.request.get('jhours')

        #User input is the name of the variable from our aout html file
        template = jinja_environment.get_template('JobPostConfirm.html')
        self.response.out.write(template.render(title=title, disc=disc, wage=wage, hours=hours))



#########################################################################
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/About', AboutHandler),
    ('/FindJobs', FindJobsHandler),
    ('/PostJobs', JobPostHandler),
    ('/Help', HelpPageHandler),
    ('/Privacy', PrivacyHandler),
    ('/Login', LoginHandler),
    ('/FindJobs', FindJobsHandler),
    ('/MoreInfo', MoreInfoHandler),
    ('/SignUp', SignUpHandler),
    ('/JobPostConfirm', JobPostConfirmHandler)

], debug=True)
