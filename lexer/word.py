from .word_type import WordType

class Word:
    def __init__(self, word, word_type):
        self.word = word
        self.word_type = word_type

    def __str__(self):
        return f'{self.word_type:<20} {self.word}'

    def __eq__(self, other):
        return self.word == other.word and self.word_type == other.word_type
