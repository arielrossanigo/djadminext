from django.contrib import admin
from Localidades.models import Pais, Provincia, Localidad, Persona

class LocalidadAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/jquery.js','/media/js/combo.js')

class PersonaAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/jquery.js','/media/js/combo.js')

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Persona, PersonaAdmin)
