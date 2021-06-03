class Matricula:
    def __init__(self, codigoMatricula, nombreCompleto, direccion, telefono, curso):
        self.CodigoMatricula = codigoMatricula
        self.NombreCompleto = nombreCompleto
        self.Direccion = direccion
        self.Telefono = telefono
        self.Curso = curso
        self.matriculaPersona = {}

    def inscripcion(self):
        self.matriculaPersona['Codigo Matricula'] = self.CodigoMatricula
        self.matriculaPersona['Nombre completo'] = self.NombreCompleto
        self.matriculaPersona['Direccion'] = self.Direccion
        self.matriculaPersona['Telefono'] = self.Telefono
        self.matriculaPersona['Curso'] = self.Curso
        return 'Se Agrego la matricula'

    def consulta(self):
        return f'Matricula consultada correctamente {self.matriculaPersona}'

    def eliminar(self):
       
        return f'Matricula eliminada correctamente { self.matriculaPersona.clear()}'



matricula = Matricula(1,'juan david molina gonzalez','cra 50', 3344445, 'programacion')

print(matricula.NombreCompleto)
print(matricula.inscripcion())
print(matricula.consulta())
print(matricula.eliminar())
print(matricula.matriculaPersona)
