import more_itertools

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)

print('|*|' * 20)

flat_list = [item for sublist in nested_list for item in sublist]
ip = list(more_itertools.flatten(nested_list))
print(ip)


class FlatIterator(list):

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        return '\n'.join(str(i) for i in self.pop(0))


for item in FlatIterator(nested_list):
    print(item)

print('|*|' * 20)


def flat_generator(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    yield flat_list


for item in flat_generator(nested_list):
    print(item)
