from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField
from wtforms.validators import Required, Length


class EditForm(Form):
    nickname = TextField('nickname', validators=[Required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
