from flask import Flask, Response, request, render_template, redirect, url_for, session
from flaskext.mysql import MySQL
import datetime, os, shutil
from twilio.rest import *

app = Flask(__name__)

# Your Account SID from twilio.com/console
#account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
#auth_token = "your_auth_token"

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#        to="+18578005581",
#        from_="+16179552483",
#       body="Hello from Python!")

#print(message.sid)
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()


