from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tabelname__ = 'facts'
    
    id = db.Column(db.Integer, primary_key=True)
    submiter = db.Column(db.String(255))
    fact = db.Column(db.Text)