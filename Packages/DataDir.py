class Direccion:
    def __init__(self, calle: str, nomenclatura: str, barrio: str, ciudad: str, urbanizacion: str, noApto: str):
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad
        self.__urbanizacion = urbanizacion
        self.__noApto = noApto

    def __str__(self):
        return self.toString()

    def getCalle(self):
        return self.__calle
    
    def getNomenclatura(self):
        return self.__nomenclatura
    
    def getBarrio(self):
        return self.__barrio
    
    def getCiudad(self):
        return self.__ciudad
    
    def getUrbanizacion(self):
        return self.__urbanizacion
    
    def getNoApto(self):
        return self.__noApto
    
    def toString(self):
        return f"{self.__calle} {self.__nomenclatura}, {self.__barrio}, {self.__ciudad}"
    
class Fecha:
    def __init__(self, d: int, m: int, a: int):
        self.__dd = d
        self.__mm = m
        self.__aa = a
    
    def __str__(self):
        return self.toString()

    def getDD(self):
        return self.__dd
    
    def getMM(self):
        return self.__mm
    
    def getAA(self):
        return self.__aa
    
    def setDD(self, dia: int):
        self.__dd = dia
    
    def setMM(self, mes: int):
        self.__mm = mes

    def setAA(self, año: int):
        self.__aa = año

    def toString(self):
        return f"{self.__dd}/{self.__mm}/{self.__aa}"
