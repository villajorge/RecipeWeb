from flask import Flask, redirect, url_for, render_template, request
import http.client
import json
import os
import sqlite3

cur_loc = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)

@app.route('/')
def index():
    conn = http.client.HTTPSConnection("themealdb.p.rapidapi.com")
    headers = {
    'X-RapidAPI-Key': "a174ac89eamshf7c57f29f424319p17a06djsn41bb1dfbf0f3",
    'X-RapidAPI-Host': "themealdb.p.rapidapi.com"
    }

    conn.request("GET", "/randomselection.php", headers=headers)
    res = conn.getresponse()
    data = res.read()
    diction = json.loads(data)    
    return render_template("index.html",res=diction)


@app.route('/search', methods=["POST","GET"])
def search():
    if request.method == "POST":
        ingr = request.form.get("ingr")
    
        url = "themealdb.p.rapidapi.com"
        conn = http.client.HTTPSConnection(url)
        headers = {
	        'X-RapidAPI-Key': "a174ac89eamshf7c57f29f424319p17a06djsn41bb1dfbf0f3",
            'X-RapidAPI-Host': "themealdb.p.rapidapi.com"
        }

        conn.request("GET",f"/filter.php?i={ingr}", headers=headers)
        res =conn.getresponse()
        data = res.read()
        
        diction = json.loads(data)
        if diction["meals"] == None:
            string = "Could not find any recipes with that ingredient"
            return render_template("search.html", string = string)

        
        return render_template("results.html", res=diction)
    else: 
        return render_template("search.html")
    
@app.route('/instructions/<id>', methods=["POST","GET"])
def instructions(id):
    conn = http.client.HTTPSConnection("themealdb.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': "a174ac89eamshf7c57f29f424319p17a06djsn41bb1dfbf0f3",
    'X-RapidAPI-Host': "themealdb.p.rapidapi.com"
    }
    #print("Grabbing stuff")
    conn.request("GET", f"/lookup.php?i={id}",headers=headers)
    res = conn.getresponse()
    data = res.read()
    diction = json.loads(data)
    #print(diction)
    return render_template("instructions.html", res=diction)

# @app.route('/cat')
# def cat():
#     return render_template("cat.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")

# @app.route('/login', methods = ['POST'])
# def getInfo():
#     UN = request.form('')

if __name__ == "__main__":
    app.run(debug=True)