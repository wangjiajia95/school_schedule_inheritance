from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, 
        gets_transportation = False, clubs = None):
        
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
        self.clubs = clubs if clubs is not None else []

    def summary(self):
        return "".join((super().summary(), self.display_transportation(), self.display_clubs()))

    def display_transportation(self):
        if self.gets_transportation:
            return f"{self.name} {self.gets_transportation} get transportation"
    
    def display_clubs(self):
        return f"{self.name} is a member of {self.clubs}"


