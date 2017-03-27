# -*- coding: utf-8 -*-
from VetLife import db


class AnimalType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), info={'label': u'Вид животного'})

    def __repr__(self):
        return u'{0}'.format(self.name)
