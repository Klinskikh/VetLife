from VetLife import db
from .BaseModel import BaseModel


class Audit(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(64), index=True)
    object_id = db.Column(db.Integer, index=True)
    descr = db.Column(db.String(1024))

