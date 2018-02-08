import re


class Analizator:
    def __init__(self, file_with_tags, file_with_tweets):
        self.tags_list = open(file_with_tags, 'r').read().splitlines()
        self.text = open(file_with_tweets, 'r').read()

    def find_with_regular_expresion(self, tag):
        regex = r"" + re.escape(tag) + r""
        return re.findall(regex, self.text)

    def find_with_string_find(self, tag):
        result = self.findall(tag, self.text)
        print(sum(1 for i in result))

    def __findall(self, p, s):
        '''Yields all the positions of
        the pattern p in the string s.'''
        i = s.find(p)
        while i != -1:
            yield i
            i = s.find(p, i+1)


if __name__ == "__main__":
    Analizator('uniue_tags_from_class.txt', 'twitter_data.txt')
