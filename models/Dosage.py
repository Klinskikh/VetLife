# -*- coding: utf-8 -*-
from VetLife import db


class Dosage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_type_id = db.Column(db.Integer, db.ForeignKey('animal_type.id'))
    animal_type = db.relationship('AnimalType', backref=db.backref('animal_types', lazy='dynamic'), info={'label': u'Вид животного'})
    active_substance_id = db.Column(db.Integer, db.ForeignKey('active_substance.id'))
    active_substance = db.relationship('ActiveSubstance', backref=db.backref('active_substances', lazy='dynamic'), info={'label': u'Дейсвующее вещество'})
    value = db.Column(db.Float, info={'label': u'Дозировка (мг/кг)'})

    def __repr__(self):
        return u'<Дозировка для {0}:{1}>'.format(self.animal_type, self.value)
