from flask import Flask, request, redirect, session 
from twilio.rest import TwilioRestClient 
import twilio.twiml 
import time

app = Flask(__name__) 

@app.route("/") def smsEcho(): 
	client = TwilioRestClient(SID,TOKEN) 
	return "HelloWorld" 
	if __name__ == "__main__": 
		app.run(debug=True)