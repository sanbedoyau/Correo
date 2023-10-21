from Packages.DataDir import *
from Packages.Structures import *
from datetime import datetime
import os

class Usuario:
    def __init__(self, id: int, nombre: str):
        self.__id = id
        self.__nombre = nombre
        self.__fecha_nac = Fecha(0,0,0)
        self.__ciudad_nac = ""
        self.__dir = Direccion("",0,"","","","")
        self.__tel = 0
        self.__email = ""
        self.__password = ""
        self.__status = "Empleado"
        self.__bandeja = DoubleList()
        self.__msjLeidos = Queue()
        self.__borradores = Stack()
    
    def __repr__(self):
        return f"({self.__id}, {self.__nombre})"

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre
    
    def getFechaNac(self):
        return self.__fecha_nac
    
    def getCiudadNac(self):
        return self.__ciudad_nac
    
    def getDir(self):
        return self.__dir
    
    def getTel(self):
        return self.__tel
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def getStatus(self):
        return self.__status
    
    def getBandeja(self):
        if not self.__bandeja.isEmpty():
            return self.__bandeja
        else:
            return None
    
    def getLeidos(self):
        if not self.__msjLeidos.isEmpty():
            return self.__msjLeidos
        else:
            return None
    
    def getBorradores(self):
        if not self.__borradores.isEmpty():
            return self.__borradores
        else:
            return None

    def setId(self, id: int):
        self.__id = id

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setFechaNac(self, fecha: Fecha):
        self.__fecha_nac = fecha
    
    def setCiudadNac(self, ciudad: str):
        self.__ciudad_nac = ciudad

    def setDir(self, dir: Direccion):
        self.__dir = dir
    
    def setTel(self, tel: int):
        self.__tel = tel

    def setEmail(self, email: str):
        self.__email = email

    def setPassword(self, password: str):
        self.__password = password
    
    def setStatus(self, status: str):
        self.__status = status.lower()

    def recibirMensaje(self, remitente: str, title: str, msj: str):
        self.__bandeja.addLast(f"{datetime.now().strftime('Recibido el %d/%m/%Y, a las %H:%M')}|{remitente}|{title}|{msj}")
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}BA.txt") as BA:
            reader = BA.readlines()
        writer = reader
        if len(writer) == 0:
            writer.append(f"{datetime.now().strftime('Recibido el %d/%m/%Y, a las %H:%M')}|{remitente}|{title}|{msj}")
        else:
            writer.append(f"\n{datetime.now().strftime('Recibido el %d/%m/%Y, a las %H:%M')}|{remitente}|{title}|{msj}")
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}BA.txt", "w") as BA:
            BA.writelines(writer)
    
    def cargarBandeja(self):
        self.__bandeja = DoubleList()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}BA.txt") as BA:
            reader = BA.readlines()
        for mensaje in reader:
            self.__bandeja.addLast(mensaje.replace('\n', ''))

    def leerMensaje(self, msj: str):
        if self.__bandeja.getSize() > 1:
            f = self.__bandeja.first()
            while f != None:
                if f.getData() == msj:
                    self.__bandeja.remove(f)
                    break
                f = f.getNext()
        else:
            self.__bandeja = DoubleList()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}BA.txt") as BA:
            reader = BA.readlines()
        writer = []
        for mensaje in reader:
            if msj not in mensaje:
                writer.append(mensaje)
        if len(writer) == 0:
            self.__bandeja = DoubleList()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}BA.txt", "w") as BA:
            BA.writelines(writer)
        self.__msjLeidos.enqueue(msj)
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}ML.txt") as ML:
            reader = ML.readlines()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}ML.txt", "w") as ML:
            if len(reader) == 0:
                ML.write(msj)
            else:
                reader.append(f"\n{msj}")
                ML.writelines(reader)
    
    def cargarLeidos(self):
        self.__msjLeidos = Queue()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}ML.txt") as ML:
            reader = ML.readlines()
        for mensaje in reader:
            self.__msjLeidos.enqueue(mensaje.replace('\n', ''))

    def guardarBorrador(self, id: str, title: str, msj: str):
        self.__borradores.push(f"{datetime.now().strftime('Guardado el %d/%m/%Y a las %H:%M')}|{id}|{title}|{msj}")
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt") as B:
            reader = B.readlines()
        writer = reader
        if len(writer) != 0:
            writer.insert(0,f"{datetime.now().strftime('Guardado el %d/%m/%Y a las %H:%M')}|{id}|{title}|{msj}\n")
        else:
            writer.insert(0,f"{datetime.now().strftime('Guardado el %d/%m/%Y a las %H:%M')}|{id}|{title}|{msj}")
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt", "w") as B:
            B.writelines(writer)

    def cargarBorrador(self):
        self.__borradores = Stack()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt") as B:
            reader = B.readlines()
        for mensaje in reader[::-1]:
            self.__borradores.push(mensaje.replace('\n', ''))

    def usarBorrador(self):
        self.__borradores.pop()
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt") as B:
            last = B.readline()
            reader = B.readlines()
        writer = []
        for mensaje in reader:
            if mensaje != last:
                writer.append(mensaje)
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt", "w") as B:
            B.writelines(writer)
        if len(writer) == 0:
            self.__borradores = Stack()





    def getMensajes(self):
        Bandeja = []
        f = self.__bandeja.first()
        while f != None:
            Bandeja.append([f.getData().split("|")[0], f.getData().split("|")[1] ,f.getData().split("|")[2].upper(), f.getData()])
            f = f.getNext()
        return Bandeja
    
    def getLastMLeidos(self):
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}ML.txt") as ML:
            reader = ML.readlines()
        return reader
    
    def ultimoBorrador(self):
        with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{self.__nombre}/{self.__id}B.txt") as B:
            last = B.readline()
        if last != "":
            return last.replace("\n","")
        return None

        

    


