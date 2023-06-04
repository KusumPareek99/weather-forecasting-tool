#create a function to fetch weather which takes city_name as parameter and uses openweathermap api to fetch weather data
import requests
import config


def fetch_weather(city_name):
    #openweathermap api url
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+config.api_key
    #print(url)
    #fetching data from api
    response = requests.get(url)
    #converting data to json format
    data = response.json()
    #returning data
    return data    

#using the fetch_weather function to fetch weather data for the city display the weather data in the format mentioned in the problem statement
def display_weather(city_name):
    #fetching weather data
    data = fetch_weather(city_name)
    #checking if data is fetched successfully
    if data['cod'] == 200:
        #fetching temperature from data
        temperature = data['main']['temp']
        #fetching weather description from data
        weather_description = data['weather'][0]['description']
        #fetching wind speed from data
        wind_speed = data['wind']['speed']
        #fetching humidity from data
        humidity = data['main']['humidity']
        #fetching pressure from data
        pressure = data['main']['pressure']
        #fetching latitude from data
        latitude = data['coord']['lat']
        #fetching longitude from data
        longitude = data['coord']['lon']
        #printing weather data
        print("Temperature: " + str(temperature))
        print("Weather Description: " + str(weather_description))
        print("Wind Speed: " + str(wind_speed))
        print("Humidity: " + str(humidity))
        print("Pressure: " + str(pressure))
        print("Latitude: " + str(latitude))
        print("Longitude: " + str(longitude))
    else:
        #printing error message
        print("Error: " + str(data['cod']) + " " + str(data['message']))

#if name is main then call the display_weather function
if __name__ == "__main__":
    #taking city name as input
    city_name = input("Enter city name: ")
    #calling display_weather function
    display_weather(city_name)