#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        scores = list(a_dictionary.values())
        maxScore = max(scores)

        for k, v in a_dictionary.items():
            if (a_dictionary[k] == maxScore):
                return k
    else:
        return None
