from VetLife import db
from .BaseModel import BaseModel


class DosageType(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return self.name
