from django import forms

class SelectAJAX(forms.Select):
    '''Clase para extender el widget Select estandar con funcionalidades de filtrado por AJAX'''

    def __init__(self, bindings ,attrs=None, choices=()):
        '''
        Se necesitan los bindings para menejar la consulta, el resto depende de
        la clase padre (Select)

        bindings: Instancia con los datos para realizar la consulta sobre la vista
                  y actualizar los campos correspondientes.
        '''
        self.bindings = bindings
        super(SelectAJAX, self).__init__(attrs, choices)

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
        return super(SelectAJAX,self).render(name, value, att, choices)
