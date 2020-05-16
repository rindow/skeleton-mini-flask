import os
from acme.greeting.controller.main import MainHandler
from acme.greeting.controller.main import Guestbook
config = {
    'container': {
        'components': {
            'flask.Flask': {
                'factory_args': {
                    'params': {
                        'template_folder': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'views'),
                    },
                }
            }
        }
    },
    'mvc': {
        'router':{
            'routings':[
                ('/', MainHandler, 'home'),
                ('/sign', Guestbook, 'sign'),
            ]
        }
    },
    'debug': __name__,
}