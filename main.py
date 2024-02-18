from src.decoder import Decoder
from src.encoder import Encoder
import argparse
from dotenv import load_dotenv
import os
import json

load_dotenv()

def encode(input_file: str, output_file: str):
    encoder = Encoder()
    content = encoder.open_file(file_path=input_file)
    frequency = encoder.count_chars(content)
    sorted = encoder.create_node(dict=frequency)
    nodes = encoder.create_priority_queue(partial_tree_nodes=sorted)
    tree = encoder.create_tree(priority_queue=nodes)
    table = encoder.generate_mapping(root=tree)
    encoder.generate_file(prefix_code_table=table, text= content, filename=output_file)

def decode(input_file: str, output_file: str):
    decoder = Decoder()
    content = decoder.open_file(file_path=input_file)
    content_arr = content.split(os.getenv('SEPARATOR').encode())
    bit_str = decoder.string_to_bitstring(input_string=content_arr[1])
    prefix_table = content_arr[0]
    prefix_dict = json.loads(prefix_table.decode('utf8'))
    decoded_str = decoder.decoding_content(bit_string=bit_str,prefix_table=prefix_dict, extra_zero=int(content_arr[2]))

    with open(output_file, 'w', encoding="utf8") as file:
        file.write(decoded_str)

def main():
    try:
        parser = argparse.ArgumentParser(description='Compression Tool.')
        parser.add_argument('input_file', metavar='I', type=str, help='Input file path')
        parser.add_argument('-e', metavar=('O',), help='encode', nargs=1)
        parser.add_argument('-d', metavar=('O',), help='decode', nargs=1)
        
        args = parser.parse_args()

        if args.e:
            encode(input_file=args.input_file, output_file=args.e[0])           

        elif args.d:
            decode(input_file=args.input_file, output_file=args.d[0])

    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()