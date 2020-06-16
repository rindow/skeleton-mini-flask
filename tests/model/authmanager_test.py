from myapp import config
from myapp.model.auth import UserManager


def test_save_get(app,client):
    usermgr = UserManager()
    with app.app_context():
        user = usermgr.authenticate(
            username='user@demo.com',
            password='password',
        )
        assert user.id == 1
        assert user.username == 'user@demo.com'
    with app.app_context():
        user = usermgr.authenticate(
            username='user@demo.com',
            password='fail',
        )
        assert user is None
    with app.app_context():
        success = usermgr.register(username='user2@demo.com',password='password')
        assert success is True
    with app.app_context():
        success = usermgr.register(username='user2@demo.com',password='password')
        assert success is False
    with app.app_context():
        user = usermgr.authenticate(
            username='user2@demo.com',
            password='password',
        )
        success = usermgr.delete(user)
        assert success is True
    with app.app_context():
        success = usermgr.delete(user)
        assert success is False
