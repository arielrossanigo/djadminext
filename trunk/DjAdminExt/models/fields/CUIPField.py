from django.db import models
from DjAdminExt import forms

class CUIPField(models.IntegerField):
    __metaclass__= models.SubfieldBase

    def db_type(self):
        from django.conf import settings
        if settings.DATABASE_ENGINE == 'postgresql_psycopg2':
            return 'bigint'
        else:
            raise Exception ('No implementado para el engine %s'%settings.DATABASE_ENGINE)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.CUIPField}
        defaults.update(kwargs)
        return super(CUIPField, self).formfield(**defaults)

