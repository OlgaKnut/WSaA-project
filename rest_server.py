import wsaa_mysql_util

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello Cities"

#
# View Cities by ID
#
@app.route('/city/<int:city_id>', methods=['GET'])
def get_city_by_id(city_id):
    cities = wsaa_mysql_util.get_city(city_id)
    for city in cities:
        return jsonify(city)
#
#View all Cities
#
@app.route('/cities', methods=['GET'])
def get_cities():
    cities = wsaa_mysql_util.get_cities()
    return jsonify(cities)

#
#View all Countries
#
@app.route('/countries', methods=['GET'])
def get_countries():
    countries = wsaa_mysql_util.get_countries()
    return jsonify(countries)

#
#View Cities by Countries
#
@app.route('/cities/<country_name>', methods=['GET'])
def get_cities_by_country(country_name):
    cities = wsaa_mysql_util.get_cities_by_country(country_name)
    return jsonify(cities)

#
#add City
#
#curl -X POST --header "Content-Type: application/json" -d "{\"ID\":\"100001\",\"Name\":\"test\", \"CountryCode\":\"USA\",\"District\":\"test\",\"Population\":\"123\", \"Latitude\":\"0\",\"Longitude\":\"0\"}" http://127.0.0.1:5000/cities

@app.route('/cities', methods=['POST'])
def add_city():
     jsonstring = request.json
     city={}
     if "ID" not in jsonstring:
                abort(403)
     city["ID"] = jsonstring["ID"]
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
     if "Latitude" not in jsonstring:
                abort(403)
     city["Latitude"]= jsonstring["Latitude"]
     if "Longitude" not in jsonstring:
                abort(403)
     city["Longitude"]= jsonstring["Longitude"]
     city = wsaa_mysql_util.add_city(city)
     return jsonify(city)



#
#delete City
#
# curl -X DELETE  http://127.0.0.1:5000/cities/100001
@app.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    wsaa_mysql_util.delete_city(id)
    return ""
#
#update City
#
#curl -X PUT --header "Content-Type: application/json" -d "{\"Name\":\"test\", \"CountryCode\":\"USA\",\"District\":\"test\",\"Population\":\"123\", \"Latitude\":\"0\",\"Longitude\":\"0\"}" http://127.0.0.1:5000/cities/100001
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
    if "Latitude" not in jsonstring:
                abort(403)
    city["Latitude"]= jsonstring["Latitude"]
    if "Longitude" not in jsonstring:
                abort(403)
    city["Longitude"]= jsonstring["Longitude"]
    city = wsaa_mysql_util.update_city(id, city)
    return jsonify(city)
  



if __name__ == "__main__":
    app.run(debug = True)