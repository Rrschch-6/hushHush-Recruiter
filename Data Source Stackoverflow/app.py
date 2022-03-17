from urllib import response
from markupsafe import escape
from flask import Flask, abort,redirect,url_for,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Nissy Sasidharan!"

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/stack/')
def stack():
    code = ""
    code = request.args.get('code')
    if code != "":
        response_text = getaccesstoken(code)
        return   '<h3>This is the redirected page with code</h3><p>'+ response_text +'</p>'
    else:
        return '<h3>This is the redirected page without accesstoken</h3>'
    
@app.route('/client/')
def client():
    clientid = "23005"
    scope = "no_expiry"
    redirecturi = "http://localhost:5000/stack"
    baseurl = "https://stackoverflow.com/oauth"
    url = "{}?client_id={}&scope={}&redirect_uri={}".format(baseurl,clientid,scope,redirecturi)
    return redirect(url)


def getaccesstoken(code):
     baseurl = "https://stackoverflow.com/oauth/access_token/json"
     clientid = "23005"
     clientsecret = "ZxGRfJBrhR7BnCadkeAFxw(("
     redirecturi = "http://localhost:5000/stack"
     payload = "client_id={}&client_secret={}&code={}&redirect_uri={}".format(clientid,clientsecret,code,redirecturi)
     headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
     response = requests.request("POST", baseurl, headers=headers, data=payload)
     return response.text



