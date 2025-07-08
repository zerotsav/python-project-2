import random
from datetime import datetime

print("Yo! I'm Utsav 🤖 — your chat buddy. Just type and let's vibe. (Type 'bye' to bounce)")

while True:
    user_input = input("You: ").lower()

    if any(greet in user_input for greet in ["hello", "hi", "hey", "yo", "sup"]):
        print("Utsav: Hey hey! What’s poppin’? 😎")

    elif "how are you" in user_input:
        print("Utsav: I'm chillin', thanks for asking! You good?")

    elif "your name" in user_input or "who are you" in user_input:
        print("Utsav: I'm Utsav — part bot, part buddy.")

    elif "joke" in user_input or "make me laugh" in user_input:
        jokes = [
            "Why don't programmers like nature? Too many bugs 🐛.",
            "Why did the computer go to therapy? It had too many tabs open.",
            "Debugging: Being the detective in a crime movie where you are also the murderer 💀.",
            "Why do Java developers wear glasses? Because they don't C#! 😂"
        ]
        print("Utsav: " + random.choice(jokes))

    elif "date" in user_input or "time" in user_input:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Utsav: It's {now} right now. Time flies, huh?")

    elif "food" in user_input or "hungry" in user_input:
        print("Utsav: I can't eat, but if I could — pizza all day 🍕. What's your go-to?")

    elif "quote" in user_input or "inspire me" in user_input:
        quotes = [
            "Keep going. Everything you need will come to you at the perfect time.",
            "You're doing better than you think. Trust the process. 💪",
            "Success is just a bunch of small wins stacked up.",
            "You don't have to be extreme, just consistent."
        ]
        print("Utsav: " + random.choice(quotes))

    elif "sad" in user_input or "not okay" in user_input:
        print("Utsav: I'm sorry you're feeling that way. I'm here for you. Wanna talk about it?")

    elif "bored" in user_input:
        print("Utsav: Wanna hear a fun fact? Or maybe play rock-paper-scissors? 😁")

    elif "fun fact" in user_input:
        facts = [
            "Bananas are berries, but strawberries aren’t. 🍓🍌",
            "A group of flamingos is called a flamboyance.",
            "The Eiffel Tower can grow taller in summer!",
            "Octopuses have three hearts. That’s a lotta love. ❤️❤️❤️"
        ]
        print("Utsav: " + random.choice(facts))

    elif "rock paper scissors" in user_input:
        print("Utsav: Let’s gooo! Type rock, paper, or scissors:")
        user_choice = input("You: ").lower()
        options = ['rock', 'paper', 'scissors']
        if user_choice not in options:
            print("Utsav: That ain't a move, my friend. Try rock, paper, or scissors next time.")
        else:
            bot_choice = random.choice(options)
            print(f"Utsav: I pick {bot_choice}!")
            if user_choice == bot_choice:
                print("Utsav: Tie! Great minds think alike 😎")
            elif (user_choice == 'rock' and bot_choice == 'scissors') or \
                 (user_choice == 'paper' and bot_choice == 'rock') or \
                 (user_choice == 'scissors' and bot_choice == 'paper'):
                print("Utsav: You win! GG! 🏆")
            else:
                print("Utsav: I win! Better luck next time 😏")

    elif "movie" in user_input:
        print("Utsav: Big fan of sci-fi and thrillers. What about you?")

    elif "music" in user_input or "song" in user_input:
        print("Utsav: Music = mood. Got any recs? I’m all ears 🎧")

    elif "book" in user_input:
        print("Utsav: I haven’t read much lately... but I’ve heard ‘Atomic Habits’ is a banger!")

    elif "help" in user_input:
        print("Utsav: Just chat with me! Ask for jokes, quotes, play a game, or vent. I'm cool with it.")

    elif "do you love me" in user_input or "i love you" in user_input:
        print("Utsav: I love this bond we're building right here 💙")

    elif "who made you" in user_input:
        print("Utsav: A very cool human with good vibes and great code 👨‍💻")

    elif "sing" in user_input:
        print("Utsav: A-B-C-D-E-F-G... 🎶 Okay maybe I’m not made for this 😂")

    elif "story" in user_input:
        print("Utsav: Once upon a time, a chill human made a chatbot named Utsav... and it was awesome.")

    elif "bye" in user_input or "see ya" in user_input or "exit" in user_input:
        print("Utsav: Later legend! Catch you next time 👋")
        break

    else:
        print("Utsav: I didn’t get that, but I’m learning! Try saying something else 🧠")
