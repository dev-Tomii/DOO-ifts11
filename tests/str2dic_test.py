from proyecto.str2dic import *

schema = 'Nombre,Apellido,Edad,Mail'
row = 'Tomas,Medina,21,devtomii03@gmail.com'

o = Str2Dic(schema)
d = o.convert(row)

print(d)