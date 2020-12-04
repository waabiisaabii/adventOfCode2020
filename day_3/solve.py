from functools import reduce
from typing import List


def part_1(inputs: List[str],
    right_offset: int,
    bottom_offset: int) -> int:
    count = 0
    i = 0
    j = 0
    while i < len(inputs):
        current = inputs[i][j]
        count = count + (1 if current == '#' else 0)
        i = i + bottom_offset
        j = (j + right_offset) % len(inputs[0])
    return count


def part_2(inputs: List[str]) -> int:
    options = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    return reduce(lambda a, b: a * b,
                  [part_1(inputs, x, y) for (x, y) in options])


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input: List[str] = f.read().split('\n')
        result_1 = part_1(input, 3, 1)
        print('part 1: ' + str(result_1))

        result_2 = part_2(input)
        print('part 2: ' + str(result_2))


util('sample.txt')
util('input.txt')
