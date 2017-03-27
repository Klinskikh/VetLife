# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea

from . import ModelForm
from VetLife.models import Dosage


class DosageTypeForm(ModelForm):
    class Meta:
        model = Dosage
        field_args = {'descr': {'widget': TextArea()}}

