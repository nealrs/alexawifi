import requests
import os
from flask import Flask, request, session, redirect, render_template, Response, make_response, jsonify
from flask_ask import (
    Ask,
    request as ask_request,
    session as ask_session,
    context as ask_context,
    version, question, statement, audio, current_stream
)

ssid = str(os.environ['SSID'])
password = str(os.environ['PASSWORD'])

app = Flask(__name__)
ask = Ask(app, '/')
@app.route("/", methods=["GET", "POST"])
def home():
    return "Hi there.", 200
    #return ssid + " "+ password + " " + (' '.join(ssid)) + " " + (' '.join(password)), 200
@ask.launch
@ask.default_intent
@ask.intent('WifiIntent')
def launch():
    print "wifi skill launch"
    speech = "The wireless network name is "+(' '.join(ssid))+", and the password is "+(' '.join(password))+"."
    #return statement(speech) # in case you don't want to return the card
    card_title = "Get on the WiFi"
    card_text = "Network: "+ssid+"\nPassword: "+ password
    return statement(speech).simple_card(title=card_title, content=card_text)

if __name__ == "__main__":
	app.run(debug=os.environ['DEBUG'])
