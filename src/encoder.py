import heapq
import networkx as nx
import json
from dotenv import load_dotenv
import os

load_dotenv()

class Node(object):
    def __init__(self, value, weight, left = None, right = None, is_leaf = False):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right
        self.is_leaf = is_leaf

    def __lt__(self, other):
        return self.weight < other.weight
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.value, self.weight, self.left, self.right, self.is_leaf) == (other.value, other.weight, other.left, other.right, other.is_leaf)
        return False

class Encoder():
    def open_file(self, file_path: str):
        with open(file_path, encoding="utf8") as file:
            content = file.read()
    
        return content

    def count_chars(self, content: str):
        frequency = {}
        
        for char in content:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        return frequency

    def create_node(self, *, dict: dict[str, int]):
        partial_tree_nodes = []
        for k, v in dict.items():
            node = Node(k, v, is_leaf = True)
            partial_tree_nodes.append(node)

        return partial_tree_nodes
    
    def create_priority_queue(self, *, partial_tree_nodes: list[Node]):
        priority_queue = []

        for node in partial_tree_nodes:
            heapq.heappush(priority_queue, (node.weight, node))

        return priority_queue
    
    def create_tree(self, *, priority_queue: list):
        while len(priority_queue) > 1:
            node_1 = heapq.heappop(priority_queue)[1]
            node_2 = heapq.heappop(priority_queue)[1]
            
            combined_partial_tree = Node(node_1.weight + node_2.weight, 
                                         node_1.weight + node_2.weight, 
                                         left = node_1, 
                                         right = node_2)

            heapq.heappush(priority_queue, (combined_partial_tree.weight, combined_partial_tree))
    
        return priority_queue[0][1]

    def generate_mapping(self, root, code="", mapping={}):
        if root is not None:
            if root.value is not None and root.is_leaf:
                mapping[root.value] = code
            self.generate_mapping(root.left, code + "0", mapping)
            self.generate_mapping(root.right, code + "1", mapping)
        return mapping

    def generate_file(self, prefix_code_table: dict, text: str, filename: str):
        header_json = json.dumps(prefix_code_table)
        encoded_content, extra_zero = self.encoding_content(text=text, prefix_code_table=prefix_code_table)

        with open(filename, 'wb') as file:
            file.write(header_json.encode('utf-8'))
            file.write(os.getenv('SEPARATOR').encode('utf-8'))
            file.write(encoded_content)
            file.write(os.getenv('SEPARATOR').encode('utf-8'))
            file.write(str(extra_zero).encode('utf-8'))

    def encoding_content(self, text: str, prefix_code_table: dict):
        bit_string = ''
        for char in text:
            bit_string += prefix_code_table[char]

        extra_zero = 0
        if len(bit_string) % 8 != 0:
            extra_zero = 8 - len(bit_string) % 8
            bit_string += '0' * extra_zero

        bytes = bytearray()
        for i in range(0, len(bit_string), 8):
            byte = bit_string[i:i+8]
            bytes.append(int(byte, 2))
        
        return bytes, extra_zero