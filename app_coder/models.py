from django.contrib.auth.models import User
from django.db import models


class Farmacia(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phonenumber = models.IntegerField()

    def __str__(self):
        return f' Nombre de la farmacia: {self.name} -- Dirección: {self.address} -- Teléfono: {self.phonenumber}'


class Cliente(models.Model):
    name = models.CharField(max_length=40)
    obra_social = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del cliente: {self.name} -- Obra social: {self.obra_social}'


class Farmaceutico(models.Model):
    name = models.CharField(max_length=40)
    matricula = models.IntegerField()
    

    def __str__(self):
        return f'Nombre del Farmacéutico: {self.name} -- Matrícula: {self.matricula}'


class Medicamento(models.Model):
    name = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre del medicamento: {self.name} -- Precio: {self.precio}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'