from .clases.db import Collection
from .clases.db import Document
from .clases.str2dic import Str2Dic

def import_collection(path: str) -> Collection:
    with open(path) as f:
        schema = f.readline().replace("\n", "")
        rows = f.readlines()
        parser = Str2Dic(schema)
        col = Collection('Personas')
        id = 0
        for row in rows:
            item = parser.convert(row.replace("\n", ""))
            col.añadir_documento(Document(id, item))
            id += 1
    return col

personas = import_collection('proyecto/datos_personales.csv')

# Pruebas
doc = personas.buscar_documento(1)
print(doc.obtener_valor('Nombre'))