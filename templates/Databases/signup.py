#!/usr/bin/env python
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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('index.html') #specify which HTML file to serve
        self.response.out.write(template.render())
        #sends the variables to the html as a parameter

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('Aboutpage.html') #specify which HTML file to serve
        self.response.out.write(template.render())
        #sends the variables to the html as a parameter
class FindJobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('FindJobs.html')
        self.response.out.write(template.render())

class JobPostingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('JobPosting.html')
        self.response.out.write(template.render())

class HelpPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('HelpPage.html')
        self.response.out.write(template.render())

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('SignUp.html')
        self.response.out.write(template.render())

class LogInHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_enviornment.get_template('loginpage.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/About', AboutHandler),
    ('/FindJobs', FindJobsHandler),
    ('/PostJobs', JobPostingHandler),
    ('/Help', HelpPageHandler),
    ('/SignUp', SignUpHandler),
    ('/LogIn', LogInHandler),

], debug=True)
