from typing import List, Dict


class GraphNode:
    def __init__(self, value):
        self.children_str_set = set()
        self.value = value
        self.parents_str_set = set()
        self.children_count = {}


def build_graph_mapping(inputs: List[str]) -> Dict:
    node_maps = {}

    for rule in inputs:
        parent_str = ' '.join(rule.strip().split('contain')[0]
                              .strip().split(' ')[:-1]).strip()

        children_freq_map = {}

        children_statement = rule.strip().split('contain')[1].strip()
        for s in children_statement.split(','):
            s = s.strip('.').strip()
            if s.split(' ')[0] == 'no':
                continue
            freq = int(s.split(' ')[0])
            name = ' '.join(s.split(' ')[1:-1])
            children_freq_map[name] = freq

        if parent_str not in node_maps:
            node_maps[parent_str] = GraphNode(parent_str)
        parent_node = node_maps[parent_str]

        parent_node.children_count = children_freq_map

        for child_str, _ in children_freq_map.items():
            if child_str == 'other':
                continue

            if child_str not in node_maps:
                node_maps[child_str] = GraphNode(child_str)
            child_node = node_maps[child_str]
            child_node.parents_str_set.add(parent_str)
    return node_maps


def part_1(inputs: List[str]) -> int:
    # top down: build tree
    node_maps = build_graph_mapping(inputs)

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
    node_maps = build_graph_mapping(inputs)

    # top down again, count
    stack = [(1, 'shiny gold')]
    count = 0
    while len(stack) > 0:
        current_freq, current_str = stack.pop()
        count = count + current_freq

        children_count_map: Dict = node_maps[current_str].children_count
        for child, freq in children_count_map.items():
            stack.append((current_freq * freq, child))
    return count - 1


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
