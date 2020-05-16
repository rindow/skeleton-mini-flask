from google.appengine.ext import ndb

class Author(ndb.Model):
    nickname = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)

class Greeting(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
