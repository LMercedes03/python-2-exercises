class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        self.word_count = len(self.sentence.split())

    def get_word_count(self):
        self.word_count = len(self.sentence.split())
        return self.word_count

    def get_shortest_word(self):
        words = self.sentence.split()
        return min(len(word) for word in words)

    def get_longest_word(self):
        words = self.sentence.split()
        return max(len(word) for word in words)


sentence = "This is a test of the emergency broadcast system"
word_counter = WordCounter(sentence)
word_counter.count_words()
print(word_counter.get_word_count())  # Returns the number of all the words.
print(word_counter.get_shortest_word())  # Returns the length of the shortest word.
print(word_counter.get_longest_word())  # Returns the length of the longest word.
