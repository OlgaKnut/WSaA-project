import citiesDAO

from flask import Flask, request, jsonify, abort, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

#
# View Cities by ID
#
#@app.route('/city/<int:city_id>', methods=['GET'])
#def get_city_by_id(city_id):
    #cities = citiesDAO.get_city(city_id)
    #for city in cities:
        #return jsonify(city)
#
#View all Cities
#
@app.route('/cities', methods=['GET'])
def get_cities():
    #cities = citiesDAO.get_cities()
    #return jsonify(cities)
# Pagination parameters
    #page = int(request.args.get('page', 1))
    #per_page = int(request.args.get('per_page', 10))  # Default 10 items per page

    # Calculate offset
    #offset = (page - 1) * per_page

    # Fetch cities for the current page
    cities = citiesDAO.get_cities()
    return jsonify(cities)
    # Get total number of cities for pagination
    #total_cities = citiesDAO.get_total_cities_count()

    # Calculate total number of pages
    #total_pages = (total_cities + per_page - 1) // per_page

    #return render_template('cities.html', cities=cities, page=page, per_page=per_page, total_pages=total_pages)

#
#View all Countries
#
@app.route('/countries', methods=['GET'])
def get_countries():
    countries = citiesDAO.get_countries()
    return jsonify(countries)

#
#View Cities by Countries
#
@app.route('/cities/<country_name>', methods=['GET'])
def get_cities_by_country(country_name):
    cities = citiesDAO.get_cities_by_country(country_name)
    return jsonify(cities)

#
#add City
#
#curl -X POST --header "Content-Type: application/json" -d "{\"ID\":\"100001\",\"Name\":\"test\", \"CountryCode\":\"USA\",\"District\":\"test\",\"Population\":\"123\", \"latitude\":\"0\",\"longitude\":\"0\"}" http://127.0.0.1:5000/cities

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
     city = citiesDAO.add_city(city)
     return jsonify(city)



#
#delete City
#
# curl -X DELETE  http://127.0.0.1:5000/cities/100001
@app.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    citiesDAO.delete_city(id)
    return ""
#
#update City
#
#curl -X PUT --header "Content-Type: application/json" -d "{\"Name\":\"test\", \"CountryCode\":\"USA\",\"District\":\"test\",\"Population\":\"123\", \"latitude\":\"0\",\"longitude\":\"0\"}" http://127.0.0.1:5000/cities/100001
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

@app.route('/cat')
def cat():
    # Assuming your JPEG file is named "example.jpg" and located in the "static" directory
    jpeg_path = url_for('WSaA-project', filename='cat_looking_at_a_globe.jpg')
    return f'The path to the JPEG file is: {jpeg_path}'

if __name__ == "__main__":
    app.run(debug = True)