class WeatherCity:
    def __init__(self, city_name, temperature, humidity, weather_description):
        self.city_name = city_name
        self.temperature = temperature
        self.humidity = humidity
        self.weather_description = weather_description

    def __str__(self):
        return (f"City: {self.city_name}, Temperature: {self.temperature}°C, "
                f"Humidity: {self.humidity}%, Condition: {self.weather_description.capitalize()}")

    def is_hotter_than(self, other):
        return self.temperature > other.temperature