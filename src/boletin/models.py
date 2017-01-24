from django.db import models

# Create your models here.
class Registrado(models.Model):
	# blank para quedar en blanco en el form y null en blanco en la BD
	nombre = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	

	def __unicode__(self): # para python2
		return self.email #unique

	def __str__(self): # para python3
		return self.email


# Para ejecutar se debe migrar la aplicacion y BD
# python manage.py makemigrations  -> busca las modificaciones y empaqueta
# python manage.py migrate

# Para manejar la BD ejecutamos
# python manage.py shell
# >>> from boletin.models import Registrado -> seleccionamos
# >>> gente = Registrado.objects.all() -> variable de busqueda
# >>> gente  -> ejecuta la busqueda de la variable creada
# >>> persona1 = Registrado.objects.create(nombre='Carlos', email='c@email.com') -> registramos
# >>> persona1  -> ejecutamos