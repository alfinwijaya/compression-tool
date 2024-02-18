from dotenv import load_dotenv

class Decoder():
    def open_file(self, file_path: str):
        with open(file_path, 'rb') as file:
            content = file.read()

        return content

    def string_to_bitstring(self, input_string):
        bit_string = ""
        for char in input_string:
            bit_string += format(char, '08b')
        
        return bit_string

    def decoding_content(self, bit_string: str, prefix_table: dict, extra_zero: int):
        decoded_string = ''
        current_code = ''

        if extra_zero > 0:
            bit_string = bit_string[:-extra_zero]

        for bit in bit_string:
            current_code += bit
            letter = next((key for key, value in prefix_table.items() if value == current_code), None)
            if letter:
                decoded_string += letter
                current_code = ''
        
        return decoded_string