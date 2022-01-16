class ClasseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada=None
    def setPropiedadPrivada (self,valor):
        self.__propiedad_privada=valor
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    def propiedadPrivada (self, valor=None):
        if valor==None:
            return self.__propiedad_privada
        else:
            self.__propiedad_privada=valor
    
    def __srt__(self):
        return 'ClaseConGetterySetter con Propiedad privada-->{} '.format(self.__propiedad_privada)
        
if __name__=='__main__':
    c= ClasseConGetterySetter()