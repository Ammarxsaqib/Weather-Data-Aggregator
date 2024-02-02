import os
import requests

def get_weather_data(api_key, latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temp_kelvin = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_condition = weather_data['weather'][0]['description']
        temp_celsius = temp_kelvin - 273.15

        print(f'Temperature: {temp_celsius:.2f} °C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Weather Condition: {weather_condition}')
    else:
        print(f'Failed to retrieve data. Status Code: {response.status_code}')

if __name__ == "__main__":

    api_key = os.getenv('a23b4ffafefe3fd2f4fdaadc63c86c34', 'a23b4ffafefe3fd2f4fdaadc63c86c34')
    #Coordinates of Islamabad
    latitude = 33.6844    #40.7128  New York
    longitude = 73.0479   #74.0060   New york

    get_weather_data(api_key, latitude, longitude)
