# -*- coding: utf-8 -*-
from wtforms import SelectField
from wtforms_alchemy import QuerySelectField

from . import ModelForm
from VetLife import models


class DosageForm(ModelForm):
    dosage_type = QuerySelectField(query_factory=models.DosageType.query.all, label=u"Тип дозировки")

    class Meta:
        model = models.Dosage
