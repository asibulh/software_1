#1

import requests

# API URL
url = "https://api.chucknorris.io/jokes/random"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print only the joke text
print(data["value"])



#2

import requests

def get_weather():
    # My API key
    api_key = "c7f9f8809ed455227199e1cde1e80c11"

    city = input("Enter the name of a municipality: ")

    #URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)

        # Check....if city is wrong

        if response.status_code == 404:
            print("Municipality not found. Please check the spelling.")
            return

        # Other errors

        response.raise_for_status()
        data = response.json()

        # Get weather info
        description = data['weather'][0]['description']
        temp = data['main']['temp']

        print("\nCurrent weather in", city.capitalize() + ":")
        print("Condition:", description)
        print("Temperature:", temp, "°C")

    except requests.exceptions.RequestException as e:
        print("Connection error:", e)

if __name__ == "__main__":
    get_weather()