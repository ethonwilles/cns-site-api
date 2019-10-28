from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS


app = Flask(__name__)


CORS(app)
client = pymongo.MongoClient('mongodb+srv://ethonwilles:password54123@cluster0-t779q.mongodb.net/conv?retryWrites=true&w=majority')
db = client['conv']
col = db['client_info']

@app.route('/log-submission' , methods=["POST"])
def logger():
    

    try:
        name = request.json["name"]
        email = request.json["email"]
        number = request.json["number"]
        desc = request.json["desc"]

        col.insert_one({'name' : name , 'email' : email, 'number': number, 'desc': desc})
        return {'LOGGED_INFORMATION' : True}
    except:
        return {'LOGGED_INFORMATION' : False}

if __name__ == '__main__':
    app.run(debug=True)



