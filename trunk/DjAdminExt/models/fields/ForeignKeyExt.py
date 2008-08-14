from django.db import models
from DjAdminExt import forms

class ForeignKeyExt(models.ForeignKey):
    '''Clase para extender el field ForeignKey con funcionalidades extras'''

    def __init__(self, to, to_field=None, rel_class=models.ManyToOneRel, **kwargs):
        '''
        Los parametros dependen de la clase padre (ForeignKey).
        Se necesita que se indique el parametro bindings con la lista de
        parametros requeridos para actualizar cada campo.
        '''
        bindings = kwargs.pop('bindings', list)
        app_name=''
        if isinstance(to, basestring):
            if to.index('.') > 0:
                app_name, model_name= to.split('.')
            else:
                model_name= to
        else:
            model_name= to._meta.object_name
        self.bindings=[]
        for attrs in bindings:
            if not attrs.has_key('app_name'):
                attrs['app_name']= app_name
            self.bindings.append(Binding(master_model_name=model_name, **attrs))
        super(ForeignKeyExt, self).__init__(to, to_field, rel_class, **kwargs)

    def formfield(self,**kwargs):
        '''Se determina el formField a utilizar'''
        defaults = {'form_class': forms.ForeignKeyExt, 'bindings': self.bindings}
        defaults.update(kwargs)
        return super(ForeignKeyExt, self).formfield(**defaults)


class Binding(object):
    '''Clase para hacer bindings entre campos ForeignKeyExt'''
    def __init__(self, url='/MasterDetailCombo/', app_name='', master_model_name='', detail_model_name='',
                detail_field_name='', detail_display_field=''):
        '''
        url: URL de la vista a consultar, ej: /MasterDetailCombo (vista generica)
        app_name: Nombre de la aplicacion que contiene el modelo del master
        master_model_name: Nombre del modelo master
        detail_model_name: Nombre del modelo detalle
        detail_field_name: Nombre del campo que se va a actualizar
        detail_display_field: Nombre del campo del detalle que se va a mostrar en el combo
        '''
        self.url=url
        self.app_name= app_name
        self.master_model_name = master_model_name
        self.detail_model_name= detail_model_name
        self.detail_field_name = detail_field_name
        if detail_display_field == '':
            self.detail_display_field= detail_field_name
        else:
            self.detail_display_field= detail_display_field

