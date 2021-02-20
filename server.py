#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


db_connect = create_engine('sqlite:///C:/Users/ankth/OneDrive/Desktop/TarunHouseKeeping.db')
app = Flask(__name__)
api = Api(app)



class Asset(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        AssetID = request.json['ASID']
        AssetName = request.json['ASNM']
        COST = request.json['COST']
        query = conn.execute("insert into AssetsDsc values('{0}','{1}','{2}')".format(AssetID,AssetName,COST))
        return {'status':'success'}
    
    
class Task(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        TaskDID = request.json['TDID']
        Taskf =request.json['TF']
        TDESC = request.json['TDSC']
        query = conn.execute("insert into Tasks values('{0}','{1}','{2}')".format(TaskDID,Taskf,TDESC))
        return {'status':'success'}
        

class Worker(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        WorkID = request.json['WID']
        Name = request.json['Nm']
        Phno = request.json['Phno']
        Addr = request.json['Add']
        query = conn.execute("insert into Worker values('{0}','{1}','{2}','{3}')".format(WorkID,Name,Phno,Addr))
        return {'status':'success'}
    
class PrAsser(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from AssetsDsc ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class AllocateTask(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        TimeofAllocation = request.json['TOA']
        TimeToBePeBy = request.json['TOP']
        TaskID = request.json['TID']
        ASSETTID = request.json['ASTID']
        WorkTaskID = request.json['WTID']
        query = conn.execute("insert into TaskAll values('{0}','{1}','{2}','{3}','{4}')".format(TaskID,ASSETTID,WorkTaskID,TimeofAllocation,TimeToBePeBy))
        return {'status':'success'}

api.add_resource(Home, '/') 
api.add_resource(Asset, '/add-asset')
api.add_resource(Task, '/add-task') 
api.add_resource(Worker, '/add-worker') 
api.add_resource(PrAsser, '/assests/all')
api.add_resource(AllocateTask, '/allocate-task')


if __name__ == '__main__':
     app.run(port=3134)  
