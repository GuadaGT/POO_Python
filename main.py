class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def info_alumno(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def resultado_alumno(self):
        if self.nota >= 5:
            print("¡Enhorabuena!", self.nombre, "ha aprobado con un", self.nota, "de nota final.")
        else:
            print("Lo lamento.", self.nombre, "ha suspendido con un", self.nota, "de nota final.")

a1 = Alumno("Laura", 8)
a1.info_alumno()
a1.resultado_alumno()

a2 = Alumno("Gloria", 4.5)
a2.info_alumno()
a2.resultado_alumno()
