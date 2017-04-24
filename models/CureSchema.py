# -*- coding: utf-8 -*-
from VetLife import db


class CureSchema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True, info={'label': u'Наименование'})
    descr = db.Column(db.String(65000), info={'label': u'Диагностика'})
    crue = db.Column(db.String(65000), info={'label': u'Лечение'})

    def __repr__(self):
        return self.title
