from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app=Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'SCHOOL_STATE': True, 'RESOURCE_TYPE': True, 'POVERTY_LEVEL': True,'TOTAL_DONATIONS': True, 'DATE_POSTED': True,  '_id': False}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donorschoose/projects')
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS,limit=10000)
    json_projects=[]
    for project in projects:
        json_projects.append(project)

    json_projects=json.dumps(json_projects,default=json_util.default)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)