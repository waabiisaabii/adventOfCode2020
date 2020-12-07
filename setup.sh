DAY=${1:=0}
DIR="day_$DAY"

mkdir $DIR
touch $DIR/input.txt
touch $DIR/sample.txt
touch $DIR/README.md
touch $DIR/solve.py
echo 'from typing import List


def part_1(inputs: List[str]) -> int:
    pass


def part_2(inputs: List[str]) -> int:
    pass


def util(file_uri: str):
    with open(file_uri) as f:
        print(f"\\nReading {file_uri}")

        input: List[str] = f.read().split('\n')
        result_1 = part_1(input)
        print('part 1: ' + str(result_1))

        result_2 = part_2(input)
        print('part 2: ' + str(result_2))


util('sample.txt')
util('input.txt')
' >> $DIR/solve.py

echo "- [ ] [$DIR]($DIR)" >> README.md
