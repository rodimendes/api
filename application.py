from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    capital = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.capital}'

@app.route('/')
def index():
    return 'Hello!'

@app.route('/countries')
def get_countries():
    return {'country': 'country_data'}