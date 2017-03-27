# -*- coding: utf-8 -*-
from wtforms import SelectField
from wtforms_alchemy import QuerySelectField

from . import ModelForm
from VetLife import models


class DosageForm(ModelForm):
    animal_type = QuerySelectField(query_factory=models.AnimalType.query.all, label=u"Тип животного")

    class Meta:
        model = models.Dosage
