class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self):
        self.edad += 1
        return f"Ahora tengo {self.edad} años."

    def presentar(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return f"Mi nuevo nombre es {self.nombre}."

    def saludarA(self,nombreotraPersona):
        return f"Hola {self.nombre}. te manda saludar {nombreotraPersona}"

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("Pancho", 28)
persona3 = Persona("Damian", 65)
# Usar algunos de los métodos

print(persona1.saludar())
print(persona1.presentar())
print(persona1.cumplir_anios())
print(persona1.es_mayor_de_edad())
print(persona1.cambiar_nombre("Carlos"))

print(persona2.saludar())
print(persona2.presentar())
print(persona2.cumplir_anios())
print(persona2.es_mayor_de_edad())
print(persona2.cambiar_nombre("Francisco"))

print(persona3.saludar())
print(persona3.presentar())
print(persona3.cumplir_anios())
print(persona3.es_mayor_de_edad())
print(persona3.cambiar_nombre("El DM"))

print(persona1.saludarA(persona2.nombre))