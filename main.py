from weather_fetcher import WeatherFetcher
from data_processor import DataProcessor
from weather_objects import WeatherCity

def main():
    print("🌦️ Weather Monitoring App")

    city_objects = []

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == 'exit':
            break

        if not DataProcessor.is_valid_city_name(city):
            print("❌ Invalid city name. Use only letters and spaces.")
            continue

        data = WeatherFetcher.get_weather(city)
        if not data:
            print("⚠️ Could not fetch data. Please try again.")
            continue

        weather_info = DataProcessor.process_weather_data(data)
        if weather_info:
            # Display and store data
            DataProcessor.display_info(weather_info)
            DataProcessor.store_weather_data(weather_info)

            city_obj = WeatherCity(
                city_name=weather_info["city_name"],
                temperature=weather_info["temperature"],
                humidity=weather_info["humidity"],
                weather_description=weather_info["weather_description"]
            )
            city_objects.append(city_obj)

        else:
            print("⚠️ Failed to process weather data.")

    # After exiting the loop
    if city_objects:
        print("\n📊 Sorted Weather Data (by Temperature - High to Low):\n")
        sorted_cities = sorted(city_objects, key=lambda c: c.temperature, reverse=True)
        for city in sorted_cities:
            print(city)

        hottest = sorted_cities[0]
        print(f"\n🔥 The hottest city is: {hottest.city_name} with a temperature of {hottest.temperature}°C.")

    print("\n👋 Thanks for using the Weather App!")

if __name__ == "__main__":
    main()
