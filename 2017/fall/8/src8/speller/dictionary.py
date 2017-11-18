class Dictionary:
    """Implements a dictionary's functionality"""

    def __init__(self):
        self.words = set()

    def check(self, word):
        """Return true if word is in dictionary else false"""
        return word.lower() in self.words

    def load(self, dictionary):
        """Load dictionary into memory, returning true if successful else false"""
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True

    def size(self):
        """Returns number of words in dictionary if loaded else 0 if not yet loaded"""
        return len(self.words)

    def unload(self):
        """Unloads dictionary from memory, returning true if successful else false"""
        return True
