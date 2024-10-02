from .custom_exceptions import *

class Str2Dic():
    def __init__(self, schema, separator=','):
        if (len(schema)) == 0:
            raise SchemaError("El schema esta vacio")
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")
