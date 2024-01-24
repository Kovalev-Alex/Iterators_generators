nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', False],
    [1, 2, None],
]


class Nested_iter:
    def __init__(self, nested_list):
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self

    def __str__(self):
        return '\n'.join(str(elem) for elem in nested_list[self.start])


if __name__ == '__main__':
    for elem in Nested_iter(nested_list):
        print(elem)
