# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea
from wtforms_alchemy import QuerySelectField

from . import ModelForm
from VetLife import models


class MedicineForm(ModelForm):
    unit = QuerySelectField(query_factory=models.Unit.query.all, label=u"Еденица измерения")
    class Meta:
        model = models.Medicine
        field_args = {'descr': {'widget': TextArea()}}

