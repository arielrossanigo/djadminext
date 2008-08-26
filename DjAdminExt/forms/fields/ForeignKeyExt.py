from django import forms
from DjAdminExt.forms.widgets import SelectAJAX

class ForeignKeyExt(forms.ModelChoiceField):
    def __init__(self, queryset, empty_label=u"---------", cache_choices=False,
                 required=True, widget=SelectAJAX, label=None, initial=None,
                 bindings=None, help_text=None, *args, **kwargs):
        super(ForeignKeyExt, self).__init__(queryset, empty_label, cache_choices,  required,
        widget(bindings), label, initial, help_text, *args, **kwargs)
