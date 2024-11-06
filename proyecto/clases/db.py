from .str2dic import Str2Dic
from .custom_exceptions import *
import json

class Document:
    def __init__(self, id: int, contenido: dict = None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}
        
    def get_value(self, clave: str) -> str:
        return self.contenido.get(clave, None)
    
    def modify_value(self, clave: str, valor: str) -> None:
        self.contenido[clave] = valor
        
    def to_json(self) -> str:
        dic = {'title': '', 'content': {}}
        dic['title'] = f'Documento ID {self.id}'
        dic['content'] = self.contenido
        return json.dumps(dic)
        
    def __str__(self) -> str:
        return f'Documento | ID {self.id}\n{self.contenido}'
    
class Collection:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.documentos = {}
    
    def add_document(self, documento: Document) -> None:
        if (type(documento) != Document):
            raise TypeError('No se ha ingresado un documento valido')
        self.documentos[documento.id] = documento
        
    def delete_document(self, id_documento: int) -> None:
        if id_documento in self.documentos:
            del self.documentos[id_documento]
            
    def get_document(self, id_documento: int) -> Document | None:
        return self.documentos.get(id_documento, None)
    
    def list_documents(self) -> None:
        return self.documentos
    
    def __str__(self):
        return f'Coleccion {self.nombre} | {len(self.documentos)} Documento/s registrados'
    
class Database:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.colecciones = {}
        
    def create_collection(self, nombre_coleccion: str) -> None:
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
            
    def delete_collection(self, nombre_coleccion: str) -> None:
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def get_collection(self, nombre_coleccion: str) -> Collection | None:
        return self.colecciones.get(nombre_coleccion, None)
    
    def import_csv(self, name: str, path: str) -> None:
        if (type(path) != str):
            raise AttributeError("Se ha ingresado una ruta inexistente.")
        with open(path) as f:
            schema = f.readline().replace("\n", "")
            rows = f.readlines()
            parser = Str2Dic(schema)
            col = self.get_collection(name)
            if (col == None):
                raise NonExistentDocumentError("El documento indicado no existe")
            id = 0
            for row in rows:
                item = parser.convert(row.replace("\n", ""))
                col.add_document(Document(id, item))
                id += 1
    
    def __str__(self):
        return f'BDDocument {self.nombre} | {len(self.documentos)} Coleccion/es registrados'
    