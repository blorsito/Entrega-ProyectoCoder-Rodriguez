from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('farmacias', views.farmacias, name = 'Farmacias'),
    path('farmaceuticos', views.farmaceuticos, name='Farmaceuticos'),
    path('clientes', views.clientes, name='Clientes'),
    path('medicamentos', views.medicamentos, name='Medicamentos'),
    path('formHTML', views.form_hmtl),
    path('farmacia-django-forms', views.farmacia_forms_django, name='FarmaciaDjangoForms'),
    path('farmaceutico-django-forms', views.farmaceutico_forms_django, name='FarmaceuticosDjangoForms'),
    path('medicamento-django-forms', views.medicamento_forms_django, name='MedicamentoDjangoForms'),
    path('cliente-django-forms', views.cliente_forms_django, name='ClienteDjangoForms'),
    path('search', views.search, name='Search'),


    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

]