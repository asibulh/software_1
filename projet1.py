import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="166082",
    database="flight_game",
    port=3306
)

cursor = connection.cursor()

icao = input("Enter ICAO code: ").upper().strip()

query = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor.execute(query, (icao,))

result = cursor.fetchone()

if result:
    print("Airport:", result[0])
    print("City:", result[1])
else:
    print("Not found")

cursor.close()
connection.close()