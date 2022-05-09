from flask import render_template,request,redirect,url_for,abort,flash
from ..import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,AddPitch,CommentForm,UpvoteForm,Downvote
from .. import db,photos
from flask.views import View,MethodView


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Pitch Deck'
    
    return render_template('index.html', title = title)


@main.route('/loggedin')
def loggedin():

    title = 'Pitch Deck'

    return render_template('loggedin.html',title =title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = f'{uname} Profile'
    return render_template("profile/profile.html", user = user, title = title)






