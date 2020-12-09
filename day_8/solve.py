from typing import List


def part_1(inputs: List[str]) -> int:
    instructions = list(
        map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), inputs))
    visited = set()
    next_instruction = (0, instructions[0][0], instructions[0][1])
    global_accu = 0
    while next_instruction[0] not in visited:
        current_pos, action, step = next_instruction
        visited.add(current_pos)

        if action == 'nop':
            next_pos = current_pos + 1
        elif action == 'acc':
            global_accu = global_accu + step
            next_pos = current_pos + 1
        elif action == 'jmp':
            next_pos = current_pos + step

        if next_pos > len(instructions) - 1:
            return global_accu

        next_instruction = (
            next_pos, instructions[next_pos][0], instructions[next_pos][1])
    return global_accu


def replace(instructions: List, idx: int, target_action: str) -> List:
    result = []
    for ii in range(0, len(instructions)):
        if ii == idx:
            result.append((target_action, instructions[ii][1]))
        else:
            result.append((instructions[ii][0], instructions[ii][1]))
    return result


def part_2(inputs: List[str]) -> int:
    instructions = list(
        map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), inputs))
    jump_indices = []
    nops = []
    for i in range(0, len(instructions)):
        action, step = instructions[i]
        if action == 'nop':
            jump_indices.append(i)
        elif action == 'jmp':
            nops.append(i)

    for idx in jump_indices:
        current_instructions = replace(instructions, idx, 'jmp')
        visited = set()
        next_instruction = (
            0, current_instructions[0][0], current_instructions[0][1])
        global_accu = 0
        while next_instruction[0] not in visited:

            current_pos, action, step = next_instruction
            visited.add(current_pos)

            if action == 'nop':
                next_pos = current_pos + 1
            elif action == 'acc':
                global_accu = global_accu + step
                next_pos = current_pos + 1
            elif action == 'jmp':
                next_pos = current_pos + step

            if next_pos > len(current_instructions) - 1:
                return global_accu

            next_instruction = (
                next_pos, current_instructions[next_pos][0],
                current_instructions[next_pos][1])

    for idx in nops:
        current_instructions = replace(instructions, idx, 'nop')
        visited = set()
        next_instruction = (
            0, current_instructions[0][0], current_instructions[0][1])
        global_accu = 0
        while next_instruction[0] not in visited:
            current_pos, action, step = next_instruction

            visited.add(current_pos)

            if action == 'nop':
                next_pos = current_pos + 1
            elif action == 'acc':
                global_accu = global_accu + step
                next_pos = current_pos + 1
            elif action == 'jmp':
                next_pos = current_pos + step

            if next_pos > len(current_instructions) - 1:
                return global_accu

            next_instruction = (
                next_pos, current_instructions[next_pos][0],
                current_instructions[next_pos][1])
    return -1


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
