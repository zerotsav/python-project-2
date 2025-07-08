import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your own API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp}°C")
    else:
        print("Sorry, I couldn't find the weather for that city.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
