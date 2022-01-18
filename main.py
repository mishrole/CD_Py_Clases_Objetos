from Student import Student

mitch = Student(1, "Mitchell", "Rodríguez")
print(mitch)
print(mitch.firstname)
mitch.print_info()
print(mitch.average())
print(mitch.program)
gabriel = Student(2, "Gabriel", "Acurio")

# Atributos de Clase:
# La idea es que se mantengan a través de todas las instancias de una clase
print(gabriel.program)
# La actualización directa tiene prioridad sobre la actualización desde la clase
gabriel.program = "Python"
mitch.program = "MERN"

print(mitch.program)
print(gabriel.program)

# Modificando a través de la clase
Student.program = "Java"
print(Student.program)

print(Student.student_list)

Student.printStudents()

# TypeError: printId() missing 1 required positional argument: 'self'
# mitch.printId()

mitch.printBothStudent(gabriel)