import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. 
    Verb will match the tense and quantity.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def make_sentence(quantity, tense):
    """Build and return a sentence with a determiner, noun, and verb."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner.capitalize()} {noun} {verb}."
    return sentence

def main():
    # Generating and printing sentences with different quantity and tense
    print(make_sentence(1, "past"))      # single, past
    print(make_sentence(1, "present"))   # single, present
    print(make_sentence(1, "future"))    # single, future
    print(make_sentence(2, "past"))      # plural, past
    print(make_sentence(2, "present"))   # plural, present
    print(make_sentence(2, "future"))    # plural, future

# Calling the main function
if __name__ == "__main__":
    main()
