# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea

from . import ModelForm
from VetLife.models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        field_args = {'descr': {'widget': TextArea()}}

