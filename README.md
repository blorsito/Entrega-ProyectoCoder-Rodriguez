
# Proyecto Curso Python CoderHouse
```bash
Este proyecto fue realizado por Pablo Rodríguez como entrega final para el curso dictado durante marzo, abril,
mayo y junio de 2022.
En este blog se encuentra información sobre farmacias, farmacéuticos, clientes y obras sociales de la provincia de Buenos Aires.
Tiene un login donde podes registrarte y elegir un avatar para tu cuenta. Se puede agregar, editar y eliminar farmacias con todos
sus datos. El usuario tambien puede agregar, editar y eliminar farmacéuticos. 

Ver online: https://coderproject-django-pcpr.herokuapp.com/

```

# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/blorsito/Entrega-ProyectoCoder-Rodriguez.git

cd django-coderhouse-project

git checkout entrega1

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
