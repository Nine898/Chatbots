def weather_day_planner():
    print("Welcome to the Personalized Weather-Based Day Planner!")
    
    weather = input("What's the weather like today? (sunny, rainy, cloudy, snowy, windy): ").strip().lower()
    age = int(input("How old are you? "))
    gender = input("What's your gender? (male, female, non-binary, prefer not to say): ").strip().lower()
    interests = input("What are your interests? (e.g., sports, books, music, photography, gaming, cooking, fashion, hiking, coding, board games): ").strip().lower().split(", ")

    plans = {
        "sunny": [
            ("Play pickup basketball or soccer outdoors.", ["sports", "basketball", "soccer"]),
            ("Go on a hiking or biking adventure.", ["outdoors", "hiking", "fitness"]),
            ("Try skateboarding at a local park.", ["sports", "skateboarding", "outdoors"]),
            ("Do a photography tour of nature spots.", ["photography", "outdoors"]),
            ("Test out drone flying in an open field.", ["technology", "outdoors", "photography"]),
            ("Host a backyard barbecue with friends.", ["cooking", "social", "relaxation"])
        ],
        "rainy": [
            ("Dive into a sports-related book or biography.", ["books", "sports"]),
            ("Host an indoor D&D or board game night.", ["DnD", "gaming", "social"]),
            ("Watch classic sports documentaries or game replays.", ["sports", "movies"]),
            ("Try a new recipe or bake homemade bread.", ["cooking", "creativity"]),
            ("Experiment with coding a new project.", ["technology", "coding"]),
            ("Start sketching character designs or comics.", ["art", "creativity"])
        ],
        "cloudy": [
            ("Capture stunning photos of the moody atmosphere.", ["photography", "art"]),
            ("Visit a science museum or planetarium.", ["science", "technology", "education"]),
            ("Write poetry, journal, or blog your thoughts.", ["writing", "books", "creativity"]),
            ("Try fashion styling—create new outfits.", ["fashion", "creativity"]),
            ("Work on puzzle-solving or strategy games.", ["gaming", "board games", "logic"])
        ],
        "snowy": [
            ("Play a friendly hockey or ice skating game.", ["sports", "hockey", "fitness"]),
            ("Sip hot cocoa and read a cozy novel.", ["books", "relaxation"]),
            ("Try skiing or snowboarding at a nearby resort.", ["sports", "outdoors"]),
            ("Build an elaborate snow fort or igloo.", ["creativity", "outdoors", "fun"]),
            ("Have a nostalgic retro gaming day indoors.", ["gaming", "social"])
        ],
        "windy": [
            ("Fly a kite or watch the wind move across landscapes.", ["outdoors", "nature"]),
            ("Take an invigorating walk in the fresh air.", ["fitness", "relaxation"]),
            ("Explore astrophotography—capture cloud movement.", ["photography", "science"]),
            ("Indoor yoga or flexibility exercises.", ["fitness", "health"]),
            ("Try competitive chess or strategy-based card games.", ["gaming", "logic"])
        ]
    }

    def rank_activities(weather_activities):
        ranked_activities = []
        for activity, tags in weather_activities:
            match_score = sum(1 for tag in tags if tag in interests)
            ranked_activities.append((activity, match_score))
        
        # Sort activities by match score, highest first
        ranked_activities.sort(key=lambda x: x[1], reverse=True)
        return ranked_activities

    if weather in plans:
        ranked_list = rank_activities(plans[weather])

        print(f"\nHere are your ranked activity options for today's {weather} weather:")
        for idx, (activity, score) in enumerate(ranked_list, start=1):
            print(f"{idx}. {activity} (Match score: {score})")
    else:
        print("I don't recognize that weather! Try again.")

weather_day_planner()
