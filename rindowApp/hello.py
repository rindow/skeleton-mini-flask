import sys,os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'vendor'))
import loader

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

if __name__ == "__main__":
    app.run()