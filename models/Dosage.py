from VetLife import db


class Dosage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_from = db.Column(db.Integer)
    d_to = db.Column(db.Integer)
    medicine_id = db.Column(db.Integer, db.ForeignKey('Medicine.id'))
    dosage_type_id = db.Column(db.Integer, db.ForeignKey('DosageType.id'))
    weight = db.Column(db.Integer)
    unit_id = db.Column(db.Integer, db.ForeignKey('Unit.id'))
