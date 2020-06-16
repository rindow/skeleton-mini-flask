from myapp import config
from myapp.model.blog import PostManager

def test_save_get(app,client):
    postmgr = PostManager()
    with app.app_context():
        post = postmgr.factory(
            author_id=1,
            title='test subject',
            body='content',
        )
        postmgr.save(post)
    with app.app_context():
        posts = postmgr.find_all()
        num = 0
        for post in posts:
            assert post.title=='test subject'
            assert post.body=='content'
            num += 1
        assert num==1
    with app.app_context():
        post = postmgr.find_by_id(1)
        assert post.id == 1
        assert post.title == 'test subject'
        assert post.body == 'content'
    with app.app_context():
        post = postmgr.delete_by_id(1)
    with app.app_context():
        assert postmgr.find_by_id(1) is None

def test_get_no_content(app,client):
    postmgr = PostManager()
    with app.app_context():
        assert postmgr.find_by_id(1) is None
