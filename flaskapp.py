from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/add-data", methods=["POST"])
def add_task():
   if not request.json:

    return jsonify({
        "status":"error",

        "message":"Please provide the data!"
    },400)

contact = {
    'id' : tasks[-1]['id'] + 1,

    'Name' : request.json['Name'],

    'Contact' : request.json.get('Contact', ""),
    'done' : False
}