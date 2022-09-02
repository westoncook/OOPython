from random import randint


class WordFinder:
    """
    Word Finder: finds random words from a dictionary.

    >>> find = WordFinder('oneword.txt')
    1 words read

    >>> find.get_random_word()
    'tornado'
    """

    def __init__(self, path):
        self.path = path
        self.word_list = self.get_list()
        self.len = len(self.word_list)
        print(f"{self.len} words read")

    def get_list(self):
        file = open(self.path, 'r')
        lst = [word.strip() for word in file.readlines()]
        file.close()
        return lst

    def get_random_word(self):
        rand = randint(0, self.len -1)
        return self.word_list[rand]


class SpecialWordFinder(WordFinder):
    """ Special Word Finder: picks random word from file while ignoring empty lines and comments
    
        >>> f = SpecialWordFinder("word.txt")
        1 words read


        >>> f.get_random_word()
        'tornado'
    """
    
    def get_list(self):
        unprocessed_list = super().get_list()
        return [word for word in unprocessed_list if len(word) > 0 and not '#' in word]

    


