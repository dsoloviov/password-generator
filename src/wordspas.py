#/usr/bin/env python

import random
import pickle
import os.path
import requests

WORD_SITE = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
CACHE_NAME = "words.pickle"


class WordsPassword(object):
    """
    Generate password consisting of words
    """
    def __init__(self, number_of_words=4, min_length=5, delimiter="-", complicate=False):
        self.number_of_words = number_of_words
        self.min_length = min_length
        self.delimiter = delimiter
        self.complicate = complicate
        self.words = []
        self.elements = []
        self.complication = {"o": "0", "i": "!", "l": "1"}
        self.password = self.__generate_password()

    def __generate_password(self):
        self.__cache()
        for i in range(self.number_of_words):
            self.elements.append(self.__get_word())
        password = self.delimiter.join(self.elements)
        if self.complicate:
            return self.__complicate_password(password)
        return password

    def __get_word(self):
        while True:
            word = random.choice(self.words)
            if len(word) > self.min_length:
                return word.lower()

    def __cache(self):
        if os.path.exists(CACHE_NAME):
            with open(CACHE_NAME, "rb") as cache:
                self.words = pickle.load(cache)
        else:
            print "Fetching words..."
            response = requests.get(WORD_SITE)
            self.words = response.content.splitlines()
            with open(CACHE_NAME, 'wb') as cache:
                pickle.dump(self.words, cache)

    def __complicate_password(self, password):
        for key, value in self.complication.iteritems():
            password = password.replace(key, value)
        return password


if __name__ == "__main__":
    words_password = WordsPassword(complicate=True)
    print words_password.password
