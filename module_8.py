#NB(I am using pymysql library instead of mysql because mysql is crashing in my PyCharm).


#1

import pymysql
connection= pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="166082",
    autocommit=True
)
cursor= connection.cursor()
icao_code= input("Enter the ICAO code of the airport: ").upper().strip()
sql= "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao_code,))
result= cursor.fetchone()
if result:
    airport_name, town= result
    print(f"Airport Name: {airport_name}")
    print(f"Location (Town): {town}")
else:
    print("Airport not found.")
cursor.close()
connection.close()




#2

import pymysql
connection= pymysql.connect(
 host="127.0.0.1",
 port=3306,
 database="flight_game",
 password="166082",
 user="root",
 autocommit=True
)
cursor= connection.cursor()
country_code= input("Enter the country code of the airport(E.g. FI): ").upper()
query = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type"""
cursor.execute(query, (country_code,))
result= cursor.fetchall()
for row in result:
    print(row[0],":",row[1])
cursor.close()
connection.close()