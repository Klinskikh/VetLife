# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea

from . import ModelForm
from VetLife.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
