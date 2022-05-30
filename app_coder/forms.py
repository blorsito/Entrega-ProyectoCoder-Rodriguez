import datetime
from django import forms
from django.forms import ModelForm


class FarmaciaForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    address = forms.CharField(max_length=40, min_length=3, label='Direccion')
    phonenumber = forms.IntegerField(label='Telefono')


class FarmaceuticoForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    matricula = forms.IntegerField(label='Matricula')
   

class MedicamentoForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del medicamento')
    precio = forms.IntegerField(label='Precio')

class ClienteForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    obra_social = forms.CharField(max_length=40, min_length=3, label='Obra social')
