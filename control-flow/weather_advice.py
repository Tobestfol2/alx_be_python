# This script asks for the weather and gives clothing advice using if/elif/else statements.

# Prompt the user to input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Check the weather and provide a recommendation
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")