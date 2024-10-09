from proyecto.clases.db import *

doc1 = Document(0, {})
doc2 = 'Documento'
col = Collection('documentos')

col.añadir_documento(doc1)
print(col)
col.añadir_documento(doc2)