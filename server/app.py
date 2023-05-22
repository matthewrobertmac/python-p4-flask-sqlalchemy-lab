#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)



@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response 
    
    response_body = f'''
        <h1> Information for {animal.name}</h1>
        <h2>Animal Species is {animal.species}</h2>
        <h2>Animal Zookeeper is {animal.zookeeper}</h2>
        <h2>Animal Enclosure is {animal.enclosure}</h2>
    '''
    response = make_response(response_body, 200) 
    
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first() 

    if not zookeeper:
        response_body = '<h1>404 zookeeper not found</h1>'
        response = make_response(response_body, 404) 
        return response 
    
    response_body = f'''
        <h1>Information for {zookeeper.name} 
        <h2>Zookeeper Birthday is {zookeeper.birthday}</h2>
        <h2>Zookeeper Animals are {zookeeper.animals}</h2>
    
'''
    response = make_response(response_body, 200) 

    return response 

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    if not enclosure: 
        response_body = '<h1>404 enclosure not found</h1>' 
        response = make_response(response_body, 404) 
        return response 
    
    response_body = f'''
        <h1>Information for {enclosure.name}</h2>
        <h2>Enclosure Environment is {enclosure.environment}</h2>
        <h2>Enclosure Open to Visitors: {enclosure.open_to_visitors}
        <h3>Enclosure animals are: {enclosure.animals}</h3>
    '''
    response = make_response(response_body, 200) 

    return response 


if __name__ == '__main__':
    app.run(port=5555, debug=True)

"""
Your database should represent a zoo. There should be three tables: animals, zookeepers, and enclosures.
The Animal model should contain a name, a species, a zookeeper, and an enclosure.
The Zookeeper model should contain a name, a birthday, and a list of animals that they take care of.
The Enclosure model should contain an environment (grass, sand, or water), an open_to_visitors boolean, and a list of animals.
Your application should contain three views: animal_by_id, zookeeper_by_id, and enclosure_by_id. Their routes should be animal/<int:id>, zookeeper/<int:id>, and enclosure/<int:id>, respectively.
Each view should display all attributes as line items (ul). If there is a one-to-many relationship, each of the many should have its own line item.
A seed script, server/seed.py, has been provided to generate test data once your models have been built and migrated to a database. Make sure to run this so that there are resources for the test suite to visit.

"""