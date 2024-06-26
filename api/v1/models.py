from api.v1 import db
from datetime import datetime
from datetime import timezone


class Task(db.Model):
    __tablename__ = 'tasks'

    def current_datetime_utc():
        """Returns the current datetime in UTC timezone"""
        return datetime.now(timezone.utc)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date)
    status = db.Column(db.String, nullable=False, default="pending")
    priority = db.Column(db.String, nullable=False, default='medium')
    created_at = db.Column(db.DateTime, default=current_datetime_utc)
    updated_at = db.Column(db.DateTime, default=current_datetime_utc, onupdate=current_datetime_utc)

    def __repr__(self):
        _id = self.id
        t = self.title,
        d = self.description
        dd = self.due_date
        s = self.status
        p = self.priority
        c = self.created_at
        u = self.updated_at
        return f"Task('{_id}', '{t}', '{d}', '{dd}', '{s}', '{p}', '{c}', '{u}')"

    def to_dict(self):
        """Makes a dictionary of a task"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': datetime.strftime(self.due_date, '%Y-%m-%d'),
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
