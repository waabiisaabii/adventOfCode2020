from typing import List


def part_1(inputs: List[str]) -> int:
    # TODO
    def is_valid(
        minimum: int,
        maximum: int,
        target: str,
        given_passwd: str) -> int:

        freq = {}
        for c in given_passwd:
            freq[c] = freq.get(c, 0) + 1

        f = freq.get(target, 0)
        return 0 \
            if f > maximum or f < minimum \
            else 1

    count = 0
    for input in inputs:
        if input == '':
            continue
        splitted = input.split()

        minimum = int(splitted[0].split('-')[0])
        maximum = int(splitted[0].split('-')[1])
        target = splitted[1][:-1]
        given_passwd = splitted[2]

        count = count + is_valid(
            minimum, maximum, target, given_passwd)

    return count


def part_2(inputs: List[str]) -> int:
    def is_valid(
        idx_1: int,
        idx_2: int,
        target: str,
        given_passwd: str) -> int:
        char_at_1 = given_passwd[idx_1 - 1]
        char_at_2 = given_passwd[idx_2 - 1]
        return 1 \
            if \
            (char_at_1 == target) ^ \
            (char_at_2 == target) \
            else 0

    count = 0
    for input in inputs:
        splitted = input.split()

        idx_1 = int(splitted[0].split('-')[0])
        idx_2 = int(splitted[0].split('-')[1])
        target = splitted[1][:-1]
        given_passwd = splitted[2]

        count = count + \
                is_valid(idx_1, idx_2, target, given_passwd)

    return count


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input = f.read().split('\n')
        result_1 = part_1(input)
        print('part 1: ' + str(result_1))

        result_2 = part_2(input)
        print('part 2: ' + str(result_2))


util('sample.txt')
util('input.txt')
