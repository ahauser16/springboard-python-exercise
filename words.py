def print_upper_words(words, must_start_with):
    """Print each word on a separate line in uppercase if it starts with a specified letter.

    - words: list of words
    - must_start_with: set of letters

    For example:

      print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})

    should print:

      HELLO
      HEY
      YO
      YES
    """

    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})