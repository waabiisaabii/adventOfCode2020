from typing import List

mapping = {
    'F': 'left',
    'B': 'right',
    'L': 'left',
    'R': 'right'
}


def binary_search(actions: str, upper: int) -> int:
    left = 0
    right = upper

    for i in range(0, len(actions)):
        mid = int(left + (right - left) / 2)
        action = mapping[actions[i]]
        if action == 'left':
            right = mid
        else:
            left = mid + 1
    return left


def compute_id(input: str) -> int:
    row = binary_search(input[:-3], 127)
    col = binary_search(input[-3:], 7)
    return row * 8 + col


def part_1(inputs: List[str]) -> int:
    ids = [compute_id(x) for x in inputs]
    return max(ids)


def part_2(inputs: List[str]) -> int:
    ids = [compute_id(x) for x in inputs]
    ids.sort()
    left = 0
    right = len(ids) - 1

    import math
    while left < right:
        mid_value = math.ceil((ids[left] + ids[right]) / 2)
        mid = int(left + (right - left) / 2)
        if ids[mid] < mid_value:
            left = mid + 1
        else:
            right = mid - 1
    return ids[right] + 1


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input: List[str] = f.read().split('\n')
        result_1 = part_1(input)
        print("part 1: " + str(result_1))

        result_2 = part_2(input)
        print("part 2: " + str(result_2))


util("sample.txt")
util("input.txt")
