matched_words = []


class Node():
    def __init__(self):
        self.next = {}
        self.word_match = False

    def add_word(self, string):
        if len(string) == 0:
            self.word_match = True
            return
        key = string[0]
        string = string[1:]
        if key in self.next:
            self.next[key].add_word(string)
        else:
            node = Node()
            self.next[key] = node
            node.add_word(string)

    def dfs(self, matched_words, aggregated_word=None):
        '''perform deep first search'''
        # if it is a leaf node
        if self.next.keys() == []:
            return
        if self.word_match == True:
            matched_words.append(aggregated_word)

        for key in self.next:
            self.next[key].dfs(matched_words, aggregated_word + key)

    def populate_matching_words(self, word_to_search, aggregated_word=''):
        global matched_words
        if len(word_to_search) > 0:
            key = word_to_search[0]
            word_to_search = word_to_search[1:]
            if key in self.next:
                aggregated_word += key
                self.next[key].populate_matching_words(
                    word_to_search, aggregated_word)
            else:
                return []
        else:
            if self.word_match == True:
                matched_words.append(aggregated_word)
            for k in self.next:
                self.next[k].dfs(matched_words, aggregated_word + k)


if __name__ == "__main__":
    root = Node()
    root.add_word('apple')
    root.add_word('applet')
    # root.populate_matching_words('ut')
    root.populate_matching_words('apple')
    print(matched_words)
