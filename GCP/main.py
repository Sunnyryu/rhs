import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.write('hello from app engine!');

app = webapp2.WSGIApplication([
    ('/', HelloWorld),
])
