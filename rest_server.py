import citiesDAO

from flask import Flask, request, jsonify, abort, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')


#
#View all Countries
#
@app.route('/countries', methods=['GET'])
def get_countries():
    countries = citiesDAO.get_countries()
    return jsonify(countries)
    
#
#View all Cities
#
@app.route('/cities/<int:firstCityIndex>/<int:maxNumber>', methods=['GET'])
def get_cities(firstCityIndex, maxNumber):
    cities = citiesDAO.get_cities(firstCityIndex, maxNumber)
    return jsonify(cities)

#
#add City
#

@app.route('/cities', methods=['POST'])
def add_city():
     jsonstring = request.json
     city={}
     
     if "Name" not in jsonstring:
                abort(403)
     city["Name"]= jsonstring["Name"]
     if "CountryCode" not in jsonstring:
                abort(403)
     city["CountryCode"]= jsonstring["CountryCode"]
     if "District" not in jsonstring:
                abort(403)
     city["District"]= jsonstring["District"]
     if "Population" not in jsonstring:
                abort(403)
     city["Population"]= jsonstring["Population"]
     city = citiesDAO.add_city(city)
     return jsonify(city)

#
#delete City
#
@app.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    citiesDAO.delete_city(id)
    city={}
    city["ID"]=id
    return jsonify(city)
#
#update City
#
@app.route('/cities/<int:id>', methods=['PUT'])
def update_city(id):
    jsonstring = request.json
    city={}
    
    city["ID"] = id
    if "Name" not in jsonstring:
                abort(403)
    city["Name"]= jsonstring["Name"]
    if "CountryCode" not in jsonstring:
                abort(403)
    city["CountryCode"]= jsonstring["CountryCode"]
    if "District" not in jsonstring:
                abort(403)
    city["District"]= jsonstring["District"]
    if "Population" not in jsonstring:
                abort(403)
    city["Population"]= jsonstring["Population"]
    city = citiesDAO.update_city(id, city)
    return jsonify(city)


if __name__ == "__main__":
    app.run(debug = True)