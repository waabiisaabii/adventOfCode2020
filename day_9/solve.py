from typing import List


def part_1(inputs: List[str]) -> int:
    # sample preamble is 5 but actual question asks 25
    preamble = 25
    inputs_int = [int(x) for x in inputs]
    i = preamble - 1
    bag = set([inputs_int[x] for x in range(0, preamble)])
    while i < len(inputs_int):
        next_val = inputs_int[i + 1]
        is_valid = False
        for given in bag:
            if next_val - given in bag and given != next_val - given:
                is_valid = True
                break
        if not is_valid:
            return next_val
        i = i + 1
        bag.add(next_val)
        bag.remove(inputs_int[i - preamble])
    return -1


def part_2(inputs: List[str], result_1: int) -> int:


    pass


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input: List[str] = f.read().split("\n")
        result_1 = part_1(input)
        print("part 1: " + str(result_1))

        result_2 = part_2(input, result_1)
        print("part 2: " + str(result_2))


# util("sample.txt")
util("input.txt")

