class User:

    def __init__(self,id,nombre,apellido,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"User: {self.id} {self.nombre} {self.apellido} {self.edad}"