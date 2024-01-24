class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count = 0
        self.internal_count = 0
        return self

    def __next__(self):
        result = []
        if self.count <= len(self.list_of_list):
            self.len_internal_list = len(self.list_of_list[self.count])
            if self.internal_count == self.len_internal_list:
                self.count += 1
                self.internal_count = 0
                result.extend(self.list_of_list[self.count][self.internal_count])
                self.internal_count += 1
            elif self.internal_count < self.len_internal_list:
                result.extend(str(self.list_of_list[self.count][self.internal_count]))
                self.internal_count += 1
        else:
            raise StopIteration
        print(f'Вывод: внеш. {self.count}, внутр. {self.internal_count}', "".join(result))
        return "".join(result)


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        print(flat_iterator_item)
        print(check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
