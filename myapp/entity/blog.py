from myapp.config.database import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DATETIME, default=datetime.now, nullable=False)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    author = db.relationship('User')

    def __repr__(self):
        return '<Post %r>' % self.title
