"""blog models"""
from myapp.config.database import db
from myapp.entity.blog import Post

class PostManager():
    # pylint: disable=no-self-use
    # pylint: disable=redefined-builtin
    # pylint: disable=invalid-name
    """post manager"""
    def find_all(self):
        """find all entity"""
        return Post.query.all()

    def find_by_id(self, id):
        """find entity by id"""
        return Post.query.filter_by(id=id).first()

    #def save(self, entity):
    #    """save post"""
    #    if entity.get('id'):
    #        post = self.find_by_id(entity['id'])
    #        post.title = entity['title']
    #        post.body = entity['body']
    #    else:
    #        post = Post(**entity)
    #        db.session.add(post)
    #    db.session.commit()
    def factory(self, **data):
        """new entity"""
        return Post(**data)


    def save(self, post):
        """save post"""
        if not post.id:
            db.session.add(post)
        db.session.commit()


    def delete_by_id(self, id):
        """delete entity by id"""
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()

postManager = PostManager()
