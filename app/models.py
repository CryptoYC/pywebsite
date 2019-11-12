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

    def to_json(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'risk': self.risk,
            'url': self.url,
            'content': self.content,
            'report_time': self.report_time
        }

@dataclass
class Contact(db.Model):
    """
    Model for Report.
    """
    id: int
    name: str
    mail: str
    content: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    mail = db.Column(db.String(150))
    content = db.Column(db.Text)

@dataclass
class Project(db.Model):
    """
    Model for Project.
    """
    id: int
    name:str
    website:str
    doc_addr:str
    submitter:str
    contact:str
    github:str
    mail:str
    remark:str
    attachment:str

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    website= db.Column(db.String(150))
    doc_addr= db.Column(db.String(150))
    submitter= db.Column(db.String(50))
    contact= db.Column(db.String(150))
    github= db.Column(db.String(150))
    mail= db.Column(db.String(150))
    remark= db.Column(db.String(200))
    attachment= db.Column(db.Text)
