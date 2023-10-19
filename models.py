"""Models for heard app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Submission(db.Model):
    """Submission model"""

    __tablename__ = 'submissions'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    submission_start = db.Column(db.String,
                                 nullable=False)
    
    prompt_1 = db.Column(db.String)
    prompt_1_resp = db.Column(db.String)
    prompt_2 = db.Column(db.String)
    prompt_2_resp = db.Column(db.String)
    summary = db.Column(db.String)
    
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    # @classmethod
    # def build_submission(cls):