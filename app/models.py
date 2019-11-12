from dataclasses import dataclass
from . import db
import datetime


@dataclass
class Report(db.Model):
    """
    Model for Report.
    """
    id: int
    rating: str
    risk: str
    url: str
    content: str
    report_time: datetime

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    rating = db.Column(db.String(1))
    risk = db.Column(db.String(1))
    url = db.Column(db.Text)
    content = db.Column(db.Text)
    report_time = db.Column(db.DateTime)

    def __json__(self):
        return ['id', 'rating', 'risk', 'url', 'content', 'report_time']
