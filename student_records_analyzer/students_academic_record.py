class StudentGWAReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_students(self):
        students = []
        with open(self.filepath, 'students.txt') as file:
            for line in file:
                student_name, student_gwa = line.strip().split(',')
                self.student_records.append((student_name, float(student_gwa)))

    def find_top_students(self):
        lowest_gwa_value = min(student_gwa for student_name, student_?gwa in sel.student_records)
        top_students = [
            (student_name, student_gwa)
            for student_name, student_gwa in self.student_records
            if student_gwa == lowest_gwa_value
        ]
        return top_students, lowest_gwa_value

    def display_results(self):
        top_students, lowest_gwa_value = self.find_top_students()
        print('Top students:')
        for student_name, student_gwa in top_students:
            print(f'{student_name}: {student_gwa}')
            print('-' * len(student_gwa))