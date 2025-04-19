from flask import Flask, redirect, request, render_template, session
from flask_session import Session

import project5

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app) # tells the flask app to have sessions

def is_logged_in():
    if not session.get('email'):
        return False
    return True

@app.route('/project5')
def homepage_html():
    return render_template('homepage.html')

@app.route('/project5/login')
def login():
    if is_logged_in():
        return render_template('account.html', email=session.get('email'))
    else:
        return render_template('login.html')

@app.route('/project5/account')
def account_html():
    if is_logged_in():
        return render_template('account.html')
    else:
        return redirect('/project5/login')

@app.route('/project5/logout')
def logout():
    session.pop('email', None)
    return redirect('/project5') # will have button to return to login page

@app.route('/acc_login', methods=['POST'])
def acc_login():
    return project5.login(request.form) #request.form is for 'POST' request bc it sends the form, so it receives the form

@app.route('/project5/uploadfile', methods=['POST'])
def project5_uploadfile():
    return project5.uploadfile(request.form)

@app.route('/project5/deletefile', methods=['POST'])
def project5_deletefile():
    return project5.deletefile(request.form)

@app.route('/project5/listfiles')
def project5_listfiles():
    return project5.listfiles()
