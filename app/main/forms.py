from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add or Update your bio ',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
    
class AddPitch(FlaskForm):
    pitcher = StringField("Submitted By: Your Name ...", validators = [DataRequired()])
    title = StringField("Pitch Title", validators = [DataRequired()])
    category = SelectField("What category are you submitting to?", choices=[("fashion", "Fashion"), ( "music", "Music"), ("sports", "Sports"), ("design", "Design")],validators=[DataRequired()])
    description = TextAreaField('What pitch do you want to share?',validators = [DataRequired()] )
    submit = SubmitField('Submit') 
    
class CommentForm(FlaskForm):

    description = TextAreaField('Add a comment',validators = [DataRequired()] )
    submit = SubmitField('Submit')  
    
class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()
