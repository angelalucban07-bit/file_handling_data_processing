class NumberProcessor:
    def __init__(self, filepath="integers.txt"):
        self.source_filepath = source_filepath
        self.even_output_filename = "squares.txt"
        self.odd_output_filename = "cube.txt"

    def process_file(self):
        with open(self.source_filepath, "r") as source_file, \
open(self.even_output_filename, "w") as even_output_file, \
open(self.odd_output_filename, "w") as odd_output_file:
            for line in source_file:
                numbers_strings = line.split()
                    for number_strings in numbers_strings:


