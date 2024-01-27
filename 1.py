class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count = 0
        self.internal_count = -1
        return self

    def __next__(self):
        if self.count == len(self.list_of_list):
            raise StopIteration
        else:
            len_internal_list = len(self.list_of_list[self.count])
            if self.internal_count < len_internal_list-1:
                self.internal_count += 1
            else:
                self.count += 1
                self.internal_count = 0
        return self.list_of_list[self.count][self.internal_count]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        # print(f'flat: {flat_iterator_item}, check: {check_item}')

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
