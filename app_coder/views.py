import os
import random
import string
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

from app_coder.models import Farmacia, Cliente, Farmaceutico, Medicamento, Avatar
from app_coder.forms import FarmaciaForm, FarmaceuticoForm, MedicamentoForm, ClienteForm, AvatarForm

from django.contrib import messages


def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html"
    )

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def farmaceuticos(request):
    farmaceuticos = Farmaceutico.objects.all()

    context_dict = {
        'farmaceuticos': farmaceuticos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/farmaceuticos.html"
    )


def farmacias(request):
    farmacias = Farmacia.objects.all()

    context_dict = {
        'farmacias': farmacias
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/farmacias.html"
    )


def clientes(request):
    clientes = Cliente.objects.all()

    context_dict = {
        'clientes': clientes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/clientes.html"
    )


def medicamentos(request):
    medicamentos = Medicamento.objects.all()

    context_dict = {
        'medicamentos': medicamentos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/medicamentos.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        farmacia = Farmacia(name=request.POST['name'], address=request.POST['address'], phonenumber=request.POST['phonenumber'])
        farmacia.save()

        farmacias = Farmacia.objects.all()
        context_dict = {
            'farmacias': farmacias
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/farmacias.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def farmacia_forms_django(request):
    if request.method == 'POST':
        farmacia_form = FarmaciaForm(request.POST)
        if farmacia_form.is_valid():
            data = farmacia_form.cleaned_data
            farmacia = Farmacia(name=data['name'], address=data['address'], phonenumber=data['phonenumber'])
            farmacia.save()

            farmacias = Farmacia.objects.all()
            context_dict = {
                'farmacias': farmacias
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/farmacias.html"
            )

    farmacia_form = FarmaciaForm(request.POST)
    context_dict = {
        'farmacia_form': farmacia_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/farmacia_django_forms.html'
    )

@login_required
def farmaceutico_forms_django(request):
    if request.method == 'POST':
        farmaceutico_form = FarmaceuticoForm(request.POST)
        if farmaceutico_form.is_valid():
            data = farmaceutico_form.cleaned_data
            farmaceutico = Farmaceutico(
                name=data['name'],
                matricula=data['matricula'],
            )
            farmaceutico.save()

            farmaceuticos = Farmaceutico.objects.all()
            context_dict = {
                'farmaceuticos': farmaceuticos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/farmaceuticos.html"
            )

    farmaceutico_form = FarmaceuticoForm(request.POST)
    context_dict = {
        'farmaceutico_form': farmaceutico_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/farmaceutico_django_forms.html'
    )

@login_required
def update_farmaceutico(request, pk: int):
    farmaceutico = Farmaceutico.objects.get(pk=pk)

    if request.method == 'POST':
        farmaceutico_form = FarmaceuticoForm(request.POST)
        if farmaceutico_form.is_valid():
            data = farmaceutico_form.cleaned_data
            farmaceutico.name = data['name']
            farmaceutico.matricula = data['matricula']
            farmaceutico.save()

            farmaceuticos = Farmaceutico.objects.all()
            context_dict = {
                'farmaceuticos': farmaceuticos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/farmaceuticos.html"
            )

    farmaceutico_form = FarmaceuticoForm(model_to_dict(farmaceutico))
    context_dict = {
        'farmaceutico': farmaceutico,
        'farmaceutico_form': farmaceutico_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/farmaceutico_form.html'
    )

@login_required
def delete_farmaceutico(request, pk: int):
    farmaceutico = Farmaceutico.objects.get(pk=pk)
    if request.method == 'POST':
        farmaceutico.delete()

        farmaceuticos = Farmaceutico.objects.all()
        context_dict = {
            'farmaceuticos': farmaceuticos
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/farmaceuticos.html"
        )

    context_dict = {
        'farmaceutico': farmaceutico,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/farmaceutico_confirm_delete.html'
    )

def medicamento_forms_django(request):
    if request.method == 'POST':
        medicamento_form = MedicamentoForm(request.POST)
        if medicamento_form.is_valid():
            data = medicamento_form.cleaned_data
            medicamento = Medicamento(
                name=data['name'],
                precio=data['precio'],
            )
            medicamento.save()

            medicamentos = Medicamento.objects.all()
            context_dict = {
                'medicamentos': medicamentos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/medicamentos.html"
            )

    medicamento_form = MedicamentoForm(request.POST)
    context_dict = {
        'medicamento_form': medicamento_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/medicamento_django_forms.html'
    )

def cliente_forms_django(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            data = cliente_form.cleaned_data
            cliente = Cliente(
                name=data['name'],
                obra_social=data['obra_social'],
            )
            cliente.save()

            clientes = Cliente.objects.all()
            context_dict = {
            'clientes': clientes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/clientes.html"
            )

    cliente_form = ClienteForm(request.POST)
    context_dict = {
            'cliente_form': cliente_form
    }
    return render(
            request=request,
            context=context_dict,
            template_name='app_coder/cliente_django_forms.html'
    )

def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(address__contains=search_param), Q.OR)
        farmacias = Farmacia.objects.filter(query)
        context_dict = {
            'farmacias': farmacias
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class FarmaciaListView(ListView):
    model = Farmacia
    template_name = "app_coder/farmacia_list.html"


class FarmaciaDetailView(DetailView):
    model = Farmacia
    template_name = "app_coder/farmacia_detail.html"


class FarmaciaCreateView(LoginRequiredMixin, CreateView):
    model = Farmacia
    success_url = reverse_lazy('app_coder:farmacia-list')
    fields = ['name', 'address', 'phonenumber']


class FarmaciaUpdateView(LoginRequiredMixin, UpdateView):
    model = Farmacia
    success_url = reverse_lazy('app_coder:farmacia-list')
    fields = ['name', 'address', 'phonenumber']


class FarmaciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmacia
    success_url = reverse_lazy('app_coder:farmacia-list')
    fields = ['name', 'address', 'phonenumber']


from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from app_coder.forms import UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario Registrado satisfactoriamente."},
                template_name="app_coder/login.html",
            )
    # form = UserCreationForm()
    else:
        form = UserRegisterForm() #Aca meti el else
    return render(
        request=request,
        context={"form":form},
        template_name="app_coder/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "app_coder/home.html"
        else:
            template_name = "app_coder/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("app_coder:Home")

@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return redirect('app_coder:Home')

    form = UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('app_coder:Home')

    form = AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_coder/avatar_form.html",
    )