from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,email


class Authorforms(FlaskForm):

    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),email()])
    website = StringField('Website', validators=[DataRequired()])
    photo = StringField('Photo', validators=[DataRequired()])
    bio = TextAreaField('Biografia', validators=[DataRequired()])

class Categoryforms(FlaskForm):

    name = StringField('Nome', validators=[DataRequired()])