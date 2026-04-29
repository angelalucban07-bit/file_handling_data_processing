class NumberSorter:
    def __init__(self, target_file="numbers.txt"):
        # The constructor sets the target file name
        self.target_file = target_file

    def sort_and_save(self):
        try:
            #Open the file manually
            my_file = open(self.target_file, "r")
            numbers = []
            #Use a for loop to read each line
            for line in my_file:
                if line.strip():
                    numbers.append(int(line.strip()))

            #closing the file manually
            my_file.close()
            even_file = open("even.txt", "w")
            odd_file = open("odd.txt", "w")

            for number in numbers:
                if number % 2 == 0:
                    even_file.write(str(number) + "\n")
                else:
                    odd_file.write(str(number) + "\n")

            # Closing output files
            even_file.close()
            odd_file.close()

            print("✅ Success! Numbers sorted into even.txt and odd.txt.")

        except FileNotFoundError:
            print(f" Error: The file '{self.target_file}' was not found.")
        except ValueError:
            print(" Error: The file contains data that isn't an integer.")
        except Exception as unexpected_error:
            print(f" An unexpected error occurred: {unexpected_error}")

if __name__ == "__main__":
    sorter = NumberSorter("numbers.txt")
    sorter.sort_and_save()