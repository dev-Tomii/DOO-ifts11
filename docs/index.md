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

|      Metodo     |        Parametros       | Retorno |                    Descripcion                   |
|:---------------:|:-----------------------:|:-------:|:------------------------------------------------:|
|  obtener_valor  |        clave: str       |   str   |       Ingresa una clave y devuelve su valor      |
| modificar_valor | clave: str<br>valor:str |   None  | Cambia el valor de la clave ingresada al deseado |

---

### Collection
Es una clase que almacena en forma de diccionario un contenido.

|  Atributo  | Tipo |        Descripcion        |
|:----------:|:----:|:-------------------------:|
|   nombre   |  str | El nombre de la coleccion |
| documentos | dict |  Contiene los documentos  |

|       Metodo       |      Parametros     |      Retorno     |                        Descripcion                       |
|:------------------:|:-------------------:|:----------------:|:--------------------------------------------------------:|
|  añadir_documento  | documento: Document |       None       |             Añade un documento a la coleccion            |
| eliminar_documento |  id_documento: int  |       None       | Elimina un documento de la coleccion con la id ingresada |
|  buscar_documento  |  id_documento: int  | Document \| None |         Devuelve el documento con la id ingresada        |

---

### DBDocument
Es una clase que almacena en forma de diccionario un contenido.

|   Atributo  | Tipo |        Descripcion       |
|:-----------:|:----:|:------------------------:|
| colecciones | dict | Contiene las colecciones |

|       Metodo       |       Parametros      |       Retorno      |                        Descripcion                       |
|:------------------:|:---------------------:|:------------------:|:--------------------------------------------------------:|
|   crear_coleccion  | nombre_coleccion: str |        None        | Crea una coleccion y la almacena con el nombre ingresado |
| eliminar_coleccion | nombre_coleccion: str |        None        |       Elimina la coleccion con el nombre ingresado       |
|  buscar_coleccion  | nombre_coleccion: str | Collection \| None |       Devuelve la coleccion con el nombre ingresado      |

---

## Excepciones

### SchemaError
Es una excepcion que marca error en el esquema ingresado