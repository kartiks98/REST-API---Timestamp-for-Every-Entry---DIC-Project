from db import db


class NameModel(db.Model):
    __tablename__ = 'names_timestamps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    timestamp = db.Column(db.String(80))

    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp

    def json(self):
        return {'id': self.id, 'name': self.name, 'timestamp': self.timestamp}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.order_by(cls.id.desc()).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
