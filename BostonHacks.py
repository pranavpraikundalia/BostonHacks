from flask import Flask, Response, request, render_template, redirect, url_for, session,jsonify
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from flaskext.mysql import MySQL


import datetime,time,requests
from os import *
#from flaskext.mysql import MySQL
#import datetime, os, shutil
from twilio.rest import *
from twilio import *



app = Flask(__name__, static_folder="static")
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'I(E(ream7861'
app.config['MYSQL_DATABASE_DB'] = 'BostonHacks'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
app = Flask(__name__)


# My number = 16178299091
# secret key = bvRm9fytaLHf54TQkhZ70SifB9wR8VgN
# Your Account SID from twilio.com/console
#account_sid = "AC072910fce1e2bad15bf85051f2e932e5"
# Your Auth Token from twilio.com/console
#auth_token = "81e4aa1d436687b464db9335ff9a3d32"

#client = Client(account_sid, auth_token)


# Your Account Sid and Auth Token from twilio.com/console
#api_key_sid = "SKd282f2bee6cf6ca53946cc380e928fcc"
#api_key_secret = "bvRm9fytaLHf54TQkhZ70SifB9wR8VgN"
#client = Client(api_key_sid, api_key_secret)

#room = client.video.rooms('RMf3f98109f841f26f1c649f5eea51e286').fetch()

#room = client.video.rooms.create(unique_name='Room1')

#print(room.sid)

#Twilio.Video.Connect

#message = client.messages.create(
#        to="+18572058079",
#        from_="+16178299091",
#       body="Hello from Python!")

#print(message.sid)

def extractData(cursor):
    data = []
    for item in cursor:
        data.append(item)
    return data



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/<data>',methods=['POST', 'GET'])
def signup(data):
    assert data == request.view_args['data']
    if data=='doc':
        cursor.execute("Select * from category where cat_parent='doctor'")
        category=extractData(cursor)
        return render_template('doc_register.html',cat=category)
    if data=='tutor':
        cursor.execute("Select * from category where cat_parent='tutor'")
        category=extractData(cursor)
        return render_template('doc_register.html',cat=category)
    if data=='coder':
        cursor.execute("Select * from category where cat_parent='coder'")
        category=extractData(cursor)
        return render_template('doc_register.html',cat=category)
    if data == 'user':
        cursor.execute("Select * from category")
        category = extractData(cursor)
        return render_template('user_register.html',cat=category)
@app.route('/register/<data>',methods=['POST','GET'])
def register(data):
    assert data == request.view_args['data']
    if data=='va':
        va_id = request.form['va_id']
        va_name = request.form['va_name']
        va_address = request.form['va_address']
        va_categories=request.form.getlist('categories')
        #print(va_categories)
        #print(request.form.getlist('categories'))
        va_day=request.form['day']
        va_start_hr=request.form['start_time_hr']
        va_start_min = request.form['start_time_min']
        va_end_hr = request.form['end_time_hr']
        va_end_min = request.form['end_time_min']
        cursor.execute("Insert into virtual_assistant Values(%s,%s,%s)",(va_id,va_name,va_address))
        conn.commit()
        cursor.execute("Insert into schedule Values(%s,%s,%s,%s,%s,%s)", (va_id,va_day,va_start_hr,va_start_min ,va_end_hr,va_end_min))
        conn.commit()
        for category in va_categories:
            cursor.execute("Insert into specialization Values(%s,%s)",(va_id,category))
            conn.commit()
        return render_template('index.html')

    elif data=='user':
        va_categories = request.form.getlist('categories')
        user_id = request.form['u_id']
        user_name = request.form['user_name']
        cursor.execute("Select * from User where u_id=%s",user_id)
        if cursor.rowcount<1:
            cursor.execute("Insert into User Values(%s,%s)", (user_id, user_name))
            conn.commit()
        query_result=[]
        for i in va_categories:
            query_get_numbers=("Select v.va_id,sc.va_day,sc.start_hr,sc.start_min ,sc.end_hr,sc.end_min from virtual_assistant v, specialization s,schedule sc where s.cat_id=%s and v.va_id=s.va_id and sc.va_id=v.va_id")
            cursor.execute(query_get_numbers,(i))
            query_result.append(extractData(cursor))
        numbers=[]
        now = datetime.datetime.now()
        for i in query_result:
            for j in i:
                numbers.append(j)
        numbers=set(numbers)
        helpers_to_call=[]
        for i in numbers:
            start=now.replace(hour=i[2], minute=i[3], second=0, microsecond=0)
            end=now.replace(hour=i[4], minute=i[5], second=0, microsecond=0)
            if i[1]==time.strftime("%a"):
                if now>start and now<end:
                    helpers_to_call.append(i[0])
        print(user_id)
        print(helpers_to_call)
        return render_template('call.html', from_call=helpers_to_call, to_call=user_id)
#@app.route('/home/<data>', methods=['POST'])
#def home(data):
 #   var=data
  #  print(var)
   # data = "hello"
    #return render_template('home.html', data=data )



if __name__ == '__main__':
    app.run()

