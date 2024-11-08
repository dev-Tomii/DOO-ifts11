## Clases

### Str2Dic
Es una clase que al recibir el contenido de un archivo .csv lo convierte en un diccionario de Python

|  Atributo | Tipo |                        Descripcion                        |
|:---------:|:----:|:---------------------------------------------------------:|
|   schema  |  str |                El esquema del archivo .csv                |
| separador |  str | El separador de caracteres de cada item. Por defecto: ',' |

|  Metodo |   Parametros   | Retorno |                  Descripcion                  |
|:-------:|:--------------:|:-------:|:---------------------------------------------:|
| convert | row: list[str] |   dict  | Convierte una linea de un archivo .csv a dict |

---

### Document
Es una clase que almacena en forma de diccionario un contenido.

|  Atributo |     Tipo     |         Descripcion        |
|:---------:|:------------:|:--------------------------:|
|     id    |      int     |     la ID del documento    |
| contenido | dict \| None | El contenido del documento |

|    Metodo    |        Parametros       | Retorno |                              Descripcion                              |
|:------------:|:-----------------------:|:-------:|:---------------------------------------------------------------------:|
|   get_value  |        clave: str       |   str   |                 Ingresa una clave y devuelve su valor                 |
| modify_value | clave: str<br>valor:str |   str   |            Cambia el valor de la clave ingresada al deseado           |
|    to_json   |                         |   str   | Devuelve en un str formatteado estilo json el contenido del documento |

---

### Collection
Es una clase que almacena en forma de diccionario un contenido.

|  Atributo  | Tipo |        Descripcion        |
|:----------:|:----:|:-------------------------:|
|   nombre   |  str | El nombre de la coleccion |
| documentos | dict |  Contiene los documentos  |

|      Metodo     |      Parametros     |      Retorno     |                        Descripcion                       |
|:---------------:|:-------------------:|:----------------:|:--------------------------------------------------------:|
|   add_document  | documento: Document |       None       |             Añade un documento a la coleccion            |
| delete_document |  id_documento: int  |       None       | Elimina un documento de la coleccion con la id ingresada |
|   get_document  |  id_documento: int  | Document \| None |         Devuelve el documento con la id ingresada        |
|  list_documents |                     |  list[Document]  |        Devuelve todos los documentos en una lista        |  

---

### Database
Es una clase que almacena en forma de diccionario un contenido.

|   Atributo   | Tipo |         Descripcion        |
|:------------:|:----:|:--------------------------:|
|    nombre    |  str | Nombre de la base de datos |
| collecciones | dict |  Contiene las collecciones |

|       Metodo      |       Parametros       |       Retorno      |                                                              Descripcion                                                              |
|:-----------------:|:----------------------:|:------------------:|:-------------------------------------------------------------------------------------------------------------------------------------:|
| create_collection |  nombre_coleccion: str |        None        |                                        Crea una coleccion y la almacena con el nombre ingresado                                       |
| delete_collection |  nombre_coleccion: str |        None        |                                              Elimina la coleccion con el nombre ingresado                                             |
|   get_collection  |  nombre_coleccion: str | Collection \| None |                           Devuelve la coleccion con el nombre ingresado si existe, caso contrario sera None.                          |
|     import_csv    | name: str<br>path: str |        None        | Importa todas las lineas del archivo .csv ingresado en formato de Documento y las almacena en la coleccion que coincida con el nombre |

---

## Excepciones

### SchemaError
Es una excepcion que marca error en el esquema ingresado

### NonExistentCollectionError
Es una excepcion que marca que la coleccion es inexistente.

### NotFoundError
Es una excepcion que marca cuando un objeto no es encontrado.
