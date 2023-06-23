import os
import random
from django.db import models

def get_filename_ext(filepath):
  base_name = os.path.basename(filepath)
  name, ext = os.path.splitext(base_name)
  return name, ext

def upload_file_path(instance, filename):
  print(instance)
  print(filename)
  new_filename = random.randint(1,99999999)
  name, ext = get_filename_ext(filename)
  final_filename = f'{new_filename}{ext}'
  return f"documentacion/{new_filename}/{final_filename}"



# Create your models here.

class Persona(models.Model):

  dni = models.IntegerField(blank=False, null=False)
  apellidos = models.CharField(max_length=100, blank=True, null=True)
  nombres = models.CharField(max_length=100, blank=True, null=True)
  domicilio_real = models.CharField(max_length=200, blank=True, null=True)
  localidad = models.CharField(max_length=100, blank=True, null=True)
  telefono = models.CharField(max_length=50, blank=True, null=True)
  celular = models.CharField(max_length=50, blank=True, null=True)
  email = models.CharField(max_length=100, blank=True, null=True)
  fecha_nacimiento = models.DateField(blank=True, null=True)
  titulo = models.CharField(max_length=300, blank=True, null=True)

  #class Meta:
  # managed = False
  # db_table = 'persona'

  def __str__(self):
    return '{}, {}'.format(self.apellidos, self.nombres)

class Convocatoria(models.Model):
    CONSEJO = 1
    SECRETARIA = 2
    AREA = [(CONSEJO, "Consejo de la Magistratura"),
            (SECRETARIA, "Secretaria Administrativa",)
            ]
    idarea = models.IntegerField(blank=False, null=False, choices=AREA)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    detalle = models.CharField(max_length=1000, blank=True, null=False)
    estado = models.IntegerField(blank=False, null=False)
    inicio = models.DateField(blank=False, null=False)
    finalizacion = models.DateField(blank=False, null=False)
    link_insc = models.CharField(max_length=200, blank=True, null=True)
    link_acuerdo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
      return '{}, {}'.format(self.nombre, self.descripcion)


class Inscripcion(models.Model):
    persona = models.ForeignKey(Persona,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,
                                related_name='inscripcion')

    convocatoria = models.ForeignKey(Convocatoria,
                                     on_delete=models.DO_NOTHING,
                                     null=True)
    numero = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    idarea = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    base = models.CharField(max_length=100, blank=True, null=True)
    fecha_insc = models.DateTimeField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)

    #class Meta:
    #    managed = False
    #    #abstract = True
    #    db_table = 'inscripcion'
    def mostrar_inscripciones(self):
      return ', '.join([Persona.apellidos for Persona in self.persona.all()[:3]])

    def __str__(self):
      return self.nombre

#class Conv(models.Model):

class Legajo(models.Model):
  persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
  fechacreacion = models.DateTimeField(blank=False, null=False)
  fechaingreso = models.DateField(blank=True, null=True)

class TipoDoc(models.Model):
  tipo = models.CharField(max_length=150, blank=False, null=False)
  vence = models.BooleanField()
  vencedias = models.IntegerField(blank=True, null=True)
  def __str__(self):
    return self.tipo

 # def __str__(self):
  #  return '{} - {} / {} '.format(self.tipodoc, self.vence, self.vencedias)

#def generate_path(instance, filename):
#  folder = "modelo_" + str(instance.user)
#  return os.path.join("adjuntos", folder, filename)

class Documentacion(models.Model):
  tipodoc = models.ManyToManyField(TipoDoc, blank=True )
  persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
  legajo = models.ForeignKey(Legajo, on_delete=models.DO_NOTHING, blank=False, null=False)
  fecha_ingreso= models.DateTimeField(blank=True, null=True)
  fecha_actualizacion=models.DateTimeField(blank=True, null=True)
  archivo = models.FileField(upload_to='documentacion/')

class Archivopdf(models.Model):
  documentacion = models.ForeignKey(Documentacion, on_delete=models.CASCADE,related_name='pdf')
  archivo = models.FileField(upload_to='documentacion/')









