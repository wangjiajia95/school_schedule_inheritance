class Cohort:    
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def student_summaries(self):
        summaries = f"Students in {self.name}:\n"
        for student in self.students:
            summaries += student.summary() + "\n"
        return summaries