from flask import Flask,render_template
from flask import request as f_request
import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import utils
import pandas as pd
from main import main

global email_list, email_dict
email_list = []
email_dict= {}
email_list=main()
for i in range(len(email_list)):
     email_dict[f'{i+1}-->']=email_list[i]
print(email_dict)
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def dashboard():
    x={}
    if f_request.method == "POST":
            x=email_dict
        # req=f_request.form
        # number_of_applicants=req["number_of_applicants"]
        # title_of_applicant=req["title_of_applicant"]
    return render_template("HushHush.html", email_dict=x)


if __name__=='__main__':
    app.run(debug=True)

