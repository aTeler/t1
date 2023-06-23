from django.urls import path, include
from . import views
from .views import PersonaListar, PersonaActualizar , PersonaCrear, PersonaInscripciones, ConvocatoriaListar,\
  ConvocatoriaCrear, personasbuscar, inscripcioneslistar, subir_archivo, legajos, LegajoDocumentacion, LegajoListView, subir_documentacion


urlpatterns = [
 # url(r'^$',PersonaListar.as_view(), name='listar'),
  #url(r'^editar/(?P<pk>\d+)$',PersonaActualizar.as_view(), name='editar'),
  #url(r'^nuevo$',PersonaCrear.as_view(), name='crear'),

  path('', views.index, name='index'),
  path('listar/', PersonaListar.as_view(), name='listar'),
  path('editar/<int:pk>/', PersonaActualizar.as_view(), name='editar'),
  path('crear/' , PersonaCrear.as_view(), name='crear'),
  path('inscripciones/<int:pk>/', PersonaInscripciones.as_view(), name='inscripciones'), #
  path('listar_convocatorias/', ConvocatoriaListar.as_view(), name='conv_listar'),
  path('crear_convocatoria/', ConvocatoriaCrear.as_view(), name='conv_crear'),
  path('cuentas/', include('django.contrib.auth.urls')),
  path('buscar_persona', personasbuscar, name='buscar_persona' ),
  path('inscripciones_listar/',inscripcioneslistar, name = 'inscripciones_listar') ,
  path('legajo/', legajos, name='legajo' ),
  path('legajo/subir_documentacion/<int:pk>', subir_documentacion, name='subir_documentacion'),
  path('documentacion/<int:pk>/', LegajoListView.as_view() , name='documentacion'), #

  #path('documentacion/<int:pk>/', LegajoDocumentacion.as_view() , name='documentacion'),
  #path('consulta/<int:pk>',views.ConsultaDNI, name='consulta'),

]


