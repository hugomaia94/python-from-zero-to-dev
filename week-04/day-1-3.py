class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def status(self):
        if self.calculate_average() >= 7:
            return "Approved"
        else:
            return "Failed"
