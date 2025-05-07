# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:

    celsius = 30 # static variable 

    @staticmethod
    def convert_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
print(f'Temperature in Fahrenheit : {TemperatureConverter.convert_to_fahrenheit(TemperatureConverter.celsius)}')
