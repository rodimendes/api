from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    capital = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.capital}'

@app.route('/')
def index():
    return 'Hello!'

@app.route('/api/countries')
def get_countries():
    countries_list = Country.query.all()

    result = []
    for country in countries_list:
        countries_data = {'name': country.name, 'capital': country.capital}

        result.append(countries_data)

    return {'countries': result}

@app.route('/api/countries/<id>')
def get_country(id):
    country = Country.query.get_or_404(id)

    return {'name': country.name, 'capital': country.capital}


@app.route('/api/countries', methods=['POST'])
def add_data():
    country = Country(name=request.json['name'],
                      capital=request.json['capital'])

    db.session.add(country)
    db.session.commit()

    return {'id': country.id}
