from proyecto.clases.db import *

doc1 = Document(0, {})
doc2 = 'Documento'
col = Collection('documentos')

col.add_document(doc1)
print(col)
col.add_document(doc2)