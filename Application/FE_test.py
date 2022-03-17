from flask import Flask,render_template
from flask import request as f_request
import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import utils
import pandas as pd

app=Flask(__name__)




@app.route("/",methods=["GET","POST"])
def dashboard():
    global email_list, email_dict
    email_list = []
    email_dict = {}
    if f_request.method == "POST":
        req = f_request.form
        number_of_applicants= req["number_of_applicants"]
        title_of_applicant=req["title_of_applicant"]
        email_dict={'a':'sasha','b':'omer'}
        print(number_of_applicants)
        print(title_of_applicant)
        #
        # df_main = utils.data_tools.merge()
        #
        # if title_of_applicant == 'Solution Architect':
        #     df = utils.candidate_selection.algorithm_1(0.1, 0.2, 0.3, df_main)[0]
        #     email_list = utils.tools.select_mails(df, number_of_applicants)
        #     #utils.emailing.batch_email(email_list,number_of_candidates)
        #
        #
        # if title_of_applicant == 'Senior Developer':
        #     df = utils.candidate_selection.algorithm_1(0.1, 0.2, 0.3, df_main)[1]
        #     email_list = utils.tools.select_mails(df, number_of_applicants)
        #     # utils.emailing.batch_email(email_list,number_of_candidates)
        #
        #
        # if title_of_applicant == 'Developer':
        #     df = utils.candidate_selection.algorithm_1(0.1, 0.2, 0.3, df_main)[2]
        #     email_list = utils.tools.select_mails(df, number_of_applicants)
        #     # utils.emailing.batch_email(email_list,number_of_candidates)
        #
        # for i in range(len(email_list)):
        #     email_dict[f'Applicant {i + 1}->'] = email_list[i]
        #
    return render_template("HushHush.html",email_dict=email_dict)
if __name__=='__main__':
    app.run(debug=True)

