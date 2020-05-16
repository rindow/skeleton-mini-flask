import os
config = {
    'package_manager':{
        'packages': [
            'rindow.bridge.flask',
            'acme.greeting',
        ],
    },
    'container': {
        'components': {
            'flask.Flask': {
                'factory_args': {
                    'params': { 
                        'import_name': 'flaskr',
                        'static_folder': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static'),
                    },
                }
            }
        }
    },
    'mvc': {
        'config':{
            'DATABASE':os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flaskr.db'),
            'DEBUG':True,
            'SECRET_KEY':'development key',
            'USERNAME':'admin',
            'PASSWORD':'default'
        },
    },
}