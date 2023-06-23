from django.contrib import admin

# Register your models here.

from .models import Persona, Inscripcion, Legajo, Documentacion, TipoDoc, Archivopdf, Convocatoria


class Detalle_Inscripciones(admin.TabularInline):
  model = Inscripcion

class Inscripto_Admin(admin.ModelAdmin):
  inlines = (Detalle_Inscripciones,)


#admin.site.register(Persona)
admin.site.register(Inscripcion)
admin.site.register(Persona,Inscripto_Admin)
admin.site.register(Legajo)
admin.site.register(TipoDoc)
admin.site.register(Archivopdf)
admin.site.register(Convocatoria)
admin.site.register(Documentacion)
