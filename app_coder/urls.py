from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('farmaceuticos', views.farmaceuticos, name='Farmaceuticos'),
    path('clientes', views.clientes, name='Clientes'),
    path('medicamentos', views.medicamentos, name='Medicamentos'),
    path('formHTML', views.form_hmtl),
    path('farmaceutico-django-forms', views.farmaceutico_forms_django, name='FarmaceuticosDjangoForms'),
    path('farmaceutico/<int:pk>/update', views.update_farmaceutico, name='UpdateFarmaceutico'),
    path('farmaceutico/<int:pk>/delete', views.delete_farmaceutico, name='DeleteFarmaceutico'),
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

    path('farmacias', views.FarmaciaListView.as_view(), name='farmacia-list'),
    path('farmacia/add/', views.FarmaciaCreateView.as_view(), name='farmacia-add'),
    path('farmacia/<int:pk>/detail', views.FarmaciaDetailView.as_view(), name='farmacia-detail'),
    path('farmacia/<int:pk>/update', views.FarmaciaUpdateView.as_view(), name='farmacia-update'),
    path('farmacia/<int:pk>/delete', views.FarmaciaDeleteView.as_view(), name='farmacia-delete'),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
    path('register/update', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]