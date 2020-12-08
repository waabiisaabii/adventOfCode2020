from typing import List, Dict


class TreeNode:
    def __init__(self, value):
        self.children_str_set = set()
        self.value = value
        self.parents_str_set = set()
        self.children_count = {}


def build_tree_mapping(inputs: List[str]) -> Dict:
    node_maps = {}

    for rule in inputs:
        parent_str = ' '.join(rule.strip().split('contain')[0]
                              .strip().split(' ')[:-1]).strip()
        children_str_list = [' '.join(x.strip('.').strip().split(' ')[1:-1])
                             for x in
                             rule.strip().split('contain')[1].split(',')]
        children_str_list = list(
            filter(lambda x: x != 'other', children_str_list))

        if parent_str not in node_maps:
            node_maps[parent_str] = TreeNode(parent_str)
        parent_node = node_maps[parent_str]
        parent_node.children_str_set.update(children_str_list)

        for child_str in children_str_list:
            if child_str == 'other':
                continue

            if child_str not in node_maps:
                node_maps[child_str] = TreeNode(child_str)
            child_node = node_maps[child_str]
            child_node.parents_str_set.add(parent_str)


def part_1(inputs: List[str]) -> int:
    # top down: build tree
    node_maps = build_tree_mapping(inputs)

    # bottom up, trace back
    stack = ['shiny gold']
    can_hold_bags = set()
    while len(stack) > 0:
        current_str = stack.pop()
        parents_str = node_maps[current_str].parents_str_set

        can_hold_bags.update(parents_str)
        for parent_str in parents_str:
            stack.append(parent_str)
    return len(can_hold_bags)


def part_2(inputs: List[str]) -> int:
    # top down: build tree
    node_maps = build_tree_mapping(inputs)

    # top down again, count
    stack = ['shiny gold']
    count = 0
    while len(stack) > 0:
        current_str = stack.pop()
        children_str = node_maps[current_str].children_str_set


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
