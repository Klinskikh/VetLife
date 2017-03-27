# -*- coding: utf-8 -*-
from VetLife import db


class Dosage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_from = db.Column(db.Integer, info={'label': u'От'})
    d_to = db.Column(db.Integer, info={'label': u'До'})
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    medicine = db.relationship('Medicine', backref=db.backref('dosages', lazy='dynamic'), info={'label': u'Препарат'})
    dosage_type_id = db.Column(db.Integer, db.ForeignKey('dosage_type.id'))
    dosage_type = db.relationship('DosageType', backref=db.backref('dosages', lazy='dynamic'), info={'label': u'Тип дозировки'})
