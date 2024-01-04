import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Use "imperial" for Fahrenheit

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temperature = main_info["temp"]
        humidity = main_info["humidity"]

        print(f"Weather in {city.capitalize()}: {weather_desc}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found. Please check the city name.")

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "30d4741c779ba94c470ca1f63045390a"
    city_name = input("Enter the city name: ")

    get_weather(api_key, city_name)