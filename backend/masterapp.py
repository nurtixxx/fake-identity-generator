from flask import Flask, jsonify
from faker import Faker

app = Flask(__name__)
faker = Faker()

def generate_fake_identity():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "address": faker.address()
    }

@app.route('/api/fake')
def get_fake_data():
    return jsonify(generate_fake_identity())

