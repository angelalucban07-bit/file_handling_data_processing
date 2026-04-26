class StudentGWAReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_students(self):
        students = []
        with open(self.filepath, 'students.txt') as file:
            for line in file:
                name, gwa = line.strip().split(',')
                students.append({'name': name, 'gwa': gwa})
        return students