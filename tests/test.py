import heapq
import unittest
from src.encoder import Encoder, Node
from src.decoder import Decoder

class CompressionToolTest(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()
        self.decoder = Decoder()

    def test_read_encode_input_file(self):
        actual = self.encoder.open_file(file_path='tests/files/sample_2.txt')
        self.assertIsInstance(actual, str)

    def test_count_chars_is_dict(self):
        string = 'This is a tester text'
        actual = self.encoder.count_chars(content=string)
        self.assertIsInstance(actual, dict)

    def test_count_chars(self):
        string = 'This is a tester text'
        actual = self.encoder.count_chars(content=string)
        expected = {'T': 1, 'h': 1, 'i': 2, 's': 3, ' ': 4, 'a': 1, 't': 4, 'e': 3, 'r': 1, 'x': 1}
        self.assertEqual(actual, expected)

    def test_create_node_is_list(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        actual = self.encoder.create_node(dict=dictionary)
        self.assertIsInstance(actual, list)

    def test_create_node(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        actual = self.encoder.create_node(dict=dictionary)
        expected = [Node('a', 1, is_leaf=True), Node('b', 2, is_leaf=True), Node('c', 3, is_leaf=True)]
        self.assertEqual(actual, expected)

    def test_create_priority_queue(self):
        nodes = [Node('a', 3), Node('b', 2), Node('c', 1), Node('d', 5), Node('e', 2)]
        queue = self.encoder.create_priority_queue(partial_tree_nodes=nodes)
        actual = heapq.heappop(queue)[1]
        expected = Node('c', 1)
        self.assertEqual(actual, expected)

    def test_create_tree(self):
        queue = [(1, Node('a', 1)), (2, Node('b', 2)), (3, Node('c', 4))]
        actual = self.encoder.create_tree(priority_queue=queue)
        expected = Node(7 , 7,
                        left = Node(3 , 3, 
                                   left = Node('a', 1),
                                   right = Node('b', 2)
                                ),
                        right = Node('c', 4))
        self.assertEqual(actual, expected)

    def test_generate_mapping(self):
        tree = Node(7 , 7,
                        left = Node(3 , 3, 
                                   left = Node('a', 1, is_leaf=True),
                                   right = Node('b', 2, is_leaf=True)
                                ),
                        right = Node('c', 4, is_leaf=True))
        actual = self.encoder.generate_mapping(root=tree)
        expected = {'a': '00', 'b': '01' , 'c': '1'}
        self.assertEqual(actual, expected)

    def test_encoding_content(self):
        mapping = {'a': '00', 'b': '01' , 'c': '1'}
        actual = self.encoder.encoding_content(prefix_code_table=mapping, text='abbcccc')

        expected = bytearray()
        expected.append(23)
        expected.append(192)
        self.assertEqual(actual[0], expected)

    def test_string_to_bitstring(self):
        bytes = bytearray()
        bytes.append(23)
        bytes.append(192)
        actual = self.decoder.string_to_bitstring(input_string=bytes)
        expected = '0001011111000000'
        self.assertEqual(actual, expected)

    def test_decoding_content(self):
        mapping = {'a': '00', 'b': '01' , 'c': '1'}
        bit_str = '0001011111000000'
        actual = self.decoder.decoding_content(bit_string=bit_str, prefix_table=mapping, extra_zero=6)
        expected = 'abbcccc'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()