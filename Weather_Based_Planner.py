def weather_day_planner():
    print("Welcome to the Personalized Weather-Based Day Planner!")
    
    while True:
        weather = input("\nWhat's the weather like today? (sunny, rainy, cloudy, snowy, windy): ").strip().lower()
        age = int(input("\nHow old are you? "))
        gender = input("What's your gender? (male, female, non-binary, prefer not to say): ").strip().lower()
        interests = input("What are your interests? ").strip().lower().split(", ")

        plans = {
            "sunny": [
                ("Play pickup basketball or soccer outdoors.", ["sports", "basketball", "soccer", "outdoors"], (10, 40)),
                ("Go on a hiking or biking adventure.", ["hiking", "fitness", "outdoors"], (15, 50)),
                ("Try skateboarding at a local park.", ["sports", "skateboarding", "outdoors"], (10, 30)),
                ("Do a photography tour of nature spots.", ["photography", "outdoors"], (15, 60)),
                ("Host a backyard barbecue with friends.", ["cooking", "social", "relaxation"], (20, 60)),
                ("Visit an amusement park or carnival.", ["adventure", "social", "fun"], (5, 50)),
                ("Practice yoga or meditation in a park.", ["fitness", "relaxation", "mental health"], (18, 70)),
                ("Organize a water balloon fight.", ["fun", "kids", "outdoors"], (5, 12)),
                ("Play mini-golf with family.", ["sports", "fun", "outdoors"], (5, 70)),
                ("Attend an outdoor concert.", ["music", "social", "entertainment"], (20, 50)),
                ("Enjoy a leisurely walk in a botanical garden.", ["relaxation", "outdoors", "nature"], (50, 80))
            ],
            "rainy": [
                ("Read a sports-related book or biography.", ["books", "sports", "learning"], (10, 80)),
                ("Host an indoor D&D or board game night.", ["dnd", "gaming", "social"], (12, 50)),
                ("Try a new recipe or bake homemade bread.", ["cooking", "creativity"], (15, 80)),
                ("Experiment with coding a new project.", ["technology", "coding"], (12, 40)),
                ("Start sketching character designs or comics.", ["art", "creativity"], (8, 50)),
                ("Listen to an inspiring podcast or audiobook.", ["books", "learning", "relaxation"], (15, 80)),
                ("Organize or decorate your living space.", ["creativity", "productivity"], (18, 70)),
                ("Have a cozy movie marathon.", ["movies", "relaxation", "family"], (5, 80)),
                ("Build a pillow fort or engage in indoor hide-and-seek.", ["fun", "kids", "games"], (5, 10))
            ],
            "cloudy": [
                ("Capture stunning photos of the moody atmosphere.", ["photography", "art"], (12, 70)),
                ("Visit a science museum or planetarium.", ["science", "technology", "education"], (8, 70)),
                ("Write poetry, journal, or blog your thoughts.", ["writing", "books", "creativity"], (12, 80)),
                ("Try fashion styling—create new outfits.", ["fashion", "creativity", "self-expression"], (15, 50)),
                ("Work on puzzle-solving or strategy games.", ["gaming", "board games", "logic"], (10, 70)),
                ("Join a local coffee or book club.", ["social", "books", "learning"], (18, 80)),
                ("Visit an art gallery or local museum.", ["art", "culture", "education"], (10, 80)),
                ("Engage in a DIY home improvement project.", ["creativity", "productivity"], (20, 80))
            ],
            "snowy": [
                ("Play hockey or go ice skating.", ["sports", "hockey", "fitness"], (8, 50)),
                ("Sip hot cocoa and read a cozy novel.", ["books", "relaxation"], (5, 80)),
                ("Try skiing or snowboarding.", ["sports", "outdoors"], (10, 50)),
                ("Build an elaborate snow fort or igloo.", ["creativity", "outdoors", "fun"], (5, 80)),
                ("Have a winter-themed movie marathon.", ["movies", "relaxation", "entertainment"], (5, 80)),
                ("Enjoy a playful snowball fight.", ["fun", "kids", "outdoors"], (5, 15)),
                ("Attend a winter festival event.", ["social", "culture", "fun"], (12, 60)),
                ("Create warm indoor crafts while listening to soothing music.", ["creativity", "crafting", "relaxation"], (5, 80))
            ],
            "windy": [
                ("Fly a kite or watch the wind move across landscapes.", ["outdoors", "nature", "fun"], (5, 50)),
                ("Take an invigorating walk.", ["fitness", "relaxation"], (8, 80)),
                ("Explore astrophotography—capture cloud movement.", ["photography", "science"], (12, 60)),
                ("Do indoor yoga or flexibility exercises.", ["fitness", "health"], (15, 70)),
                ("Try competitive chess or strategy-based card games.", ["gaming", "logic"], (10, 70)),
                ("Join an indoor meditation or stretching session.", ["health", "relaxation", "mental health"], (15, 80)),
                ("Visit a local historical site or museum.", ["education", "culture", "learning"], (10, 80)),
                ("Experiment with creative writing or drawing.", ["creativity", "art", "learning"], (12, 80))
            ]
        }

        def rank_activities(weather_activities):
            ranked_activities = []
            for activity, tags, age_range in weather_activities:
                match_score = 0
                # Increase score based on matching interests
                match_score += sum(1 for tag in tags if tag in interests)
                # Adjust score based on age suitability
                if age_range[0] <= age <= age_range[1]:
                    match_score += 2  # bonus for age-appropriate activities
                else:
                    match_score -= 1  # slight penalty if age doesn't match ideally
                ranked_activities.append((activity, match_score))
            ranked_activities.sort(key=lambda x: x[1], reverse=True)
            return ranked_activities

        if weather in plans:
            ranked_list = rank_activities(plans[weather])
            print(f"\nHere are your ranked activity options for today's {weather} weather:")
            for idx, (activity, score) in enumerate(ranked_list, start=1):
                print(f"{idx}. {activity} (Match score: {score})")
        else:
            print("I don't recognize that weather! Please try again.")

        again = input("\nWould you like to plan another day? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the Weather-Based Day Planner. Have a great day!")
            break

weather_day_planner()
