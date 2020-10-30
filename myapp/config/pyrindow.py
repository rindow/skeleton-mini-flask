"""config auth"""
config = {
    'module_manager': {
        'modules': {
            'pyrindow.bridge.flask': True,
        },
    },
    'flask': {
        'secret_key': 'test secret key',
        #'config': {
        #    'some_option': 'some_value',
        #},
        'jinja_options': {
        #    'bytecode_cache': 'jinja2.FileSystemBytecodeCache',
        },
        'flask_caching': {
            'enable': True,
        },
        'flask_login': {
            'enable': True,
            'login_view':'auth.login'
            'user_loader':'myapp.model.auth.user_loader'
        },
        'flask_wtf.csrf': {
            'enable': True,
        },
        'flask_sqlalchemy': {
            'enable': True,
            'database_uri': 'sqlite:///:memory:',
            'save_settings_to': 'myapp.config.database.db',
        },
    },
}
