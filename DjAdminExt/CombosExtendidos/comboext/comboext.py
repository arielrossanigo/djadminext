from django import forms
from django.db import models
from django.contrib.admin.models import models

class MiForeignWidget(forms.Select):
    '''Clase para extender el widget Select estandar con las nuevas funcionalidades'''
    
    def __init__(self, bindings ,attrs=None, choices=()):
        '''
        Se necesitan los bindings para menejar la consulta, el resto depende de
        la clase padre (Select)
        
        bindings: Instancia con los datos para realizar la consulta sobre la vista
                  y actualizar los campos correspondientes.
        '''
        self.bindings = bindings
        super(MiForeignWidget, self).__init__(attrs, choices)

    def render (self, name, value, attrs=None, choices=()):
        '''
        Los parametros dependen de la clase padre.
        la funcion genera contenido extra mediante los bindings para utilizar 
        el contenido JS
        '''
        onchange= []
        for b in self.bindings:
            onchange.append("populateSelect('%s', 'id_%s', 'id_%s', '%s', '%s', '%s_set', '%s');"%(
                b.url, name, b.detail_field_name, b.app_name, b.master_model_name, b.detail_model_name.lower(), b.detail_display_field))
        att={}
        if len(onchange)!=0:
            att['onChange']= ' '.join(onchange)
        att.update(attrs)
        return super(MiForeignWidget,self).render(name, value, att, choices)

class Binding(object):
    '''Clase para hacer bindings entre campos MiForeignKey'''
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

class MiForeignKey(models.ForeignKey):
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
        super(MiForeignKey, self).__init__(to, to_field, rel_class, **kwargs)

    def formfield(self,**kwargs):
        '''Se presetea el widget del field para usar el nuevo'''
        defaul = {'widget': MiForeignWidget(self.bindings)}
        defaul.update(kwargs)
        return super(MiForeignKey, self).formfield(**defaul)
