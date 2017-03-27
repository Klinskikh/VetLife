# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea
from wtforms_alchemy import QuerySelectField
from . import ModelForm
from VetLife import models
from .. import db

class MedicineForm(ModelForm):
    active_substance = QuerySelectField(query_factory=lambda: db.session.query(models.ActiveSubstance),
                                        label=u"Действующее вещество",
                                        allow_blank=True,
                                        blank_text=u"Не задано")

    class Meta:
        model = models.Medicine
        field_args = {'descr': {'widget': TextArea()}}

