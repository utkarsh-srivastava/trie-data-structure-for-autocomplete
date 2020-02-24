matched_words = []


class Node():
    def __init__(self):
        self.next = {}
        self.word_match = False

    def add_word(self, string):
        if len(string) == 0:
            self.word_match = True
            return
        # first char of string
        key = string[0]
        # remaining char of string except the first
        string = string[1:]
        # check if the next node with key is available or not. If not then create the next node with the key
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
                print('No results found')
                return []
        else:
            if self.word_match == True:
                matched_words.append(aggregated_word)
            for k in self.next:
                self.next[k].dfs(matched_words, aggregated_word + k)


def insert_words_from_files():
    root = Node()
    with open('dict.txt', mode='r') as f:
        contents = f.readlines()
        for word in contents:
            root.add_word(word.strip('\r\n'))
    return root


if __name__ == "__main__":
    root = insert_words_from_files()
    while True:
        matched_words = []
        print('Enter the word to search')
        word_to_search = input()
        root.populate_matching_words(word_to_search)
        print(matched_words)
