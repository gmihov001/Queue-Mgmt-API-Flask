"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Guest
from datastructures import Queue
from sms import send


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

queue = Queue()

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/queue', methods=["GET"])
def print_queue():
    tmp_queue = queue.get_queue()
    size = queue.get_size()

    response = {
        "queue_size": f"There are {size} people in the queue",
        "queue": tmp_queue,
        "next": f"Next in line: {tmp_queue[size - 1]}" if size else "No next in line"
    }
    return jsonify(response), 200

@app.route('/queue', methods=['POST'])
def add():
    guest = request.json
    queue.enqueue(guest)
    tmp_queue = queue.get_queue()
    size = queue.get_size()
    response = {
        "added": f"{tmp_queue[0]} has been added to queue",
        "current_queue": tmp_queue,
        "queue_size": f"There are now {size} people in the queue"
    }

    return jsonify(response), 200

@app.route('/queue', methods=['DELETE'])
def dequeue():
    call_person = queue.dequeue()
    phone = call_person['number']
    send(body=f"{call_person['name']}, your table is ready!", to=phone)
    response = {}
    return jsonify(f"Texted {call_person['name']} at {call_person['number']}."), 200    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
