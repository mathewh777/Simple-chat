from flask import Flask, request, render_template_string
import mysql.connector
import time
from html_temp import *
from werkzeug.serving import WSGIRequestHandler
from werkzeug import serving
from werkzeug.testapp import test_app

app = Flask(__name__)

#TODO Add private msgs, styling, iframes

@app.route('/messages', methods=['GET'])
def pub_msgs():
    cursor.execute("SELECT * FROM Chatdata Where status=\"public\";")
    results = cursor.fetchall()
    for x in results:
        text_blob.append(("%s" % (text_style))+' - '.join(x))
        msgs = ("</p>").join(text_blob)+"</p>"
    text_blob.clear()
    return msgs

@app.route('/private', methods=['GET'])
def priv_msgs():
    cursor.execute("SELECT * FROM Chatdata Where status=\"user\";")
    results = cursor.fetchall()
    for x in results:
        text_blob.append(' - '.join(x))
        msgs = "<br>".join(text_blob)
    text_blob.clear()
    return msgs

@app.route('/', methods = ['POST', 'GET'])
def main(environ, start_response):
    if request.method == "POST":
        msg = request.form.get("msg")
        cursor.execute("INSERT INTO Chatdata (time, status, user, msg) VALUES (%s, %s, %s, %s);", (time.strftime("%H:%M:%S"), "public", "user", msg))
        connection.commit()
        return html_bd + iframe +render_template_string(form)
    if request.method == "GET":
        name = request.form.get("msg")
        return html_bd + iframe + render_template_string(form)

msgs = ""
if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    serving.run_simple("localhost", 5000, main)
    #app.run()




#cursor = connection.cursor()
#cursor.execute("SELECT * FROM visitor_counter")
#connection.commit()
#gets the output
#result = cursor.fetchall()
#print(result)

#INSERT INTO Chatdata (time, user, msg)
#VALUES (time,'user','msg');

#CREATE TABLE Chatdata (time varchar(255),user varchar(255),msg varchar(255));
#DROP TABLE Chatdata
#DELETE FROM Chatdata Where table_name="user";
#DELETE FROM Chatdata LIMIT 1;

#select * from Chatdata where status="user" AND user="user";
