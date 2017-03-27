# -*- coding: utf-8 -*-
from wtforms_alchemy import QuerySelectField
from .. import db

from . import ModelForm
from VetLife import models


class DosageForm(ModelForm):
    animal_type = QuerySelectField(query_factory=lambda: db.session.query(models.AnimalType), label=u"Тип животного")

    class Meta:
        model = models.Dosage
