# -*- coding: utf-8 -*-
from VetLife import db


class Dosage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_from = db.Column(db.Float, info={'label': u'От'})
    d_to = db.Column(db.Float, info={'label': u'До'})
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    medicine = db.relationship('Medicine', backref=db.backref('dosages', lazy='dynamic'), info={'label': u'Препарат'})
    dosage_type_id = db.Column(db.Integer, db.ForeignKey('dosage_type.id'))
    dosage_type = db.relationship('DosageType', backref=db.backref('dosages', lazy='dynamic'), info={'label': u'Тип дозировки'})

    def __repr__(self):
        return u'<Дозировка от {0} до {1}>'.format(self.d_from, self.d_to)
