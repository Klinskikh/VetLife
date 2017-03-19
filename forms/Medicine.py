# -*- coding: utf-8 -*-
from . import ModelForm
from VetLife.models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine

