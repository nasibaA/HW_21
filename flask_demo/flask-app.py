#!/usr/bin/env python
import os
from unicodedata import category
#pip install flask
from flask import Flask, json, render_template, request, send_file, Response

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/") # return text
def echo_hello():
    text = '''go to /all to see all data\
        and/year/(year)(with a specific year specified where the parenthesis are)
         to see prizes for that year <br>\ and /add to add additional data'''
    return text

@app.route("/all") # return all nobel.json
def all():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

  
    return render_template("index.html",data=data_json)


@app.route("/year/<year>",methods = ['GET'])

def add_year(year):
    json_url = os.path.join(app.static_folder,"nobel.json")
    data_json = json.load(open(json_url))
    data = data_json["prizes"]
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['prizes']
        year = request.view_args['year']
        output_data = [x for x in data if x['year']==year]

        return render_template('prizes.html',html_page_text=output_data)



@app.route("/add") # adding new information
def addform():
    
    #form_url = os.path.join("templates","form.html")
    #return send_file(form_url)
    return render_template("form_simple.html") 
    
@app.route('/save', methods=['POST'])
def save():
        json_url = os.path.join(app.static_folder,"","nobel.json")
        data_json = json.load(open(json_url))
        year = request.form['year']
        laureates = request.form['laureates']
        id = request.form['id']
        firstname = request.form['firstname']
        surname = request.form['surname']
        category = request.form['category']
        motivation = request.form['motivation']
        share = request.form['share']
        form_data = request.form
        members = []
        data = {'year':year,
            'category':category}

        member = {'laureates':laureates,
                    'id':id,
              'firstname':firstname,
              'surname':surname,
                'motivation':motivation,
                'share':share}
        members.append(member)
   

        data_json = json.load(open(json_url))
        prizes = data_json['prizes']
        prizes.append(data)
        data_json['prizes'] = prizes    

        with open(json_url,'r+') as file:
                data_json = json.load(file)
                data_json['prizes'].append(data)
                json.dump(data_json, file)
        return render_template('index.html', data = form_data)        
   
 


if __name__ == "__name__":
            app.run(debug=True)
