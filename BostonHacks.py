from flask import Flask, Response, request, render_template, redirect, url_for, session
#from flaskext.mysql import MySQL
#import datetime, os, shutil
from twilio.rest import Client

app = Flask(__name__)


# My number = 16178299091
# secret key = bvRm9fytaLHf54TQkhZ70SifB9wR8VgN
# Your Account SID from twilio.com/console
#account_sid = "AC072910fce1e2bad15bf85051f2e932e5"
# Your Auth Token from twilio.com/console
#auth_token = "81e4aa1d436687b464db9335ff9a3d32"

#client = Client(account_sid, auth_token)


# Your Account Sid and Auth Token from twilio.com/console
api_key_sid = "SKd282f2bee6cf6ca53946cc380e928fcc"
api_key_secret = "bvRm9fytaLHf54TQkhZ70SifB9wR8VgN"
client = Client(api_key_sid, api_key_secret)

#room = client.video.rooms('RMf3f98109f841f26f1c649f5eea51e286').fetch()

room = client.video.rooms.create(unique_name='Room1')

print(room.sid)

Twilio.Video.Connect
'''
message = client.messages.create(
        to="+18572058079",
        from_="+16178299091",
       body="Hello from Python!")

#print(message.sid)


@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/home/<data>', methods=['POST'])
#def home(data):
 #   var=data
  #  print(var)
   # data = "hello"
    #return render_template('home.html', data=data )

'''

if __name__ == '__main__':
    app.run()

