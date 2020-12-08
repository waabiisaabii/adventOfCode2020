from typing import List, Dict


def parse(inputs: List[str]) -> Dict:
    result = {}
    raw_idx = 0
    result_idx = 0

    while raw_idx < len(inputs):
        if inputs[raw_idx] == '':
            result_idx = result_idx + 1
        else:
            current = result.get(result_idx, ' ')
            result[result_idx] = current + ' ' + inputs[raw_idx]
        raw_idx = raw_idx + 1
    return result

def part_1(inputs: List[str]) -> int:
    parsed = parse(inputs)
    count = 0
    for _, answers in parsed.items():
        yes = set()
        for c in answers:
            if c == ' ':
                continue
            else:
                yes.add(c)
        count = count + len(yes)
    return count


def part_2(inputs: List[str]) -> int:
    parsed = parse(inputs)
    count = 0
    for _, answers in parsed.items():
        num_people = len(answers.strip().split(' '))
        yes = {}
        sub_count = 0
        for answer in answers.strip().split(' '):
            for c in answer:
                yes[c] = yes.get(c, 0) + 1
        for _, val in yes.items():
            if val == num_people:
                sub_count = sub_count + 1

        count = count + sub_count
    return count


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input: List[str] = f.read().split("\n")
        result_1 = part_1(input)
        print("part 1: " + str(result_1))

        result_2 = part_2(input)
        print("part 2: " + str(result_2))


util("sample.txt")
util("input.txt")

