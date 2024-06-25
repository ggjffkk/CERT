import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    n = 3
    guess = "R"
    if len(opponent_history) >= n:
        pattern = "".join(opponent_history[-n:])

        possible_plays = ["R", "P", "S"]
        patterns = ["".join([a, b, c]) for a in possible_plays for b in possible_plays for c in possible_plays]

        sub_str = pattern[:-1]
        freqs = {p: 0 for p in patterns}
        
        for i in range(len(opponent_history) - n + 1):
            seq = "".join(opponent_history[i:i+n])
            if seq in freqs:
                freqs[seq] += 1

        most_frequent_pattern = max(freqs, key=freqs.get)

        if most_frequent_pattern[-1] == "R":
            guess = "P"
        elif most_frequent_pattern[-1] == "P":
            guess = "S"
        elif most_frequent_pattern[-1] == "S":
            guess = "R"

    return guess
import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    n = 3
    guess = "R"
    if len(opponent_history) >= n:
        pattern = "".join(opponent_history[-n:])

        possible_plays = ["R", "P", "S"]
        patterns = ["".join([a, b, c]) for a in possible_plays for b in possible_plays for c in possible_plays]

        sub_str = pattern[:-1]
        freqs = {p: 0 for p in patterns}
        
        for i in range(len(opponent_history) - n + 1):
            seq = "".join(opponent_history[i:i+n])
            if seq in freqs:
                freqs[seq] += 1

        most_frequent_pattern = max(freqs, key=freqs.get)

        if most_frequent_pattern[-1] == "R":
            guess = "P"
        elif most_frequent_pattern[-1] == "P":
            guess = "S"
        elif most_frequent_pattern[-1] == "S":
            guess = "R"

    return guess
