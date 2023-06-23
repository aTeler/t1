from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Persona, Inscripcion, Documentacion, Archivopdf

class SubirDocumentacionForm(forms.ModelForm):

  class Meta:
    model = Documentacion
    fields = ['fecha_ingreso','tipodoc','archivo']


#
# class Consulta_DNI_MF(ModelForm):
#   def clean_dni(self):
#     data = self.cleaned_data['consulta_dni']
#
#     if data < 999999:
#         raise ValidationError(__('DNI invalido (Faltan numeros'))
#
#     if data > 99999999:
#         raise ValidationError(__('DNI invalido (Sobran numeros)'))
#
#     return data
#
#   class Meta:
#     model = Persona
#     fields = ['consulta_dni',]
#     labels = {'consulta_dni' : _('Cunsulta DNI'), }
#     help_texts = { 'consulta_dni': _('Ingrese DNI para buscar'),}
#
#
#






