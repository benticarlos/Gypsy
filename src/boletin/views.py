from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "Bienvenidos a Gypsy" #se utiliza en el context
	if request.user.is_authenticated:
		titulo = "Bienvenid@ %s" %(request.user)
		# titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	#print (dir(form))

	context = {
		"titulo": titulo,
		"el_form": form,
	}

	if form.is_valid():
		instace = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instace.nombre:
			instace.nombre = "PERSONA"
		instace.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		if not nombre:
			context = {
			"titulo": "Gracias %s!" %(email)
		}

		###### Para python3
		print (instace)
		print (instace.timestamp)
		##### Para python2
		#print instace
		#print instace.timestamp
	    #form_data = form.cleaned_data
	    #abc = form_data.get("email")
	    #abc2 = form_data.get("nombre")
	    #obj = Registrado.objects.create(email=abc, nombre=abc2)
	    

	    #otra manera de almacenar los datos
	    #obj = Registrado()
	    #obj.email = abc
	    #obj.save()
	
	if request.user.is_authenticated() and request.user.is_staff:
		#for instace in Registrado.objects.all():
			# print(instace.nombre) # cada instancia de Registrado (en modelo)
		queryset = Registrado.objects.all().order_by("-timestamp") 
		#.filter(nombre__icontains="pe")
		#.filter(email__iexact="consulta")
		context = {
			"queryset": queryset, #query
		}
	return render(request, "inicio.html", context)
	#return render(request, "inicio.html", {}) # {} diccionario vacio

# luego hacer el llamado en url.py
# con la sig lineas:
	# from boletin import views
	# url(r'^$', views.inicio, name='inicio')

#se crea una vista para ContactForm
def contact(request):
	titulo = "Contacto"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "wunjo.listas@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			#fail_silently=True
			fail_silently=False #para funcionar sin servidor mail
			)
		#print (email, mensaje, nombre)
		########## similar al codigo anterior
		# for key in form.cleaned_data:
		# 	print (key)
		# 	print (form.cleaned_data.get(key))
		########## otra manera mas de hacerlo
		#for key, value in form.cleaned_data.iteritems(): #python2
		# for key, value in form.cleaned_data.items():
		# 	print (key, value)
	context = {
		"form": form,
		"titulo": titulo,
	}
	return render(request, "forms.html", context)
