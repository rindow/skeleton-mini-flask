import os
from acme.greeting.controller.main import Show
config = {
    'container': {
        'components': {
            'flask.Flask': {
                'factory_args': {
                    'params': { 
                        'static_folder': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static'),
                        'template_folder': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates'),
                    },
                }
            }
        }
    },
    'mvc': {
        'router':{
            'routings':[
                ('/', Show, 'show_entries'),
                ('/add', Show, 'add_entry'),
                ('/login', Show, 'login'),
                ('/logout', Show, 'logout'),
            ]
        }
    },
    'debug': __name__,
}