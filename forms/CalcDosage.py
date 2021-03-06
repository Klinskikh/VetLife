# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import FloatField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms_alchemy import QuerySelectField
from VetLife import models
from .. import db


class CalcDosageForm(Form):
    weigth = FloatField(u'Вес животного', validators=[DataRequired()])
    animal_type = QuerySelectField(query_factory=lambda: db.session.query(models.AnimalType),
                                   label=u"Тип животного",
                                   blank_text=u"Выберите",
                                   validators=[DataRequired()])

    def calc(self, medicine):
        dosage = models.Dosage.query.filter_by(active_substance=medicine.active_substance, animal_type=self.animal_type.data)
        result = dict(d_from=self.weigth.data * dosage[0].value / medicine.active_amount)
        value_max = dosage[0].value_max and dosage[0].value_max or dosage[0].value
        result['d_to'] = self.weigth.data * value_max / medicine.active_amount
        return result
