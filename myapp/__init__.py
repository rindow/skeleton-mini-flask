"""bootstrap app"""
# pylint: disable=import-outside-toplevel

def create_app():
    """build app"""
    from pyrindow.container.module_manager import ModuleManager
    module_manager = ModuleManager(myapp.config.pyrindow.config)
    _app = module_manager.get_service_locator().get('flask.Flask')
    # from flask import Flask
    # _app = Flask(__name__)
    # _app.secret_key = 'secret_key'
    # _app.config['DEBUG'] = True

    # from myapp.config import database, controller, auth, wtforms
    # database.init_app(_app)
    # controller.init_app(_app)
    # auth.init_app(_app)
    # wtforms.init_app(_app)

    return _app
