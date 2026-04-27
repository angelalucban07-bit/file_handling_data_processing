RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'
BOLD = '\033[1m'
class StudentGWAReader:
    def __init__(self, filepath="students.txt"):
        self.filepath = filepath

    # We split each line
    def read_students(self) -> list:
        records = []
        with open(self.filepath, 'r') as file:
            for line in file:
                name, gwa = line.strip().split(",")
                records.append((name, float(gwa)))
        return records

    def find_top_students(self, data: list) -> None:
        if not data:
            return print(RED + "No valid student data found.")

    # Finds the record with the minimum GWA
        top_student = min(data, key=lambda x: x[1])
        print(GREEN + "🏆 Highest GWA Found!" + END)
        print(BOLD+f"Student: {top_student[0]}")
        print(f"GWA: {top_student[1]}")
        print(END+GREEN + "Congrats! Ang angas mo!" + END)

if __name__ == "__main__":
    gwa = StudentGWAReader()
    student_data = gwa.read_students()
    gwa.find_top_students(student_data)