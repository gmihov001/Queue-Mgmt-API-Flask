from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r, %r>' % (self.name, self.number)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number
        }

        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }