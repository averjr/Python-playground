from memory_profiler import profile
import sys

from collections import OrderedDict


@profile
def count_lines():
    num_lines = sum(1 for line in open('tags.txt'))
    print(num_lines)
    print(sys.getsizeof(num_lines))


@profile
def uniq_set():
    content = open('tags.txt', 'r').readlines()
    content_set = set(content)
    print(len(content_set))
    print(sys.getsizeof(content))
    print(sys.getsizeof(content_set))


@profile
def using_ordered_dict():
    # with open('tags.txt') as infile, open('output.txt', 'w') as outfile:
    #     outfile.writelines(OrderedDict.fromkeys(infile))
    with open('tags.txt') as infile:
        d = OrderedDict.fromkeys(infile)
        print(len(d))
        print(sys.getsizeof(d))


count_lines()
uniq_set()
using_ordered_dict()
