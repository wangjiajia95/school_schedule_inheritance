from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_add_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    new_class = "Writing"

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    ellis.add_class(new_class)

    # Assert
    assert len(ellis.classes) == 2

def test_get_num_classes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Writing"]
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Act
    num_classes = ellis.get_num_classes()

    # Assert
    assert num_classes == 2

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = []

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 0 classes: \nEllis gets transportation"

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = []

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    summary = ellis.summary()

    assert summary == "Ellis is a junior enrolled in 0 classes: \nEllis doesn't get transportation"
