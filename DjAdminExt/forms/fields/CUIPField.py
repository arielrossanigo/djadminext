from django import forms

class CUIPField(forms.IntegerField):

    def widget_attrs(self, widget):
        res= super(CUIPField, self).widget_attrs(widget)
        res.update({'class': 'vCUIPField'})
        return res

