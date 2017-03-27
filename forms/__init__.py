from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from VetLife import db
BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

from .Login import LoginForm
from .Medicine import MedicineForm
from .Dosage import DosageForm
from .DosageType import DosageTypeForm
from .Unit import UnitForm
from .Profile import ProfileForm