class Student:
    # Class Attributes
    program = "Web Development 3 Full-Stack"
    student_list = []
    # Constructor
    def __init__(self, id = 0, firstname = "N/A", lastname = "N/A"):
        # Attributes
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.ratings = [18,19,20]
        # Append current instance
        Student.student_list.append(self)
    # Methods
    def print_info(self):
        print(f'Id: {self.id} | Firstname: {self.firstname} | Lastname: {self.lastname}')

    def setId(self, id):
        self.id = id
        
    def setFirstname(self, firstname):
        self.firstname = firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def getId(self):
        return self.id
    
    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname
    
    def average(self):
        sum = 0
        for x in self.ratings:
            sum += x
        final = sum / len(self.ratings)
        return final
    # Class Method
    @classmethod
    def printStudents(cls):
        for student in cls.student_list:
            student.print_info()

    # Class Association
    def printBothStudent(self, student2):
        self.print_info()
        student2.print_info()

    # No tiene acceso a los atributos de la clase
    # Genera error al usarlo desde la instancia
    # @staticmethod
    # def printId(self):
    #     print(self.id)