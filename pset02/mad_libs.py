import random

Templates = [
    {"text": "The :color :animal :action over the :adjective :plant.",
     "author": "Cole"},
    {"text": "A :color :object is :adjective and :verb.",
     "author": "Cole"},
    {"text": "The :adjective :animal :verb with a :color :object.",
     "author": "Cole"},
    {"text": "A :color :animal :verb the :adjective :object.",
     "author": "Cole"},
    {"text": "The :adjective :animal :verb the :color :object.",
     "author": "Cole"},
    {"text": "A :color :animal :verb the :adjective :object.",
     "author": "Cole"},
    {"text": "The :adjective :animal :verb the :color :object.",
     "author": "Cole"},
    {"text": "A :color :animal :verb the :adjective :object.",
     "author": "Cole"},
    {"text": "The :adjective :animal :verb the :color :object.",
     "author": "Cole"},
    {"text": "A :color :animal :verb the :adjective :object.",
     "author": "Cole"}
]


def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if 1 <= len(user_input) <= 30:
            return user_input
        else:
            print("Input must be between 1 and 30 characters long. Please try again.")


def get_random_template():
    return random.choice(Templates)


def fill_in_template(template):
    words = template["text"].split()
    for word in words:
        if word.startswith(":"):
            user_input = get_user_input(f"Please enter a {word[1:]}: ")
            words[words.index(word)] = user_input
    filled_template = " ".join(words)
    print(" " + filled_template)
    print(f"Author: {template['author']}")


def play_mad_libs():
    template = get_random_template()
    fill_in_template(template)
    yes_answers = {"yes", "y", "sí", "si", "oui",
                   "sure", "absolutely", "definitely"}
    no_answers = {"no", "nope", "nah"}
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in yes_answers:
        play_mad_libs()
    elif play_again in no_answers:
        print("Thanks for playing!")
    else:
        print("Invalid response. Please answer with a 'yes' or 'no'.")


play_mad_libs()
