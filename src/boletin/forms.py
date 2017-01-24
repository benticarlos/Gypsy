from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre","email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utiliza un email con la extensión .edu")
		return email	

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre
		
class ContactForm(forms.Form):
	#nombre = forms.CharField(max_length=100)
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	#edad = forms.IntegerField()
	mensaje = forms.CharField(widget=forms.Textarea)
