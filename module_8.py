#1

import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="166082",
    autocommit=True
)
cursor = connection.cursor()
icao_code = input("Enter the ICAO code of the airport: ").upper().strip()
query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao_code,))
result = cursor.fetchone()
if result:
    airport_name, town = result
    print(f"Airport Name: {airport_name}")
    print(f"Location (Town): {town}")
else:
    print("Airport not found.")
cursor.close()
connection.close()