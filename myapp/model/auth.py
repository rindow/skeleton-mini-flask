"""authenticate"""
from werkzeug.security import generate_password_hash, check_password_hash
from myapp.config.database import db, exc
from myapp.entity.auth import User
from myapp.model.interface import AbstractUserManager

def user_loader(user_id):
    """user_loader for flask_login"""
    user = User.query.filter_by(id=user_id).first()
    return user

class UserManager(AbstractUserManager):
    """user manager"""
    def authenticate(self, username: str, password: str):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return None
        if not check_password_hash(user.password, password):
            return None
        return user

    def register(self, username: str, password: str) -> bool:
        pw_hash = generate_password_hash(password)
        user = User(username=username, password=pw_hash)
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            return False
        return True

    def delete(self, user) -> bool:
        user = User.query.filter_by(id=user.id).first()
        if user is None:
            return False
        db.session.delete(user)
        db.session.commit()
        return True

userManager = UserManager()
