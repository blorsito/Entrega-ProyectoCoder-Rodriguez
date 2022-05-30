from django.db import models


class Farmacia(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phonenumber = models.IntegerField()

    def __str__(self):
        return f' Nombre de la farmacia: {self.name} -- Direccion: {self.address} -- Telefono: {self.phonenumber}'


class Cliente(models.Model):
    name = models.CharField(max_length=40)
    obra_social = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del Estudiante: {self.name} -- Obra social: {self.obra_social}'


class Farmaceutico(models.Model):
    name = models.CharField(max_length=40)
    matricula = models.IntegerField()
    

    def __str__(self):
        return f'Nombre del Farmaceutico: {self.name} -- Matricula: {self.matricula}'


class Medicamento(models.Model):
    name = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre del medicamento: {self.name} -- Precio: {self.precio}'