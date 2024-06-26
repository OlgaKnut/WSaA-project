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
     
def disconnect():
    global conn
    if conn:
        conn.close()
        conn = None

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
    disconnect()
    return city

def delete_city(id):
    if (not conn):
        connect()
    query = "delete from city where ID = %s"
    cursor=conn.cursor()
    cursor.execute(query,(id))
    conn.commit()
    disconnect()
    return ""

def update_city(id, city):
        if (not conn):
            connect()
        query ="""update city set Name = %s, CountryCode = %s, District = %s, 
                Population = %s  where id = %s"""
        cursor=conn.cursor()
        cursor.execute(query,(city["Name"],city["CountryCode"],city["District"],city["Population"], id))
        conn.commit()
        disconnect()
        return city

def get_cities(firstCityIndex, maxNumber):
    if (not conn):
        connect()
    query="""select city.ID, city.Name, city.District, city.Population, city.CountryCode, country.Name as CountryName
     from city 
     inner join country on country.Code=city.CountryCode
     order by city.Name limit %s, %s"""
    cursor=conn.cursor()
    cursor.execute(query,(firstCityIndex,firstCityIndex + maxNumber))
    disconnect()
    return cursor.fetchall()

def get_countries():
    if (not conn):
        connect()
    query="""select country.Name, country.Code
     from country order by country.Name"""
    cursor=conn.cursor()
    cursor.execute(query)
    disconnect()
    return cursor.fetchall()