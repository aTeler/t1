from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy, reverse
from django.forms.models import inlineformset_factory
from django.db.models.manager import Manager
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from .models import Persona,Inscripcion, Convocatoria, Legajo , Documentacion
from .forms import SubirDocumentacionForm


InscripcionFormset = inlineformset_factory(Persona, Inscripcion, fields='__all__')
DocumentacionFormset = inlineformset_factory(Legajo, Documentacion, fields='__all__')

def index(request):
  num_personas = Persona.objects.all().count()
  num_inscripciones = Inscripcion.objects.all().count()

  return render(request,
                'index.html',
                context= {'num_personas' : num_personas,
                          'num_inscripciones' : num_inscripciones
                          },
                )

def personasbuscar(request):
  #print(request.GET)
  queryset = request.GET.get("buscar")
  persona = Persona.objects.all()

  print(queryset)
  print(persona)
  #print(inscripciones)
  if queryset:
    persona = Persona.objects.filter(
      Q(apellidos__icontains= queryset) |
      Q(nombres__icontains= queryset) |
      Q(dni__icontains=queryset)
    ).distinct()

  return render(request,'persona_buscar.html', {'Persona' : persona })

def inscripcioneslistar(request):
  inscripcion = Inscripcion.objects.all()
  print(inscripcion)
  return render(request,'inscripciones_listar.html', {'Inscripcion' : inscripcion})

def legajos(request):
  #print(request.GET)
  queryset = request.GET.get("buscar")
  legajos =  Legajo.objects.all()

  print(queryset)
  print(legajos)
  #print(inscripciones)
  if queryset:
    legajos = Legajo.objects.filter(
      Q(persona__apellidos__icontains= queryset) |
      Q(persona__nombres__icontains= queryset) |
      Q(persona__dni__icontains=queryset)
    ).distinct()

  return render(request,'legajo_buscar.html', {'Legajo' : legajos })


def subir_archivo(request):
  if request.method == 'POST':
    form = SubirArchivoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      message = "Archivo subio correctamente!"
      #archivosubido_url =
  else:
    form = SubirArchivoForm()
  return render_to_response('')



class PersonaListar(ListView):

  template_name = 'persona_lista.html'
  model = Persona


class PersonaCrear(CreateView):
  model = Persona
  fields = '__all__'
  template_name = "persona_form.html"
  success_url = reverse_lazy('listar')

class PersonaActualizar(UpdateView):
  model = Persona
  fields = '__all__'
  template_name = "persona_form.html"
  success_url = reverse_lazy('listar')

class PersonaInscripciones(UpdateView):
  model = Persona
  fields = '__all__'
  template_name = "persona_inscripciones_form.html"
  queryset = Persona.objects.filter()

  def get_queryset(self):

    queryset = super().get_queryset()

    queryset = queryset.filter(pk=self.kwargs['pk'])
    return queryset

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data["inscripcion"] = InscripcionFormset(self.request.POST)
    else:
      data["inscripcion"] = InscripcionFormset(instance=self.object)
    return data

  def form_valid(self, form):
    context = self.get_context_data()
    inscripcion = context["inscripcion"]
    self.object = form.save()
    if inscripcion.is_valid():
      inscripcion.instance = self.object
      inscripcion.save()
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy("listar")



class LegajoListView(ListView):
  model = Documentacion
  fields = '__all__'
  template_name = "legajo_documentacion_form.html"
  queryset = Documentacion.objects.filter()
  print(queryset)
  print(str(queryset.query))
  print(Documentacion.legajo)
  context_object_name = 'documentacion'

  #model = Persona
  #fields = '__all__'
  #template_name = "persona_inscripciones_form.html"
  #queryset = Persona.objects.filter()


def subir_documentacion(request):
  print(request)
  legajo=get_object_or_404(Legajo, pk=legajo_id)

  #legajo = Legajo.objects.get(id=request.legajo_id)

  if request.method == 'POST':
      form = SubirDocumentacionForm(request.POST, request.FILES)

      if form.is_valid():
        archivo = form.save(commit=False)
        archivo.legajo = legajo
        archivo.save()
        return reversed('legajo')

  else:
      form = SubirDocumentacionForm()
  return render(request, 'legajo_documentacion_subir.html', {'form': form })




class LegajoDocumentacion(UpdateView):
  model = Legajo
  fields = '__all__'
  template_name = "legajo_documentacion_form.html"
  queryset = Legajo.objects.filter()

  def get_queryset(self):

    queryset = super().get_queryset()

    queryset = queryset.filter(pk=self.kwargs['pk'])
    return queryset

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data["documentacion"] = DocumentacionFormset(self.request.POST)
    else:
      data["documentacion"] = DocumentacionFormset(instance=self.object)
    return data

  def form_valid(self, form):
    context = self.get_context_data()
    documentacion = context["documentacion"]
    self.object = form.save()
    if documentacion.is_valid():
      documentacion.instance = self.object
      documentacion.save()
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy("legajo")



# def consulta_por_dni(request, pk):
#
#     persona=get_object_or_404(Persona, dni= pk)
#
#     return render(request, 'persona_form.html', {'persona': persona })

# Legajos - Subir

def subir_archivo(request, legajo_id):
    legajo = Legajo.objects.get(id=legajo_id)

    if request.method == 'POST':
      form = ArchivoForm(request.POST, request.FILES)
      if form.is_valid():
        archivo = form.save(commit=False)
        archivo.legajo = legajo
        archivo.save()
        return redirect('legajo', legajo_id=legajo_id)
    else:
      form = ArchivoForm()

    archivos = proyecto.archivo_set.all()

    return render(request, 'subir_archivo.html', {'form': form, 'archivos': archivos})


########################################################
# Convocatorias                                        #
########################################################
class ConvocatoriaListar(ListView):
  template_name = 'convocatoria_lista.html'
  model = Convocatoria


class ConvocatoriaCrear(CreateView):
  model = Convocatoria
  fields = '__all__'
  template_name = "convocatoria_form.html"
  success_url = reverse_lazy('conv_listar')





