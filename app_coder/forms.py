import datetime
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from app_coder.models import Avatar


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

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )