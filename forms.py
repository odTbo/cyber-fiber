from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, URL, Email, Length


class RegisterForm(FlaskForm):
    email = StringField("E-mail*", validators=[DataRequired(), Email(), Length(min=7, max=30)])
    age = StringField("Age*", validators=[DataRequired(), Length(min=1, max=3)])
    password = PasswordField("Password (min. 8 characters)", validators=[DataRequired(), Length(min=8, max=40)])
    password_confirm = PasswordField("Confirm Password (min. 8 characters)", validators=[DataRequired(), Length(min=8, max=40)])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email(), Length(min=7, max=30)])
    password = PasswordField("Password (min. 8 characters)", validators=[DataRequired(), Length(min=8, max=40)])
    submit = SubmitField("Submit")


class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Content", validators=[DataRequired()], id="FormPostBody")
    submit = SubmitField("Submit")
