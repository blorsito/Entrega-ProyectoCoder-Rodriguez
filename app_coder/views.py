from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_coder.models import Farmacia, Cliente, Farmaceutico, Medicamento
from app_coder.forms import FarmaciaForm, FarmaceuticoForm, MedicamentoForm, ClienteForm


def index(request):
    return render(request, "app_coder/home.html")


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
                template_name="app_coder/medicamento.html"
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
    context_dict = dict()
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
