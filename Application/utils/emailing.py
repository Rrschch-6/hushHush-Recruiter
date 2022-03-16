import smtplib
import sorting

#numberofattande=5
#role="Solution Architecht"
#receiver=sorting.select_attandee(numberofattande,role)
#print((receiver))

ADRESS="srhrecruiter1@gmail.com"
PASSWORD="SRHrecruiter1"
receiver=["kiyami_erdim@hotmail.com"]

with smtplib.SMTP("smtp.gmail.com",587,timeout=100) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(ADRESS,PASSWORD)
    for i in receiver:
        subject="Congratilations you selected from SRHrecruiter"
        body="Please click the link attending our quiz:)" \
         "https://www.surveymonkey.de/r/MCCDFR3"
        msg=f'Subject:{subject}\n\n{body}'
        smtp.sendmail(ADRESS,receiver,msg)

#from flask import Flask
#app = Flask(__name__)
#@app.route('/')
#def hello_world():
        #return 'What is decorater?'
#if __name__ == '__main__':
   #app.run()


