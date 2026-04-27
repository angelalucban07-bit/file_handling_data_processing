class NumberProcessor:
    def __init__(self):
        self.source_file = "integers.txt"
        self.even_output_file = "double.txt"
        self.odd_output_file = "triple.txt"

    def output_files(self):
        with open(self.source_file, "r") as source_file, \
            open(self.even_output_file, "w") as even_output_file, \
            open(self.odd_output_file, "w") as odd_output_file:

            for line in source_file:
                number_value = int(line.split())
