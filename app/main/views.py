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
    
    title = 'Pitch Space'
    
    return render_template('index.html', title = title)


@main.route('/loggedin')
def loggedin():

    title = 'Pitch Space'

    return render_template('loggedin.html',title =title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = f'{uname} Profile'
    return render_template("profile/profile.html", user = user, title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])

def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    title = 'Update | Profile'
    return render_template('profile/update.html',form =form, title = title)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/categories')
def categories():


    title = 'Pitches | Categories'
    pitch = Pitch.query.filter_by().first()
    twitter = Pitch.query.filter_by(category="twitter")
    elevator = Pitch.query.filter_by(category = "elevator")
    competition = Pitch.query.filter_by(category = "competition")
    investor = Pitch.query.filter_by(category = "investor")
    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    return render_template('categories.html',title =title, pitch = pitch, twitter=twitter, elevator= elevator, competition = competition, investor = investor, upvotes=upvotes )

@main.route('/pitches/new/', methods = ['GET','POST'])

def new_pitch():
    form = AddPitch()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        pitcher = form.pitcher.data
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category, pitcher = pitcher)
        db.session.add(new_pitch)
        db.session.commit()
         
        return redirect(url_for('main.categories'))
    return render_template('add_pitch.html',form=form)

        
        
        


        
        






