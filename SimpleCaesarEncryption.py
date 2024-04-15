import string
import os

def caesar(text):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shift = 10
    alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def encrypt_file(input_filename, output_filename):
   #Reads data from input file, encrypts it, and writes to output file within the same folder.
   current_folder = os.path.dirname(__file__)  # Get the current script's directory
   input_file_path = os.path.join(current_folder, input_filename)
   output_file_path = os.path.join(current_folder, output_filename)

   with open(input_file_path, "r") as in_file, open(output_file_path, "w") as out_file:
       data = in_file.read()
       encrypted_data = caesar(data)
       out_file.write(encrypted_data)

   print(f"File encrypted and saved to: {output_file_path}")

# Specify filenames (no need for absolute paths)
input_filename = "example.txt"
output_filename = "encrypted.txt"  # Change this if desired

# Encrypt the file
encrypt_file(input_filename, output_filename)
