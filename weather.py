import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad response

        data = response.json()

        print("\n🌦 Weather Forecast")
        print(f"City: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError as err:
        print(" HTTP Error:", err)
    except requests.exceptions.RequestException as err:
        print(" Request Failed:", err)
    except KeyError:
        print("City not found or missing data.")
    except Exception as err:
        print(" An error occurred:", err)

if __name__ == "__main__":
    print("===  Weather Forecast App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    city = input("Enter city name: ").strip()

    if not api_key or not city:
        print(" API key and city name are required.")
    else:
        get_weather(city, api_key)
