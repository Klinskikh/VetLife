# -*- coding: utf-8 -*-
from wtforms import SelectField
from wtforms_alchemy import QuerySelectField

from . import ModelForm
from VetLife import models


class DosageForm(ModelForm):

    class Meta:
        model = models.Dosage
