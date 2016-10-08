import random

def weighted_choice(choices):
    """
    Choose a random element from a list, where each element may have a
    different probability of being chosen (its 'weight').

    The list contains 2-tuples of (weight, element), where the first element
    is the probability of being chosen and the second is the actual element.

    Adapted from: http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice/.

    :param cs: a list of 2-tuples
    :return: a random element from the list
    """

    total = sum(weight for weight, _ in choices)
    thresh = random.uniform(0, total)

    upto = 0
    for weight, choice in choices:
        if upto + weight >= thresh:
            return choice
        else:
            upto += weight
