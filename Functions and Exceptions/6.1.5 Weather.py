"""
This program will give suggested footwear based on the weather.
"""

weather = input("What is the weather? (sunny, rainy, snowy): ")

def sunny_weather():
    print("On a sunny day, sandals are appropriate footwear.")

def rainy_weather():
    print("On a rainy day, galoshes are appropriate footwear.")
    
def snowy_weather():
    print("On a snowy day, boots are appropriate footwear.")
    
if weather.lower() == "sunny":
    sunny_weather()
elif weather.lower() == "rainy":
    rainy_weather()
elif weather.lower() == "snowy":
    snowy_weather()
