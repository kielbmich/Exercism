plants = {"G" : "Grass", "C" : "Clover", "R" : "Radishes", "V" : "Violets"}

class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
    
    def plants(self, student):
        position = self.students.index(student)   
        student_plants = self.diagram[0][2 * position : 2 * position + 2] + self.diagram[1][2 * position : 2 * position + 2]    
        return [plants.get(plant) for plant in student_plants]