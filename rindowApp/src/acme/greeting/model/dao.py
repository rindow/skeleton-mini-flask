from google.appengine.ext import ndb
from acme.greeting.entity.greeting import Greeting
from acme.greeting.entity.greeting import Author

class GreetingManager(object):
    def list(self,guestbook_name):
        greetings_query = Greeting.query(
                ancestor=self._guestbook_key(guestbook_name)
            ).order(-Greeting.date)
        greetings = greetings_query.fetch(10)
        return greetings
    def add(self,guestbook_name,content,nickname,email):
        greeting = Greeting(parent=self._guestbook_key(guestbook_name))
        if nickname or email:
            greeting.author = Author(
                    nickname=nickname,
                    email=email)
        greeting.content = content
        greeting.put()
    def _guestbook_key(self,guestbook_name):
        return ndb.Key('Guestbook', guestbook_name)
