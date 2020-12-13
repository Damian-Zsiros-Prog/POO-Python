class Persona:
	def __init__(self,nombres,apellidos,edad):
		self.nombres = nombres
		self.apellidos = apellidos
		self.edad = int(edad)
	def nombreCompleto(self):
		nombres = self.nombres.upper()
		apellidos = self.apellidos.upper()
		print(nombres+" "+apellidos)
	def mayorDeEdad(self):
		edad = self.edad
		if edad >= 18:
			print("Es mayor de edad")
		else:
			print("No es mayor de edad")

persona = Persona("damian","gomez",14)
persona.nombreCompleto()
persona.mayorDeEdad()