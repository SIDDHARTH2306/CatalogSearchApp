from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
from bson.json_util import dumps
from bson.json_util import loads
import csv
import pymongo
from pymongo import MongoClient
from flask import flash, render_template, request, redirect, make_response


app = Flask(__name__,template_folder="template")
api = Api(app)




class Data(Resource):

    
    def __init__(self):
        pass

    def get(self):
        headers = {'Content-Type': 'text/html'}
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydb"]
        mycol = mydb["books"]


        keyword = request.args.get('keyword')
        data = mycol.find({"Title":{'$regex':keyword, '$options':"$i"}})
        #data2= mycol.find({"Author":{'$regex':keyword, '$options':"$i"}})
        
        #return make_response(render_template('catalogue.html',data=data),200,headers)
        print(data)
        return loads(dumps(data))


api.add_resource(Data,'/catalogue')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002,debug=True)
