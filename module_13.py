#a) Exercise-1

from flask import Flask, Response
import json

# function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# API route
app = Flask(__name__)

@app.route('/prime_number/<int:number>')
def prime_number(number):
    result = {
        "Number": number,
        "is Prime": is_prime(number)
    }

    return Response(json.dumps(result), mimetype='application/json')

# Run server
if __name__ == "__main__":
    app.run(debug=False, use_reloader=True, host='127.0.0.1', port=5000)




#b) Exercise-2

from flask import Flask, Response
import pymysql
import json

# Database connection
def get_connection():
    return pymysql.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="166082",
        autocommit=True
    )

# API route
app = Flask(__name__)

@app.route('/airport/<icao>')
def get_airport(icao):
    connection = get_connection()
    cursor = connection.cursor()

    query = "Select name, municipality From airport Where ident = %s"
    cursor.execute(query, (icao.upper(),))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        data = {
            "ICAO": icao.upper(),
            "Name": result[0],
            "Location": result[1]
        }
    else:
        data = {
            "error": "Airport not found"
        }

    return Response(json.dumps(data), mimetype='application/json')

# Run server
if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host='127.0.0.1', port=5000)