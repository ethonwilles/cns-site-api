from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText



app = Flask(__name__)


CORS(app)
client = pymongo.MongoClient(mongo_uri)
db = client['conv']
col = db['client_info']

@app.route('/log-submission' , methods=["POST"])
def logger():
    

    try:
        name = request.json["name"]
        email = request.json["email"]
        number = request.json["number"]
        desc = request.json["desc"]

        

        msg = MIMEText(f""" 
        New Service Logged From Website:
        Name : {name}
        Email : {email}
        Phone Number : {number}
        Description of Service Wanted : {desc}
        """)
        msg['Subject'] = "Customer Service"
        msg['From']    = "cnsnewservicerequest@gmail.com"
        msg['To']      = "ethonwilles@gmail.com"

        s = smtplib.SMTP('smtp.mailgun.org', 587)

        s.login('postmaster@sandboxf7fb33ace9a04f1a9536131e9280ab4c.mailgun.org', secret_key)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
        col.insert_one({'name' : name , 'email' : email, 'number': number, 'desc': desc})
        return {'LOGGED_INFORMATION' : True}
    except:
        return {'LOGGED_INFORMATION' : False}

if __name__ == '__main__':
    app.run(debug=True)



