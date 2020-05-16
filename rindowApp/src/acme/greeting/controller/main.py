import urllib
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.views import MethodView

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

from acme.greeting.model.dao import GreetingManager
greetingManager = GreetingManager()
#import jinja2,os
#JINJA_ENVIRONMENT = jinja2.Environment(
#    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'..','views')),
#    extensions=['jinja2.ext.autoescape'],
#    autoescape=True)

class BaseHandler(MethodView):
    def dispatch_request(self):
        #self.serviceLocator = self.app.registry.get('serviceLocator')
        #self.greetingManager = self.serviceLocator.get('acme.greeting.greetingManager')
        self.request = request
        return super(BaseHandler,self).dispatch_request()

    def render_response(self, _filename, **context):
        #serviceLocator = self.app.registry.get('serviceLocator')
        #template = serviceLocator.get('acme.greeting.template').get_template(_filename)
        #template = JINJA_ENVIRONMENT.get_template(_filename)
        #self.response.write(template.render(context))
        return render_template(_filename, **context)

    def redirect(self,url):
        return redirect(url)

class MainHandler(BaseHandler):
    def get(self):
        guestbook_name = self.request.form.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        #greetingManager = self.app.registry.get('serviceLocator').get('acme.greeting.greetingManager')
        return self.render_response('index.html',
            greetings = greetingManager.list(guestbook_name),
            #greetings=[],
            guestbook_name = urllib.quote_plus(guestbook_name)
            #guestbook_name='AA'
            )

class Guestbook(BaseHandler):
    def post(self):
        guestbook_name = self.request.form.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        content = self.request.form.get('content')
        nickname = self.request.form.get('nickname',None)
        email = self.request.form.get('email',None)
        #greetingManager = self.app.registry.get('serviceLocator').get('acme.greeting.greetingManager')
        greetingManager.add(guestbook_name,content,nickname,email)
        query_params = {'guestbook_name': guestbook_name}
        return self.redirect('/?' + urllib.urlencode(query_params))
