# -*- coding: utf-8 -*-
from VetLife import db


class ActiveSubstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), info={'label': u'Наименование'})
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    medicine = db.relationship('Medicine', backref=db.backref('medicines', lazy='dynamic'), info={'label': u'Препарат'})

    def __repr__(self):
        return u'{0}'.format(self.name)
