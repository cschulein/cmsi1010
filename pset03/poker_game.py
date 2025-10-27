from cards import deal, poker_classification


def get_num_players():
    while True:
        user_input = input(
            "Enter number of players (2-10) or 'exit': ").strip().lower()
        if user_input in ["bye", "exit"]:
            return None
        try:
            num_players = int(user_input)
            if 2 <= num_players <= 10:
                return num_players
            else:
                print("Error: Number of players must be between 2 and 10.")
        except ValueError:
            print("Error: Invalid input. Please enter a number between 2 and 10.")


def play_poker():
    while True:
        num_players = get_num_players()
        if num_players == None:
            print("Thanks for playing!")
            break

        hands = deal(num_players, 5)
        for i in range(len(hands)):
            hand = list(hands[i])
            for j in range(len(hand)):
                for k in range(j+1, len(hand)):
                    if hand[j].rank > hand[k].rank:
                        hand[j], hand[k] = hand[k], hand[j]
            hand_str = ""
            for card in hand:
                hand_str = hand_str + str(card) + " "
            hand_str = hand_str.strip()
            classification = poker_classification(hands[i])
            print("Player " + str(i+1) + ": " +
                  hand_str + " : " + classification)


play_poker()
