# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import sys,os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'vendor'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'))
import loader

#import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import gc
def dump_garbage():
    gc.collect()
    result = ''
    i = 0
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:77]+'...'
        result = result + type(x).__name__ + '\n ' + s + '\n'
        i = i + 1
    result = ('GARBAGE OBJECTS: total %d\n' % i) + result
    result = '<pre>' + result + '</pre>'
    return result

#gc.set_debug(gc.DEBUG_LEAK)

from rindow.container.packagemanager import PackageManager
try:
    from config.settings import config
    packageMgr = PackageManager(config)
    app = packageMgr.getServiceLocator().get('flask.Flask')
except Exception, e:
    from rindow.stdlib.debug import MakeWsgiDump
    import traceback
    app = MakeWsgiDump(traceback.format_exc())

app.debug = True
if __name__ == "__main__":
    app.run()