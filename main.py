#webapp2 allows the pages to be opened in the browser. Jinja lets us use html
import webapp2, jinja2, os
from google.appengine.ext import ndb
from google.appengine.api import users

template_directory = os.path.join(os.path.dirname(__file__), 'templates') #telling where templates are
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory)) #creating jinja objects

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html') #specify which HTML file to serve
        self.response.out.write(template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('AboutPage.html') #specify which HTML file to serve
        self.response.out.write(template.render())
        #sends the variables to the html as a parameter

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


        currentUser = users.get_current_user()

        if currentUser:  #if current user exists
            nickname = currentUser.nickname()  #email address before

            url = users.create_logout_url('/')
            url_text = "logout"

            self.redirect('/PostJobs')

        else:
            url = users.create_login_url('/')
            url_text = "login"

        template = jinja_environment.get_template('loginpage.html')
        self.response.out.write(template.render(url = url,
        url_text = url_text))


class SignUpHandler(webapp2.RequestHandler):
     def get(self):
         template = jinja_environment.get_template('SignUp.html')
         self.response.out.write(template.render())

class Job(ndb.Model):
    title = ndb.StringProperty()
    type = ndb.StringProperty()
    disc = ndb.StringProperty()
    wage = ndb.StringProperty()
    hours = ndb.StringProperty()




# [Key('Job', 4644337115725824), Key('Job', 4785074604081152), Key('Job', 5066549580791808), Key('Job', 5348024557502464), Key('Job', 5629499534213120), Key('Job', 5770237022568448), Key('Job', 5910974510923776), Key('Job', 6192449487634432), Key('Job', 6473924464345088)] []

class JobPostHandler(webapp2.RequestHandler):
    def get(self):
        #title = self.request.get('jtitle')

        template = jinja_environment.get_template('JobPosting.html')
        self.response.out.write(template.render())


class JobPostConfirmHandler(webapp2.RequestHandler):


    # Creates a category for a job and returns a unique key
    def create_job_post(self, title, type, disc, wage, hours):
        post = Job(title=title, type=type, disc=disc, wage= wage, hours=hours)
        post = post.put()
    # recieves job info from JobPost page and passes them to the render parameters
    def get(self):
        title = self.request.get('title')
        type = self.request.get('type')
        disc = self.request.get('disc')
        wage = self.request.get('wage')
        hours = self.request.get('hours')

        #User input is the name of the variable from our aout html file

        #https://sites.google.com/site/usfcomputerscience/html
        template = jinja_environment.get_template('JobPostConfirm.html')
        self.response.out.write(template.render(title=title, type=type, disc=disc, wage=wage, hours=hours))

        self.create_job_post(title, type, disc, wage, hours)

class FindJobsHandler(webapp2.RequestHandler):
    def check_for_empty(self):
        query = Job.query().fetch()

        for item in query:
            if item.title == "u" or item.title=="":
                item.delete()
            else:
                continue

    def get(self):

        list_of_jobs = []
        #jobs = []

        query = Job.query().fetch(20,keys_only=True)

        for Key in query:
            one_job = Key.get()
            list_of_jobs.append(one_job)

        template = jinja_environment.get_template('FindJobs.html')
        self.response.out.write(template.render(query=query, list_of_jobs=list_of_jobs,))
class MoreInfoHandler(webapp2.RequestHandler):
    def get(self):
        # post = post_key.get()
        # return post

        template = jinja_environment.get_template('morejobinfo.html')
        self.response.out.write(template.render())



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
    # ('/SignUp', SignUpHandler),
    ('/JobPostConfirm', JobPostConfirmHandler)

], debug=True)
