# Things to do:
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"+
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------

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
