from VetLife import db


class Dosage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_from = db.Column(db.Integer)
    d_to = db.Column(db.Integer)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    medicine = db.relationship('Medicine', backref=db.backref('dosages', lazy='dynamic'))
    dosage_type_id = db.Column(db.Integer, db.ForeignKey('dosage_type.id'))
    dosage_type = db.relationship('DosageType', backref=db.backref('dosages', lazy='dynamic'))
    weight = db.Column(db.Integer)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))
    unit = db.relationship('Unit', backref=db.backref('dosages', lazy='dynamic'))