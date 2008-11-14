from django.db import models
from DjAdminExt.models import ForeignKeyExt
# Create your models here.
class Pais(models.Model):
    pais= models.CharField(max_length = 40)

    def __unicode__(self):
        return self.pais

class Provincia(models.Model):
    provincia= models.CharField(max_length= 40)
    pais= models.ForeignKey(Pais)

    def __unicode__(self):
        return self.provincia


class Localidad(models.Model):
    localidad = models.CharField (max_length= 40)
    pais = ForeignKeyExt(Pais, bindings=({'detail_model_name':'Provincia',
                                          'detail_field_name':'pro',
                                          'app_name':'Localidades',
                                          'detail_display_field':'provincia'},))
    pro= models.ForeignKey(Provincia, verbose_name= "provincia")

    def __unicode__(self):
        return self.localidad


class Persona(models.Model):
    Nombre = models.CharField(max_length= 40)
    pais = ForeignKeyExt(Pais, bindings=({'detail_model_name':'Provincia',
                                          'detail_field_name':'pro',
                                          'app_name':'Localidades',
                                          'detail_display_field':'provincia'},))
    pro = ForeignKeyExt(Provincia, bindings=({'detail_model_name':'Localidad',
                                          'detail_field_name':'ciudad',
                                          'app_name':'Localidades',
                                          'detail_display_field':'localidad'},))
    ciudad = models.ForeignKey(Localidad)

    def __unicode__(self):
        return self.Nombre
