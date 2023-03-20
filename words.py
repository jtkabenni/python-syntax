words = ["hello", "balloon", "hey", "goodbye", "google", "yo", "yes"]
def print_upper_words(words, must_start_with):
    """print_upper_words(["hello", "balloon" "hey", "goodbye", "yo", "yes"],must_start_with ={"b", "g"})"""

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
              print (word.upper())



print_upper_words (words, must_start_with = {"h", "g"})