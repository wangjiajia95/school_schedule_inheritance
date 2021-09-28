from school_schedule.middle_school_student import MiddleSchoolStudent
from school_schedule.high_school_student import HighSchoolStudent

# first instance
quinn = MiddleSchoolStudent(
                "Quinn", 
                "8th grader", 
                [
                    "Social Studies", 
                    "Science", 
                    "Algebra", 
                    "Gym", 
                    "English", 
                    "Shop"
                ],
                gets_transportation=True
            )

quinn.add_class("Painting")

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )

students = [quinn, claire]
for student in students:
    print(student.summary())