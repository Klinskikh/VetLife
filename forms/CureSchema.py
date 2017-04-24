# -*- coding: utf-8 -*-
from wtforms.widgets import TextArea
from wtforms_alchemy import QuerySelectField
from . import ModelForm
from VetLife import models
from .. import db


class CureSchemaForm(ModelForm):
    class Meta:
        model = models.CureSchema
        field_args = {'descr': {'widget': TextArea()}, 'cure': {'widget': TextArea()}}

