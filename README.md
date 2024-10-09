# DOO IFTS 11
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

En este repositorio encontraras mis trabajos de la materia **Desarrollo de Sistemas Orientado a Objetos**

# Contenidos
- [Clases](#clases)
  - [Str2Dic](#str2dic)
  - [Document](#str2dic)
  - [Collection](#str2dic)
  - [DBDocument](#str2dic)
- [Excepciones](#excepciones)
  - [SchemaError](#schemaerror)

*Para un contenido mas detallado, visita los [Docs](./docs/index.md)*

## Clases
[(Volver al indice)](#contenidos)

Aqui encontraras un listado de las clases creadas con su utilidad

### Str2Dic
Es una clase que al instanciarla con el contenido de un .csv es capaz de convertirlo a un diccionario de Python

[*(Ir al archivo)*](./proyecto/clases/str2dic.py)

### Document
Es una clase que almacena en forma de diccionario un contenido.

[*(Ir al archivo)*](./proyecto/clases/db.py)

### Collection
Es una clase que almacena en forma de diccionario un contenido.

[*(Ir al archivo)*](./proyecto/clases/db.py)

### DBDocument
Es una clase que almacena en forma de diccionario un contenido.

[*(Ir al archivo)*](./proyecto/clases/db.py)

## Excepciones
[(Volver al indice)](#contenidos)

Aqui encontraras las excepciones personalizadas que se crearon

### SchemaError
Es una excepcion que marca error en el esquema ingresado

[*(Ir al archivo)*](./proyecto/clases/custom_exceptions.py)

# Guia

Para ejecutar el proyecto entero, por favor ejecuta el archivo main con: `python -m proyecto.main`
Para ejecutar cualquier archivo de prueba, por favor usa: `python -m tests.{nombre_del_archivo}`