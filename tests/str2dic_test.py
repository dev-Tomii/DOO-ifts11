from proyecto.str2dic import *
schema = 'Nombre,Apellido,Edad,Mail'
row = 'Tomas,Medina,21,devtomii03@gmail.com'

try:
    o = Str2Dic(schema)
except SchemaError as e:
    print("Fallo algo en el schema", e)
except AttributeError as e:
    print("Pasaron mal el parametro", e)
d = o.convert(row)

print(d)