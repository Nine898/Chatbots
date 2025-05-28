def weather_day_planner():
    print("Welcome to the Personalized Weather-Based Day Planner!")
    
    weather = input("What's the weather like today? (sunny, rainy, cloudy, snowy, windy): ").strip().lower()
    age = int(input("How old are you? "))
    gender = input("What's your gender? (male, female, non-binary, prefer not to say): ").strip().lower()
    interests = input("What are your interests? (e.g., sports, books, music, photography, gaming): ").strip().lower().split(", ")

    plans = {
        "sunny": [
            "Enjoy a picnic or a scenic nature walk.",
            "Hit the beach for volleyball or surfing.",
            "Outdoor yoga or meditation for a peaceful day.",
            "Explore a botanical garden or visit a national park."
        ],
        "rainy": [
            "Curl up with a book and a cup of tea.",
            "Spend time at a cozy café or bakery.",
            "Try painting or a DIY craft indoors.",
            "Have a movie marathon with homemade popcorn."
        ],
        "cloudy": [
            "Capture stunning photos of the moody weather.",
            "Visit a museum, planetarium, or art exhibit.",
            "Write poetry, journal, or create a music playlist.",
            "Go thrift shopping or explore an antique shop."
        ],
        "snowy": [
            "Build a snow fort or have a snowball fight.",
            "Enjoy hot cocoa while watching a classic film.",
            "Try skiing, sledding, or snowboarding.",
            "Host a cozy indoor game night with friends."
        ],
        "windy": [
            "Fly a kite or watch the leaves dance in the breeze.",
            "Take an invigorating walk in the fresh air.",
            "Do an indoor workout session or yoga practice.",
            "Try strategy board games or puzzles with family."
        ]
    }

    # Customize suggestions based on age
    if age < 18:
        plans["sunny"].append("Visit a local amusement park or playground.")
        plans["rainy"].append("Have a fun indoor scavenger hunt.")
        plans["snowy"].append("Make snow angels and enjoy warm cookies.")
    
    if age >= 18 and age <= 30:
        plans["cloudy"].append("Join a creative writing or poetry event.")
        plans["windy"].append("Try windsurfing or an outdoor obstacle course.")
    
    if age > 30:
        plans["sunny"].append("Take a relaxing walk at a nearby lake or forest.")
        plans["rainy"].append("Enjoy a quiet evening with a classic novel.")
        plans["cloudy"].append("Attend a photography or art workshop.")

    # Customize suggestions based on gender (optional ideas)
    if gender == "female":
        plans["rainy"].append("Try a DIY spa day at home.")
    
    if gender == "male":
        plans["sunny"].append("Go fishing or enjoy an outdoor barbecue.")
    
    # Customize suggestions based on interests
    if "sports" in interests:
        plans["sunny"].append("Join a game of soccer or basketball with friends.")
        plans["snowy"].append("Try ice hockey or snowboarding.")

    if "books" in interests:
        plans["rainy"].append("Visit a bookstore or library for inspiration.")
        plans["cloudy"].append("Write a short story or start a book club.")

    if "music" in interests:
        plans["windy"].append("Play an instrument or create a new playlist.")
        plans["rainy"].append("Discover new artists and explore different genres.")

    if "photography" in interests:
        plans["sunny"].append("Capture golden hour or nature shots.")
        plans["cloudy"].append("Experiment with black-and-white photography.")

    if "gaming" in interests:
        plans["rainy"].append("Host an online multiplayer gaming session.")
        plans["cloudy"].append("Try a new strategy or adventure game.")

    if weather in plans:
        print("\nHere are some personalized options based on today's weather and your preferences:")
        for activity in plans[weather]:
            print("- " + activity)
    else:
        print("I don't recognize that weather! Try again.")

weather_day_planner()