class Registro:
    def __init__(self):
        self.__registro = DoubleList()
        self.__noRegistros = 0
    
    def agregar(self, usuario: Usuario):
        if self.__registro.isEmpty():
            self.__registro.addFirst(usuario)
            self.__noRegistros += 1
            return True
        else:
            f = self.__registro.first()
            while f != None:
                if f.getData().getId() == usuario.getId():
                    return False
                elif f.getData().getId() > usuario.getId():
                    self.__registro.addBefore(f,usuario)
                    self.__noRegistros += 1
                    return True
                f = f.getNext()
            self.__registro.addLast(usuario)
            self.__noRegistros += 1
            return True

    def eliminar(self, id: int):
        if not self.__registro.isEmpty():
            f = self.__registro.first()
            while f.getData().getId() != id and f.getNext() != None:
                f = f.getNext()
            if f.getData().getId() == id:
                temp = f.getData()
                self.__registro.remove(f)
                self.__noRegistros -= 1
                return temp
        return None   

    def buscarUsuario(self,id: int):
        if not self.__registro.isEmpty():
            f = self.__registro.first()
            while f != None:
                if f.getData().getId() == id:
                    return f.getData()
                f = f.getNext()
            return None

    def toFile(self):
        with open("Prácticas\Practica 2\Sources\Empleados.txt", "w") as emp:
            f = self.__registro.first()
            while f != None:
                User = f.getData()
                x = f"{User.getNombre()} {User.getId()} {User.getFechaNac().getDD()} {User.getFechaNac().getMM()} {User.getFechaNac().getAA()} {User.getCiudadNac()} {User.getTel()} {User.getEmail()} {User.getDir().getCalle()} {User.getDir().getNomenclatura()} {User.getDir().getBarrio()} {User.getDir().getCiudad()} {User.getDir().getUrbanizacion()} {User.getDir().getNoApto()}"
                if f.getNext() != None:
                    x += "\n"
                emp.write(x)
                f = f.getNext()
        with open("Prácticas\Practica 2\Sources\Password.txt", "w") as pwd:
            f = self.__registro.first()
            while f != None:
                User: Usuario = f.getData()
                x = f"{User.getId()} {User.getPassword()} {User.getStatus()}"
                if f.getNext() != None:
                    x += "\n"
                pwd.write(x)
                f = f.getNext()

    def importar(self):
        with open("Prácticas\Practica 2\Sources\Empleados.txt") as emp:
            reader = emp.readlines()
        for linea in reader[:len(reader)-1]:
            line = linea[:len(linea)-1].split()
            nombre = line[0]
            id = int(line[1])
            NuevoUsuario = Usuario(id,nombre)
            dd = int(line[2])
            mm = int(line[3])
            aa = int(line[4])
            fechaNacimiento = Fecha(dd,mm,aa)
            NuevoUsuario.setFechaNac(fechaNacimiento)
            ciudadNac = line[5]
            NuevoUsuario.setCiudadNac(ciudadNac)
            telefono = int(line[6])
            NuevoUsuario.setTel(telefono)
            email = line[7]
            NuevoUsuario.setEmail(email)
            calle = line[8]
            nomenclatura = line[9]
            barrio = line[10]
            ciudad = line[11]
            urbanizacion = line[12]
            Apto = line[13]
            direc = Direccion(calle,nomenclatura,barrio,ciudad,urbanizacion,Apto)
            NuevoUsuario.setDir(direc)
            self.agregar(NuevoUsuario)
        line = reader[-1].split()
        nombre = line[0]
        id = int(line[1])
        NuevoUsuario = Usuario(id,nombre)
        dd = int(line[2])
        mm = int(line[3])
        aa = int(line[4])
        fechaNacimiento = Fecha(dd,mm,aa)
        NuevoUsuario.setFechaNac(fechaNacimiento)
        ciudadNac = line[5]
        NuevoUsuario.setCiudadNac(ciudadNac)
        telefono = int(line[6])
        NuevoUsuario.setTel(telefono)
        email = line[7]
        NuevoUsuario.setEmail(email)
        calle = line[8]
        nomenclatura = line[9]
        barrio = line[10]
        ciudad = line[11]
        urbanizacion = line[12]
        Apto = line[13]
        direc = Direccion(calle,nomenclatura,barrio,ciudad,urbanizacion,Apto)
        NuevoUsuario.setDir(direc)
        self.agregar(NuevoUsuario)
        with open("Prácticas\Practica 2\Sources\Password.txt") as pwd:
            reader = pwd.readlines()
            for linea in reader[:len(reader)-1]:
                line = linea[:len(linea)-1].split()
                Id = int(line[0])
                password = line[1]
                status = line[2]
                self.buscarUsuario(Id).setPassword(password)
                self.buscarUsuario(Id).setStatus(status)
            line = reader[-1].split()
            Id = int(line[0])
            password = line[1]
            status = line[2]
            self.buscarUsuario(Id).setPassword(password)
            self.buscarUsuario(Id).setStatus(status)
        f = self.__registro.first()
        while f != None:
            User : Usuario = f.getData()
            try:
                os.mkdir(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{User.getNombre()}")
            except:
                pass
            try:
                with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{User.getNombre()}/{User.getId()}BA.txt", mode="x"):
                    pass
            except:
                pass
            try:
                with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{User.getNombre()}/{User.getId()}ML.txt", mode="x"):
                    pass
            except:
                pass
            try:
                with open(f"C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{User.getNombre()}/{User.getId()}B.txt", mode="x"):
                    pass
            except:
                pass
            f.getData().cargarBandeja()
            f.getData().cargarBorrador()
            f.getData().cargarLeidos()
            f = f.getNext()