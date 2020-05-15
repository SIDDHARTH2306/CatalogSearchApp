import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search():
    print("Hello")
    keyword = request.form.get('keyword')
    url1 = "http://127.0.0.1:5005/search?keyword={}".format(keyword)
    url2 = "http://127.0.0.1:5002/catalogue?keyword=Carol"

    #requests.get(url1)
    data=requests.get(url2)

    return render_template("temp.html",data=data)

@app.route('/notes', methods=['POST'])
def notes():
    return render_template('notes.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
