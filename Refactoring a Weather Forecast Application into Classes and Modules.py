# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be
# encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as
# fetching data, parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast application is written in a procedural style and
# lacks organization.

# Weather Forecast Application Script

# Fetching Data Class

class WeatherDataFetcher:
    
    def __init__(self, city):
        self.city = city
        self.weather_data = self.weather_data_fetcher()
    
    def weather_data_fetcher(self):

        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})


class WeatherDataParser:

    def __init__(self, data):
        self.data = data
    
    def weather_data_parser(self):

        if not self.data:
            return "Weather data not available"
        
        city = self.data["city"]
        temperature = self.data["temperature"]
        condition = self.data["condition"]
        humidity = self.data["humidity"]
        
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class UserInteraction:

    def __init__(self):
        self.running = True

    def get_detailed_forecast(self, city):

        fetcher = WeatherDataFetcher(city)
        data = fetcher.weather_data_fetcher()
        parser = WeatherDataParser(data)
        return parser.weather_data_parser()

    def display_weather(self, city):

        fetcher = WeatherDataFetcher(city)
        data = fetcher.weather_data_fetcher()
        
        if not data:
            print(f"Weather data not available for {city}")
        else:
            parser = WeatherDataParser(data)
            weather_report = parser.weather_data_parser()
            print(weather_report)


# Main function
def main():
    ui = UserInteraction()

    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        
        if city.lower() == 'exit':
            break
        
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        
        if detailed == 'yes':
            forecast = ui.get_detailed_forecast(city)
        else:
            forecast = ui.display_weather(city)
        
        print(forecast)


if __name__ == "__main__":
    main()
