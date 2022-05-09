from flask import app
from flask import render_template,request,redirect,url_for
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Pitch Space'
    
    return render_template('index.html', title = title)


@app.route('/loggedin')
def loggedin():

    title = 'Pitch Space'

    return render_template('loggedin.html',title =title)