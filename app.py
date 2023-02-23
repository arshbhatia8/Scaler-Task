from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

@app.route('/people', methods=['GET'])
def get_people():
    people = Person.query.all()
    return jsonify([{'name': person.name, 'email': person.email} for person in people])

@app.route('/people', methods=['POST'])
def add_person():
    name = request.json['name']
    email = request.json['email']
    person = Person(name=name, email=email)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person added successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
