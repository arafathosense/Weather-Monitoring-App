import re

class DataProcessor:
    stored_data = []

    @staticmethod
    def process_weather_data(data):
        if not data or "main" not in data:
            return None
        return {
            "city_name": data.get("name", "Unknown"),
            "temperature": data["main"].get("temp", "N/A"),
            "humidity": data["main"].get("humidity", "N/A"),
            "wind_speed": data["wind"].get("speed", "N/A"),
            "weather_description": data["weather"][0].get("description", "N/A")
        }

    @staticmethod
    def display_info(info):
        print(f"City: {info['city_name']}, "
              f"Temperature: {info['temperature']}°C, "
              f"Humidity: {info['humidity']}%, "
              f"Wind Speed: {info['wind_speed']} m/s, "
              f"Description: {info['weather_description'].capitalize()}")

    @staticmethod
    def store_weather_data(info):
        if len(DataProcessor.stored_data) >= 10:
            print("\nYou have stored weather data for 10 cities.")
            choice = input("Do you want to clear the stored data and start over? (yes/no): ").strip().lower()

            if choice == "yes":
                DataProcessor.stored_data.clear()
                print("Stored data cleared.")
            else:
                print("Oldest entry will be removed to make space.")
                DataProcessor.stored_data.pop(0)

        DataProcessor.stored_data.append(info)

    @staticmethod
    def is_valid_city_name(city):
        """Checks if the city name is valid using regex (letters and spaces only)."""
        return bool(re.match(r'^[A-Za-z ]+$', city))
