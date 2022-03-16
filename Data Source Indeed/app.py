from markupsafe import escape
from flask import Flask, abort,redirect,url_for
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/indeed/')
def indeed():
    return '<h3>This is the redirected page</h3>'


@app.route('/oauth/')
def oauth():
    clientid = "a2ac62d449c93b2298e1ce773bca17d6a83f1bd224ef4aa8dc102290b4116f1f"
    redirecturi = "http://localhost:5000/indeed"
    responsetype = "code"
    state = "employer1234"
    scope = "email+offline_access+employer_access"
    baseurl = "https://secure.indeed.com/oauth/v2/authorize"
    url = "{}?client_id={}&redirect_uri={}&response_type={}".format(baseurl,clientid,redirecturi,responsetype,state,scope)
    return redirect(url)
