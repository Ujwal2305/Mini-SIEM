from app import db
from datetime import datetime

# ---------------------------
# USER MODEL
# ---------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin / analyst


# ---------------------------
# LOGIN AUDIT LOG MODEL
# ---------------------------
class LoginLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    status = db.Column(db.String(20))  # success / failed
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)