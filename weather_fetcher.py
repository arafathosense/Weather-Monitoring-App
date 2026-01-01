import requests


class WeatherFetcher:
    API_KEY = "2717fc9f2a7c3c777dd4d53f5fb200ba"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city):
        try:
            params = {
                'q': city,
                'appid': WeatherFetcher.API_KEY,
                'units': 'metric'
            }
            response = requests.get(WeatherFetcher.BASE_URL, params=params)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.HTTPError:
            print("City not found or invalid response.")
        except requests.exceptions.ConnectionError:
            print("Network error. Check your internet connection.")
        except requests.exceptions.Timeout:
            print("The request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        return None