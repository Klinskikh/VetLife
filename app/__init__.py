from flask import Flask

app = Flask(_name_)
app.config.from_object('config')

from app import views