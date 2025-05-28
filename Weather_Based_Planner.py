def weather_day_planner():
    print("Welcome to the Weather-Based Day Planner!")
    weather = input("What's the weather like today? (sunny, rainy, cloudy, snowy, windy): ").strip().lower()

    plans = {
        "sunny": [
            "Perfect day for a picnic or hiking.",
            "How about surfing or beach volleyball?",
            "Maybe a nature walk or biking adventure."
        ],
        "rainy": [
            "A cozy day for reading books by the window.",
            "Grab a warm drink at a coffee shop.",
            "Movie marathon time—bring out the popcorn."
        ],
        "cloudy": [
            "Great for photography—moody aesthetics.",
            "Visit a museum or art gallery.",
            "Time to journal or try a creative project."
        ],
        "snowy": [
            "Build a snowman or have a snowball fight.",
            "Hot cocoa and blankets—it’s cozy season.",
            "Try skiing or ice skating."
        ],
        "windy": [
            "Fly a kite or watch the breeze dance.",
            "Try outdoor yoga or meditation in the wind.",
            "Indoor gaming—board games or puzzles."
        ]
    }

    if weather in plans:
        print("\nHere are some fun options for today's weather:")
        for activity in plans[weather]:
            print("- " + activity)
    else:
        print("I don't recognize that weather! Try again.")

weather_day_planner()