import os
import pytest
from werkzeug.security import generate_password_hash, check_password_hash
from myapp import create_app
from myapp import config

@pytest.fixture
def app():
    os.environ['FLASK_ENV'] = 'testing'
    _app = create_app()
    _app.config['WTF_CSRF_ENABLED'] = False
    _app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    return _app

@pytest.fixture
def client(app):
    from myapp.entity.auth import User
    config.database.db.drop_all()
    config.database.db.create_all()
    with app.app_context():
        pw_hash = generate_password_hash('password')
        config.database.db.session.add(
            User(username='user@demo.com',password=pw_hash))
        config.database.db.session.commit()
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
