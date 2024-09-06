from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)

    users = db.relationship('User', backref='role', lazy='dynamic')

class Permission:
    GENERAL_USER = 1
    PREMIUM = 2
    ADMIN = 4

def create_roles():
    db.session.add(Role(name='User', permissions=Permission.GENERAL_USER))
    db.session.add(Role(name='Premium', permissions=Permission.PREMIUM | Permission.GENERAL_USER))
    db.session.add(Role(name='Admin', permissions=Permission.ADMIN | Permission.PREMIUM | Permission.GENERAL_USER))
    db.session.commit()
