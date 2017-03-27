# -*- coding: utf-8 -*-
from wtforms import SelectField
from wtforms_alchemy import QuerySelectField

from . import ModelForm
from VetLife import models


class ActiveSubstanceForm(ModelForm):
    class Meta:
        model = models.ActiveSubstance
