import app_sqlDB
import app_DBNeoj

def main():
    display_menu()
    while True:
        choice = input("Enter your choice: ")
        
        # 4.4.1 1 (View Cities by Country)
        if (choice == '1'):
            #The user is asked to enter a country name
            countryName = input("Enter Country name: ")
            # The user is then shown the following details of cities in that country/those countries:
            countries = app_sqlDB.city_by_country(countryName)
            for countryName in countries:
                print(countryName["Country Name"],"|",["City Name"],"|",["City Distrinct"],"|",["city Population"])
            # If the user presses any key except q the details of the next 2 cities in that country/those countries are shown.
            # Whenever the user presses q he/she is returned to the Main Menu
            next_action = input("Press any key to continue or 'q'")
            if next_action.lower() == 'q':
              continue
            
         # 4.4.2 2 (Update City Population)   
        elif (choice == '2'):
            # The user is asked to enter a City ID:
            cityID = input("Enter city ID: ")
            # When a valid City ID is entered the following details of the city are shown:
            cities = app_sqlDB.find_cityID(cityID)
            for cityID in cities:
                print(cityID["ID"],"|",["Name"],"|",["CountryCode"],"|",["Population"],"|",["latitude"],"|",["longitude"])
            # The user is then asked whether he/she wishes to Increase or Decrease the City’s Population, and by how much.
            inc_dec_population = input("[I]crease/[D]ecrease Population: ")
            how_much_pop = input("Enter Population Decrease: ")
            print(inc_dec_population)
            print(how_much_pop)
            
         # 4.4.3 3 (Add New Person)   
        elif (choice == '3'):
            # The user is asked to enter the following details for a Person:
            personID = input("Add New Person\nID: ")
            personname = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = input("Enter salary: ")
            city = input("Enter City: ")
            app_sqlDB.add_person(personID, personname, age, salary, city)
            display_menu()
            
        # 4.4.4 4 (Delete Person)
        elif (choice == '4'):
            # The user is asked to enter the ID of the person to be deleted.
            id_per = input("Enter ID of person to Delete: ")
            app_sqlDB.del_person(id_per)
            # This person is then deleted from the database, and the user returned to the main menu.
            display_menu()
            
        # 4.4.5 5 (View Countries by population)
        elif (choice == '5'):
            # The user is asked to enter <, > or =, followed by a population. 
            put_sign = input (" Enter < > or = :")
            print(put_sign)
            #For any country whose population is <, > or = (as appropriate) the population entered by the user, the following information is shown:
            put_pop = input("Enter population: ")
            popul = app_sqlDB.country_by_pop(put_sign, put_pop)
            for put_pop in popul:
                print(put_pop["Code"],"|",["Name"],"|",["Continent"],"|",["Population"])
        ###########    NEO4J
        #4.4.6 6 (Show Twinned Cities)
        # When this option is chosen, the list of twinned cities (from the Neo4j database) is shown in alphabetical order
        elif (choice == '6'):
            tw = input ("Enter choice: ")
            print(tw)
            app_DBNeoj.get_twinned_cities(tw)
            
        #4.4.7 7 (Twin with Dublin)
        elif (choice == '7'):
            #The user is asked to enter the ID of a city to be twinned with Dublin in the Neo4j database
            twDublin = input("Enter city ID: ")
            print (twDublin)
            app_DBNeoj.create_twinned_relationship(twDublin)
        # 4.4.8 x (Exit Application)   
        elif (choice == 'x'):
            print("Exit")
            break
        # 4.4.9 Anything Else
        else:
            break
            # print("Invalid choice. Please enter")


def display_menu():
    print("====================")
    print("       MENU         ")
    print("====================")
    print("")
    print("1 - View Cities by Country")
    print("2 - Update City Population")
    print("3 - Add New Person")
    print("4 - Delete Person")
    print("5 - View Countries by population")
    print("6 - Show Twinned Cities")
    print("7 - Twin with Dublin")
    print("x - Exit application")

            

if __name__ == "__main__":
    main()