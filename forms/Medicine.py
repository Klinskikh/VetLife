# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea
from wtforms_alchemy import QuerySelectField
from flask_admin.form.widgets import Select2Widget
from . import ModelForm
from VetLife import models


class MedicineForm(ModelForm):
    active_substance = QuerySelectField(query_factory=models.ActiveSubstance.query.all, label=u"Действующее вещество"
                                        , widget=Select2Widget())

    class Meta:
        model = models.Medicine
        field_args = {'descr': {'widget': TextArea()}}

