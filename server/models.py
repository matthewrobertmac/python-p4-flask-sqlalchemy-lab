from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.String(100), unique=False, nullable=False)
    animals = db.Column(db.String(80), unique = False, nullable=False)


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    animals = db.Column(db.String(80), unique=True, nullable=False)


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    species = db.Column(db.String(80), unique=True, nullable=False)
    enclosure = db.Column(db.String(80), unique=True, nullable=False)


"""
class Animal(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    species = db.Column(db.String(80), unique=True, nullable=False)
    enclosure = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name 

class Zookeeper(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.Integer(10), unique=False, nullable=False)
    animals = db.Column(db.String(80), unique = False, nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name
    
class Enclosure(db.Model):
    environment = db.relationship('grass', 'sand', 'water') 
    open_to_visitors = db.Column(db.Bool, nullable=False)
    animals = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name 

"""