from reminder.database import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())