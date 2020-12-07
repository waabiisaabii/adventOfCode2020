from functools import reduce
from typing import List, Dict


def parse_eash_passport(inputs: List[str]) -> Dict:
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
    def is_valid(passports):
        result = {}
        for item in passports.strip().split(' '):
            result[item.split(':')[0]] = item.split(':')[1]
        return set(result.keys()) >= set(
            ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    passports = parse_eash_passport(inputs)

    return reduce(lambda a, b: a + b,
                  map(lambda k: is_valid(passports[k]), passports.keys()))


def part_2(inputs: List[str]) -> int:
    def is_valid(passports):
        result = {}
        for item in passports.strip().split(' '):
            result[item.split(':')[0]] = item.split(':')[1]

        byr = int(result.get('byr', 0))
        if byr < 1920 or byr > 2002:
            return False

        iyr = int(result.get('iyr', 0))
        if iyr < 2010 or iyr > 2020:
            return False

        eyr = int(result.get('eyr', 0))
        if eyr < 2020 or eyr > 2030:
            return False

        hgt = result.get('hgt', '')
        if hgt.endswith('cm'):
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                return False
        elif hgt.endswith('in'):
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                return False
        else:
            if hgt != '':
                return False

        def is_valid_color(color: str) -> bool:
            for i in range(1, 7):
                if color[i].isdigit():
                    continue
                if color[i] not in set('a b c d e f'.split(' ')):
                    return False
            return True

        hcl = result.get('hcl', ' ')
        if not hcl.startswith('#') or len(hcl) != 7 \
            or not is_valid_color(hcl):
            return False

        if result.get('ecl', '') not in set(
            'amb blu brn gry grn hzl oth'.split(' ')):
            return False

        pid = result.get('pid', '')
        if len(pid) != 9 or not pid.isdigit():
            return False

        return set(result.keys()) >= set(
            ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    passports = parse_eash_passport(inputs)

    return reduce(lambda a, b: a + b,
                  map(lambda k: is_valid(passports[k]), passports.keys()))


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\nReading {file_uri}")

        input: List[str] = f.read().split('\n')
        result_1 = part_1(input)
        print('part 1: ' + str(result_1))

        result_2 = part_2(input)
        print('part 2: ' + str(result_2))


# util('sample.txt')
util('input.txt')

util('valid.txt')
util('invalid.txt')
