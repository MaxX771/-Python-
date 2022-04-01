nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, main_list):
        self.main_list = main_list

    def __iter__(self):
        self.my_list = []
        for i in self.main_list:
            self.my_list += i
        return self

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
        return self.my_list.pop(0)


for item in FlatIterator(nested_list):
    print(item)

print('|*|' * 20)


def flat_generator(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item


for item in flat_generator(nested_list):
    print(item)

print('|*|' * 20)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)