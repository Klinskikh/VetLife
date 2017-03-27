from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, Length


class ProfileForm(Form):
    nickname = TextField('nickname', validators=[Required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
