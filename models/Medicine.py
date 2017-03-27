# -*- coding: utf-8 -*-
from VetLife import db


class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True, info={'label': u'Наименование'})
    descr = db.Column(db.String(65000), info={'label': u'Описание'})
    active_amount = db.Column(db.Float, info={'label': u'Количество действующего вещества (мг/мл)'})

    def __repr__(self):
        return self.title
