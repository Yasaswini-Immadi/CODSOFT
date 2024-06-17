# Movie database
dataset = {
    "action": {
        "english": ["The BeeKeeper", "Die Hart the movie", " House"],
        "hindi": ["Ek Tha Tiger", "War", "Mission Majnu"],
        "telugu": ["Operation Valentine", "Major", "Guntur Kaaram"],
        "korean": ["The K2", "My Name", "Vegabond"],
        "thai": ["The Sign", "Kinnporsche", "Wolf"]

    },
    "comedy": {
        "thai": ["We are", "oh my boss!", "F4:Thailand"],
        "hindi": ["3 idiots","Bhool Bhulaiyaa","HouseFull"],
        "telugu": ["Dj Tillu", "F2:Fun and Frustration", "Jaatiratnalu"],
        "korean": ["Business proposal", "Business Proposal", "Welcome to wakiwaki"],
        "english": ["The hangover", "Bridesmaids", "Ted"]
    },
    "thriller": {
        "english": ["Shutter Island", "Phone booth", "The girl with the dragon"],
        "telugu": ["Hit", "Gentleman", "Oka Kshanam"],
        "hindi": ["Hotel Mumbai", "Neerja", "A Thursday"],
        "korean": ["The train", "Tell me what you saw", "Squid Game","Mouse"],
        "thai": ["Enigma", "Manner of Death", "Kemjira The series"]
    },
    "horror": {
        "english": ["The Boy", "The Curse of la Llorona", "Smile"],
        "hindi": ["Chhorii", "Pari", "Bhoot:The Haunted Ship"],
        "telugu": ["Pindam", "Virupaksha", "Diya","U Turn"],
        "korean": ["Parasyte", "The Wailing", "Exhuma","Velma"],
        "thai": ["God bless you from death", "The promise", "The devil's Whishperer"]
    }

}

# Ask for genre and language
genre = input("Enter genre (action, comedy, thriller, horror ): ").lower()
language = input("Enter language (english, hindi, telugu, korean, thai): ").lower()

# Check if genre and language are valid
if genre in dataset and language in dataset[genre]:
    recommended_movies = dataset[genre][language]
    print("Here are a list of movies in ",genre," genre in ",language,":\n")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("Sorry, no movies found for the selected genre and language.")
