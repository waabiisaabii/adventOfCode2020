from typing import List


def part_1(input: List[int]) -> int:
    s = set(input)
    for val in input:
        if 2020 - val in s:
            return (2020 - val) * val
    return -1


def part_2(input: List[int]) -> int:
    s = set(input)
    for j in range(0, len(input)):
        for k in range(0, len(input)):
            if k == j:
                continue
            target = 2020 - (input[j] + input[k])
            if target in s:
                return target * input[j] * input[k]
    return -1


with open('sample.txt') as f:
    input = f.read().split()
    cleaned = list(map(lambda x: int(x), input))
    result_1 = part_1(cleaned)
    print('part 1 ' + str(result_1))

    result_2 = part_2(cleaned)
    print('part 2 ' + str(result_2))

with open('input.txt') as f:
    input = f.read().split()
    cleaned = list(map(lambda x: int(x), input))
    result_1 = part_1(cleaned)
    print('part 1 ' + str(result_1))

    result_2 = part_2(cleaned)
    print('part 2 ' + str(result_2))
