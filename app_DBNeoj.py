
from neo4j import GraphDatabase
import sqlite3

# Function to connect to Neo4j
def connect_to_neo4j(uri = "neo4j://localhost:7687", user = "neo4j", password = "neo4jneo4j"):
    return GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"))

# Function to connect to SQLite
def connect_to_sqlite(appDBCity_Neo4j):
    return sqlite3.connect(appDBCity_Neo4j)

# 4.4.6 6 (Show Twinned Cities).Function to retrieve twinned cities from both databases
def get_twinned_cities(neo4j_session, sql_connection):
    # Query Neo4j database for twinned cities
    neo4j_query = """
    MATCH (c:City)-[:TWINS_WITH]->(t:City)
    RETURN c.name AS city1, t.name AS city2
    ORDER BY city1, city2
    """
    with neo4j_session.session() as session:
        result = session.run(neo4j_query)
        twinned_cities = {record['city1']: True for record in result}
    
    # Query SQLite database for additional twinned cities
    sql_query = """
    SELECT city_name FROM twinned_cities
    """
    cursor = sql_connection.cursor()
    cursor.execute(sql_query)
    for record in cursor.fetchall():
        twinned_cities[record[0]] = True

    return sorted(twinned_cities.keys())

# 4.4.7 7 (Twin with Dublin). Function to create a new city and twinned relationship in Neo4j
def create_twinned_relationship(neo4j_session, city_id):
    neo4j_query = """
    MATCH (d:Dublin), (c:City)
    WHERE d.name = 'Dublin' AND c.id = $city_id
    MERGE (d)-[:TWINS_WITH]->(c)
    """
    with neo4j_session.session() as session:
        session.run(neo4j_query, city_id=city_id)

    # SQLite database path
    sqlite_database = "path/to/your/sqlite/database.db"

    # Connect to Neo4j and SQLite
    neo4j_driver = connect_to_neo4j(neo4j_uri ="neo4j://localhost:7687", neo4j_user = "neo4j", neo4j_password = "neo4jneo4j")
    sql_connection = connect_to_sqlite(sqlite_database)

    # Retrieve twinned cities
    twinned_cities = get_twinned_cities(neo4j_driver, sql_connection)

    # Display twinned cities
    print("Twinned cities in alphabetical order:")
    for city in twinned_cities:
        print(city)

    # Prompt user to enter a city ID to twin with Dublin in Neo4j
    city_id = input("Enter the ID of a city to twin with Dublin (if it doesn't exist in Neo4j): ")
    create_twinned_relationship(neo4j_driver, city_id)

    # Close connections
    neo4j_driver.close()
    sql_connection.close()
    