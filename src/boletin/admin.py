from django.contrib import admin

# Register your models here.

from .forms import RegModelForm
from .models import Registrado #importacion relativa .model de mismo directorio
# para cambiar la vista administrativa de "Boletin"

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode__", "nombre", "timestamp"]
	form = RegModelForm
	#list_display_links = ["nombre"]
	#list_display = ["email", "nombre", "timestamp"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"] # no se puede editar el email(unique) 
	search_fields = ["email", "nombre"]
	#class Meta:
	#	model = Registrado


admin.site.register(Registrado, AdminRegistrado)