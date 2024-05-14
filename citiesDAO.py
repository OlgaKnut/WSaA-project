
import pymysql

conn = None

def connect():
     global conn
     conn = pymysql.connect( 
        host ='localhost', 
        user ='root',  
        password = "root", 
        database ='appdbproj', 
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
     


def add_city(city):
    if (not conn):
        connect()

    query = """insert into city (Name, CountryCode, District, Population) 
                    values (%s, %s, %s, %s)"""

    cursor=conn.cursor()
    cursor.execute(query,(city["Name"],city["CountryCode"],city["District"],city["Population"]))
    conn.commit()
    newid = cursor.lastrowid
    city["id"] = newid
    return city


def delete_city(id):
    if (not conn):
        connect()
    query = "delete from city where ID = %s"
    cursor=conn.cursor()
    cursor.execute(query,(id))
    conn.commit()
    return ""

def update_city(id, city):
        if (not conn):
            connect()
        query ="""update city set Name = %s, CountryCode = %s, District = %s, 
                Population = %s  where id = %s"""
        
        cursor=conn.cursor()
        cursor.execute(query,(city["Name"],city["CountryCode"],city["District"],city["Population"], id))
        conn.commit()
        return city



def get_cities_by_country(country_name):
    if (not conn):
        connect()

    query="""select country.Name as country_name, 
            city.Name as city_name, city.District, 
            city.Population from country  
            inner join city on country.code=city.countryCode 
            where country.Name like %s order by country.Name, city.Name"""
    
    cursor=conn.cursor()
    cursor.execute(query,(country_name))
    return cursor.fetchall()

def get_cities():
    if (not conn):
        connect()

    query="""select * from city order by Name"""
    
    cursor=conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_total_cities_count():
    
    query=""" SELECT COUNT(*) FROM city"""
    pass

def get_countries():
    if (not conn):
        connect()

    query="""select * from country  
            order by Name"""
    
    cursor=conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_next_batch(cursor, max_records):
    return cursor.fetchmany(max_records)

def get_city(id):
    if (not conn):
        connect()

    query = """select  ID, Name, CountryCode, Population
            from city where ID = %s"""

    cursor=conn.cursor()
    x=cursor.execute(query,(id))
    x=cursor.fetchall()
    return x



def get_country(code):
    if (not conn):
        connect()

    query = """select  Code, Name, Continent, region, SurfaceArea, IndepYear, 
                Population, LifeExpectancy, GNP, LocalName, GovernmentForm, HeadOfState, Capital 
            from country where Code = %s"""

    cursor=conn.cursor()
    x=cursor.execute(query,(code))
    x=cursor.fetchall()
    return x



   
def get_city_name(id):
    if (not conn):
        connect()

    query = "select Name from city where ID= %s"

    cursor=conn.cursor()
    cursor.execute(query,(id))
    x=cursor.fetchall()
    return x


    