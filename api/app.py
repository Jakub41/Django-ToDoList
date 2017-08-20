from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import json
from bson import ObjectId


'''
This is a custom JSONEncoder to encode Mongos ObjectId
class. The regular JSON serializer is not able to serializer
an ObjectId.
'''
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
CORS(app)  # Allow Cross Origin Domain Requests

# Configure the mongodb connection
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'todos'
mongo = PyMongo(app, config_prefix='MONGO')
app.json_encoder = JSONEncoder


'''
PUT implementation: Updation of new task
'''
@app.route('/tasks/<string:task_id>', methods = ['PUT'])
def update_task(task_id):
    if not request.json:
        abort(400)

    task = mongo.db.tasks.find_one_or_404({'_id': ObjectId(task_id)})
    if 'text' in request.json:
        text = request.json['text']
    else:
        text = task['text']
    if 'completed' in request.json:
        completed = request.json['completed']
    else:
        completed = task['completed']
    if task:
        mongo.db.tasks.update_one({'_id': ObjectId(task_id)},
            {
                '$set': {
                    'text': text,
                    'completed': request.json['completed']
                }
            }
        )
        task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
        return jsonify(task)
    else:
        abort(404)

'''
DELETE implementation: deleting an existing task
'''
@app.route('/tasks/<string:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = mongo.db.tasks.find_one_or_404({'_id': ObjectId(task_id)})
    if task:
        mongo.db.tasks.delete_one(task)
    return jsonify({ 'result': True }), 200

'''
POST implementation: creation of new task
'''
@app.route('/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'text' in request.json:
        abort(400)
    task = request.json
    tasks = mongo.db.tasks
    tasks.insert_one(task).inserted_id
    return jsonify(task), 201

'''
GET implementation: get a particular task
'''
@app.route('/tasks/<string:task_id>', methods = ['GET'])
def get_task(task_id):
    task = mongo.db.tasks.find_one_or_404({'_id': ObjectId(task_id)})
    return jsonify(task)

'''
GET implementation: get list of all tasks
'''
@app.route('/tasks', methods = ['GET'])
def get_tasks():
    tasks = [t for t in mongo.db.tasks.find()]
    return jsonify(tasks)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({ 'error' : 'Not Found' }), 404)

if __name__ == '__main__':
    app.run(debug = True)
