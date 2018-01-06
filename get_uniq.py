class Tags:
    def __init__(self, filename):
        self.tags_list = self.read_file(filename)
        self.uniqe_tags_list = self.__get_uniq_tags()

    def read_file(self, filename):
        return open(filename, 'r').read().splitlines()

    def write_to_file(self):
        with open('unique_tags_from_class.txt', 'w') as f:
            f.write('\n'.join(self.uniqe_tags_list))

    def __get_uniq_tags(self):
        return set(self.tags_list)


if __name__ == "__main__":
    tags = Tags('tags.txt')
    tags.write_to_file()
