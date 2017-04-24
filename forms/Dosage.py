# -*- coding: utf-8 -*-
from wtforms.validators import Optional, DataRequired
from wtforms_alchemy import QuerySelectField

from .form_fields import MyFloatField
from .. import db

from . import ModelForm
from VetLife import models


class DosageForm(ModelForm):
    animal_type = QuerySelectField(query_factory=lambda: db.session.query(models.AnimalType), label=u"Тип животного")
    value = MyFloatField(u'от', validators=[DataRequired()])
    value_max = MyFloatField(u'до', validators=[DataRequired()])

    class Meta:
        model = models.Dosage
