class Grader:
    def __init__(self, grades: list[list[float]]):
        self.grades = grades

    def compute(self):
        return [
            self.transform_raw(self.compute_student(student)) for student in self.grades
        ]

    def compute_student(self, student_grades: list[float]):
        return sum(student_grades) / len(student_grades)

    def transform_raw(self, raw: float):
        if raw < 60:
            return "5.00"
        elif ...:
            ...


class CancelTheLowestGrader(Grader):
    def compute_student(self, student_grades: list[float]):
        filtered_grades = sorted(student_grades)[1:]
        return sum(filtered_grades) / len(filtered_grades)


class FloorGrader(Grader):
    def __init__(self, grades: list[list[float]], floor: float):
        super().__init__(grades)
        self._floor = floor

    def compute_student(self, student_grades: list[float]):
        with_floor = [max(g, self._floor) for g in student_grades]

        return sum(with_floor) / len(with_floor)
