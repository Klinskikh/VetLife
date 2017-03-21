from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from VetLife import db
BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

from .Login import LoginForm
from .Profile import EditForm
from .Edit_profile import EditForm
from .Medicine import MedicineForm