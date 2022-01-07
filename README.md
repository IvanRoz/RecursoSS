# Recurso didactico de servicio social
Recurso Didactico de la materia Desarrollo de Sistemas Distribuidos

```sh
git clone https://github.com/IvanRoz/RecursoSS
cd RecursoSS
source venv/bin/activate
black -l 110 . #linter
pyton manage.py makemigrations && python manage.py migrate 
python manage.py createsuperuser # create admin user
python manage.py runserver # run server

Si no estan instaladas las dependencias en el entorno virtual usar
pip install -r requirements.txt

```
