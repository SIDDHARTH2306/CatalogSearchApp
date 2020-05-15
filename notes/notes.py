from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
import csv


app = Flask(__name__)
api = Api(app)

class Notes(Resource):
    def __init__(self):
        pass

    def get(self):
        keyword = request.args.get('keyword')
        results=[]
        with open('notes.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                results.append(row)
        data=[]
        for i in results:
            if i.get('keyword') == keyword:
                data.append(i)
            else:
                print("Inside else")
                #do nothing
        return render("some URL", data=data)

    def post(self):
        content = request.form.get('content')
        keyword = request.form.get('keyword')
        temp={
            "keyword": keyword,
            "content": content
            }
        with open('notes.csv', 'a+',newline='') as csvfile:
                fieldnames = ['keyword', 'content']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(temp)


api.add_resource(Notes,'/notes')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5003,debug=True)
