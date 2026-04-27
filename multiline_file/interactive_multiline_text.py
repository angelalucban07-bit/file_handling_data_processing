BOLD = '\033[1m'
BLUE = '\033[34m'
END = '\033[0m'
class NoteWriter:
    def __init__(self, filename="notepad.txt"):
        self.filename = filename

    def write_lines(self):
        # 'w' mode = write (creates file)
        my_file = open(self.filename, "w")

        while True:
            line = input(BLUE + "Enter a line: ")
            my_file.write(line + "\n")

            choice = input("Are there more lines (y/n)? "+END).lower()
            if choice == 'n':
                break

        my_file.close()
        print(BOLD + "File saved successfully.")

# run the program
if __name__ == "__main__":
    writer = NoteWriter()
    writer.write_lines()