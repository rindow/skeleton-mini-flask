"""config auth"""
from flask_login import LoginManager
from myapp.model.auth import user_loader as user_loader_impl

login = LoginManager()

def init_app(app):
    """init auth"""
    login.login_view = 'auth.login'
    login.init_app(app)
    # pylint: disable=unused-variable
    @login.user_loader
    def user_loader(user_id):
        return user_loader_impl(user_id)
