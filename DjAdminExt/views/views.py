from django.db import models
from django.core import serializers
from django.http import HttpResponse

def master_detail(request, id_master=None, app_name= '', model_name= '', name_set='', field_name=''):
    '''
    Vista generica para retornar un par de valores (PK, Text)

    id_master: id del master por el cual se obtendran los hijos
    app_name: nombre de la aplicacion del modelo master
    model_name: nombre del modelo a consultar
    name_set: nombre del set que contiene a los hijos a mostrar
    field_name: campo del modelo hijo a mostrar
    '''
    if id_master:
        model= models.get_model(app_name, model_name)
        master= model.objects.get(id= id_master)
        se = master.__getattribute__(name_set)
        data = serializers.serialize('json', se.all(), fields=(field_name))
        return HttpResponse(data)
    else:
        return HttpResponse(str([]))
