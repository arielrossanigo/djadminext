Combos Extendidos es una extension para Django que permite realizar filtrado de
valores en los combos de un formulario mediante JSON. Permite a partir de la
seleccion de un valor en un campo combo (ForeignKeyExt) la actualizacion o filtrado
de los valores de uno o mas combos mediante vistas. Cada uno de los combos a
filtrar puede obtener los valores de una vista distinta.
Se incorpora una vista generica que sirve para la mayoria de los filtrados
necesarios.


Parametros de ForeignKeyExt:
url: URL de la vista a consultar, ej: /MasterDetailCombo (vista generica)
app_name: Nombre de la aplicacion que contiene el modelo del master
master_model_name: Nombre del modelo master
detail_model_name: Nombre del modelo detalle
detail_field_name: Nombre del campo que se va a actualizar
detail_display_field: Nombre del campo del detalle que se va a mostrar en el combo


Mas informacion en la pagina web del proyecto: http://code.google.com/p/djadminext/
