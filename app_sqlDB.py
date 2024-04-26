import pymysql

# 4.4.1 1 (View Cities by Country)
def city_by_country(countryName):
    db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "appdbproj", cursorclass=pymysql.cursors.DictCursor)
    sql = "select co.Name, c.Name, c.District, c.Population from city as c join country as co on c.CountryCode = co.Code"
    with db:
        cursor = db.cursor()
        cursor.execute(sql, (countryName))
        return cursor.fetchall()


#4.4.2 2 (Update City Population)
def find_cityID(cityID):
    db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "appdbproj", cursorclass=pymysql.cursors.DictCursor)
    sql = "select ID, Name, CountryCode, Population, latitude, longitude from city"
    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (cityID))
            return cursor.fetchall()
        # 4.4.3.1 Error Conditions
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.IntegrnalError as e:
            print(e)
        except Exception as e:
            print(e)    



# .4.3 3 (Add New Person)
def add_person(personID, personname, age, salary, city):
    db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "appdbproj", cursorclass=pymysql.cursors.DictCursor)
    sql = "INSERT INTO person  VALUES(%s, %s, %s, %s, %s)"
    
    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (personID, personname, age, salary, city))
            db.commit()
            # 4.4.3.1 Error Conditions
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.IntegrnalError as e:
            print(e)
        except Exception as e:
            print(e)
            
# 4.4.4 4 (Delete Person)
def del_person(id_per):
    db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "appdbproj", cursorclass=pymysql.cursors.DictCursor)
    sql = "DELETE FROM person  WHERE personID = %s"
    
    with db:
        try: 
            cursor = db.cursor()
            cursor.execute(sql, (id_per))
            db.commit()
        # 4.4.4.1 Error Conditions
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.IntegrnalError as e:
            print(e)
        except Exception as e:
            print(e)
            
# 4.4.5 5 (View Countries by population)
def country_by_pop(put_pop):
    db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "appdbproj", cursorclass=pymysql.cursors.DictCursor)
    sql = "select Code, Name, Continent, Population from country"   
    
    with db:
        try: 
            cursor = db.cursor()
            cursor.execute(sql, (put_pop))
            db.commit()
    #4.4.5.1 Error Conditions
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.IntegrnalError as e:
            print(e)
        except Exception as e:
            print(e)    
            
 
            
