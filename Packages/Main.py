from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from Packages.DataDir import Direccion
from Packages.DataDir import Fecha
from Packages.Users import Usuario
from Packages.Users import Registro
import os

class Interfaz:
    def __init__(self, user: Usuario, tipo: str, registros: Registro):
        self.User = user
        self.tipo = tipo
        self.registro = registros
        self.root = Tk()
        self.root.title(f"{self.User.getNombre().split('-')[0]} {self.User.getNombre().split('-')[1]} - {self.tipo.capitalize()}")
        self.root.geometry("1000x500")
        self.root.resizable(width=0, height=0)

        # Frame para las opciones
        self.frameOpciones = Frame(self.root, bd=0, width=150, height =500, relief=SOLID, bg="#fcfcfc")
        self.frameOpciones.pack(side="left", expand=NO, fill=BOTH)

        # Frame para lo otro
        MainFrame = Frame(self.root, bd=0, width=850, height =500, relief=SOLID, bg="#fcfcfc")
        MainFrame.pack(side="right",expand=YES, fill=BOTH)

        # Frames para distinguir en lo otro
        self.mainFrame_top = Frame(MainFrame, height=30, bd=0, relief=SOLID, bg="#fcfcfc")
        self.mainFrame_top.pack(side="top", fill=X)

        self.mainFrame_other = Frame(MainFrame, height=470, bd=0, relief=SOLID, bg="#fcfcfc")
        self.mainFrame_other.pack(side="bottom", fill=X)

        # Botones para funcionalidades
        Label(self.frameOpciones, text="Correo", font=("Times",11, BOLD), bg="#fcfcfc", anchor="w").pack(fill=X, padx=10)

        self.Bandejabtn     = Button(self.frameOpciones, text="Bandeja de entrada", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.entrada)
        self.Bandejabtn.pack(fill=X)
        self.Bandejabtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Bandejabtn))
        self.Bandejabtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Bandejabtn))

        self.Leidosbtn      = Button(self.frameOpciones, text="Mensajes leídos    ", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.leidos)
        self.Leidosbtn.pack(fill=X)
        self.Leidosbtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Leidosbtn))
        self.Leidosbtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Leidosbtn))

        self.Redactarbtn    = Button(self.frameOpciones, text="Redactar mensaje  ", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.redactarMensaje)
        self.Redactarbtn.pack(fill=X)
        self.Redactarbtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Redactarbtn))
        self.Redactarbtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Redactarbtn))

        self.Borradoresbtn  = Button(self.frameOpciones, text="Borradores", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.borradores)
        self.Borradoresbtn.pack(fill=X, padx=(20,0))
        self.Borradoresbtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Borradoresbtn))
        self.Borradoresbtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Borradoresbtn))

        if self.tipo == "administrador":
            Label(self.frameOpciones, text="Modificar usuarios", font=("Times",11, BOLD), bg="#fcfcfc", anchor="w").pack(fill=X, padx=10, pady=(45,0))

            self.Modificarbtn = Button(self.frameOpciones, text="Registrar usuario      ", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.registrarUsuario)
            self.Modificarbtn.pack(fill=X)
            self.Modificarbtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Modificarbtn))
            self.Modificarbtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Modificarbtn))

            self.ModContraseñabtn = Button(self.frameOpciones, text="Modificar contraseña", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.modificarContraseña)
            self.ModContraseñabtn.pack(fill=X)
            self.ModContraseñabtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.ModContraseñabtn))
            self.ModContraseñabtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.ModContraseñabtn))

            self.Eliminarbtn = Button(self.frameOpciones, text="Eliminar usuario       ", font=("Helvetica", 10), bg="#fcfcfc", bd=0, fg="#000", width=20, height=3, command=self.eliminarUsuario)
            self.Eliminarbtn.pack(fill=X)
            self.Eliminarbtn.bind("<Enter>", lambda event: self.mainbuttonHover(self.Eliminarbtn))
            self.Eliminarbtn.bind("<Leave>", lambda event: self.mainbuttonHover_leave(self.Eliminarbtn))

        self.root.mainloop()

    def registrarUsuario(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Modificarbtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Registrar nuevo usuario", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        Label(self.mainFrame_other, text = "Ingrese los datos del nuevo usuario (sin espacios ni puntos)", font=("Times",12), bg="#fcfcfc", fg="#616583").grid(column=0, row=0, columnspan=6, pady=10)

        # Ajustes
        Label(self.mainFrame_other, text="                         ", bg="#fcfcfc", bd=0).grid(column=1, row= 1)
        Label(self.mainFrame_other, text="                         ", bg="#fcfcfc", bd=0).grid(column=3, row=1)
        Label(self.mainFrame_other, text="                   ", bg="#fcfcfc", bd=0).grid(column=5, row=1)

        # Datos
        Nombre = StringVar()
        Label(self.mainFrame_other, text="Nombre-Apellido".ljust(35," "), font=("Times", 11), bg="#fcfcfc", bd= 0).grid(column=0, row=1, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Nombre, width=30).grid(column=0, row=2, pady=(0,5))
        
        Cedula = StringVar()
        Label(self.mainFrame_other, text="Cédula o identificación ".ljust(36," "), font=("Times", 11), bg="#fcfcfc", bd=0).grid(column=2, row=1, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Cedula, width=30).grid(column=2, row=2, pady=(0,5))

        FechaNac = StringVar()
        Label(self.mainFrame_other, text="Fecha de nacimiento (dd-mm-aa)", font=("Times", 11), bg="#fcfcfc").grid(column=4, row=1, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=FechaNac, width=30).grid(column=4, row= 2, pady=(0,5))

        CiudadNac = StringVar()
        Label(self.mainFrame_other, text="Ciudad de nacimiento".ljust(34," "), font=("Times", 11), bg="#fcfcfc").grid(column=0, row=3,pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=CiudadNac, width=30).grid(column=0, row=4, pady=(0,5))

        Telefono = StringVar()
        Label(self.mainFrame_other, text="Teléfono".ljust(42," "), font=("Times", 11), bg="#fcfcfc", bd=0).grid(column=2, row=3, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Telefono, width=30).grid(column=2, row=4, pady=(0,5))

        Correo = StringVar()
        Label(self.mainFrame_other, text="Correo electrónico".ljust(38," "), font=("Times", 11), bg="#fcfcfc").grid(column=4, row=3, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Correo, width=30).grid(column=4, row= 4, pady=(0,5))

        Contraseña = StringVar()
        Label(self.mainFrame_other, text="Nueva contraseña".ljust(35," "), font=("Times", 11), bg="#fcfcfc").grid(column=0, row=5,pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Contraseña, width=30, show="·").grid(column=0, row=6, pady=(0,5))

        Estatus = StringVar()
        Label(self.mainFrame_other, text="Estatus".ljust(42," "), font=("Times", 11), bg="#fcfcfc", bd=0).grid(column=2, row=5, pady=5)
        ttk.Combobox(self.mainFrame_other, values=("Empleado","Administrador"), width=27, state="readonly", textvariable=Estatus).grid(column=2, row=6)

        Label(self.mainFrame_other, text="Dirección", font=("Times", 16), bg="#fcfcfc", bd=0).grid(column=0,row=7, padx=(0,110), pady=(20,10))

        Calle = StringVar()
        Label(self.mainFrame_other, text="Calle (e.g. kr23)".ljust(39," "), font=("Times", 11), bg="#fcfcfc").grid(column=0, row=8,pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Calle, width=30).grid(column=0, row=9, pady=(0,5))

        Nomenclatura = StringVar()
        Label(self.mainFrame_other, text="Nomenclatura".ljust(37," "), font=("Times", 11), bg="#fcfcfc", bd=0).grid(column=2, row=8, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Nomenclatura, width=30).grid(column=2, row=9, pady=(0,5))

        Barrio = StringVar()
        Label(self.mainFrame_other, text="Barrio".ljust(44," "), font=("Times", 11), bg="#fcfcfc").grid(column=4, row=8, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Barrio, width=30).grid(column=4, row= 9, pady=(0,5))

        Ciudad = StringVar()
        Label(self.mainFrame_other, text="Ciudad".ljust(42," "), font=("Times", 11), bg="#fcfcfc").grid(column=0, row=10,pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Ciudad, width=30).grid(column=0, row=11, pady=(0,5))

        Urbanizacion = StringVar()
        Label(self.mainFrame_other, text="Urbanización".ljust(39," "), font=("Times", 11), bg="#fcfcfc", bd=0).grid(column=2, row=10, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=Urbanizacion, width=30).grid(column=2, row=11, pady=(0,5))

        NoApto = StringVar()
        Label(self.mainFrame_other, text="Número de apartamento ".ljust(32," "), font=("Times", 11), bg="#fcfcfc").grid(column=4, row=10, pady=5)
        ttk.Entry(self.mainFrame_other, textvariable=NoApto, width=30).grid(column=4, row= 11, pady=(0,5))

        # Boton para registrar
        Button(self.mainFrame_other,text="Registrar", font=("Helvetica", 10), bd=0, fg="#000", width=10, command=lambda: registrar()).grid(column=4,row=12,pady=17)

        def registrar():
            add = False
            try:
                Nom = Nombre.get()
                if Nom == "":
                    raise Exception("Sin nombre")
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese un nombre válido")
            try:
                Id = int(Cedula.get())
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese una identificación válida")
                Cedula.set("")
            try:
                Nuevo = Usuario(Id,Nom)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese identificación y nombre válidos")
            try:
                Fechas = FechaNac.get()
                dd = int(Fechas.split("-")[0])
                mm = int(Fechas.split("-")[1])
                aa = int(Fechas.split("-")[2])
                Nac = Fecha(dd,mm,aa)
                Nuevo.setFechaNac(Nac)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese una fecha válida")
            try:
                CiudNac = CiudadNac.get()
                Nuevo.setCiudadNac(CiudNac)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese una ciudad de nacimiento válida")
            try:
                Tel = int(Telefono.get())
                Nuevo.setTel(Tel)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese un teléfono válido")
            try:
                email = Correo.get()
                Nuevo.setEmail(email)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese un correo válido")
            try:
                Contr = Contraseña.get()
                Nuevo.setPassword(Contr)
            except:
                messagebox.showerror(title="Error", message="Por favor introduzca una contraseña válida")
            try:
                Stat = Estatus.get()
                if Stat == "":
                    raise Exception("Sin estatus")
                Nuevo.setStatus(Stat)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor seleccione un estatus válido")
            try:
                Cll = Calle.get()
                Nomenc = Nomenclatura.get()
                Barr = Barrio.get()
                cit = Ciudad.get()
                Urban = Urbanizacion.get()
                NoApt = NoApto.get()
                if Cll == "" or Nomenc == "" or Barr == "" or cit =="":
                    raise Exception("Direccion invalida")
                if Urban == "":
                    Urban = "null"
                if NoApt == "":
                    NoApt = "null"
                dir = Direccion(Cll, Nomenc, Barr, cit, Urban, NoApt)
                Nuevo.setDir(dir)
                add = True
            except:
                add = False
                messagebox.showerror(title="Error", message="Por favor ingrese una dirección válida y/o llene todos los campos de la dirección")
            try:
                if add:
                    self.registro.agregar(Nuevo)
                    self.registro.toFile()
                    self.registro.importar()

                    # Limpiar los campos
                    Nombre.set("")
                    Cedula.set("")
                    FechaNac.set("")
                    CiudadNac.set("")
                    Telefono.set("")
                    Correo.set("")
                    Contraseña.set("")
                    Estatus.set("")
                    Calle.set("")
                    Nomenclatura.set("")
                    Barrio.set("")
                    Ciudad.set("")
                    Urbanizacion.set("")
                    NoApto.set("")
            except:
                messagebox.showerror(title="Error", message="Vuelva a intentarlo")

    def modificarContraseña(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.ModContraseñabtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Modificar Contraseña", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        Label(self.mainFrame_other, text = "Ingrese los datos del usuario al que desea cambiar la contraseña (sin espacios ni puntos)", font=("Times",14), bg="#fcfcfc", fg="#616583").pack(fill=X)

        # Datos
        Cedula = StringVar()
        Label(self.mainFrame_other, text="Cédula o identificación", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w").pack(fill=X, pady=(10,2))
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Cedula, width=150).pack(pady=(2,5),padx=(2,600))

        Contraseña = StringVar()
        Label(self.mainFrame_other, text="Contraseña actual", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w").pack(fill=X,pady=(10,2))
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Contraseña, width=150, show="·").pack(pady=(2,5),padx=(2,600))

        Button(self.mainFrame_other, text="Verificar", font=("Helvetica", 10), bd=0, fg="#000", width=10, command= lambda: verificar()).pack(padx=(100,0))

        temp = Label(self.mainFrame_other, textvariable="", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w")
        temp.pack(fill=X,pady=500)

        def verificar():
            Id = Cedula.get()
            add = False
            try:
                Id = int(Id)
                User: Usuario = self.registro.buscarUsuario(Id)
                if User == None:
                    messagebox.showerror(title="Error", message="Identificación no registrada")
                    Cedula.set("")
                    add = False
                else:
                    add = True
            except:
                messagebox.showerror(title="Error", message="Por favor ingrese una identificación válida")
                Cedula.set("")
            if add:
                cambiar = False
                try:
                    Pwd = Contraseña.get()
                    if Pwd == "":
                        raise Exception("No pwd")
                    elif User.getPassword() != Pwd:
                        messagebox.showerror(title="Error", message="Contraseña incorrecta")
                        Contraseña.set("")
                        cambiar = False
                    else:
                        cambiar = True
                except:
                    messagebox.showerror(title="Error", message="Por favor ingrese una contraseña válida")
                    Contraseña.set("")
                if cambiar:
                    temp.destroy()

                    NuevaContraseña = StringVar()
                    NuevaContraseñalbl = Label(self.mainFrame_other, text="Nueva contraseña", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w")
                    NuevaContraseñalbl.pack(fill=X, pady=(10,2))
                    NuevaContraseñatxt = ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=NuevaContraseña, width=150, show="·")
                    NuevaContraseñatxt.pack(pady=(2,5),padx=(2,600))

                    ConfNuevaCont = StringVar()
                    ConfNuevaContlbl = Label(self.mainFrame_other, text="Nueva contraseña (confirmar)", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w")
                    ConfNuevaContlbl.pack(fill=X,pady=(10,2))
                    ConfNuevaConttxt = ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=ConfNuevaCont, width=150, show="·")
                    ConfNuevaConttxt.pack(pady=(2,5),padx=(2,600))

                    Cambiarbtn = Button(self.mainFrame_other, text="Cambiar", font=("Helvetica", 10), bd=0, fg="#000", width=10, command= lambda: cambiar())
                    Cambiarbtn.pack(padx=(100,0), pady=(0,105))

                    def cambiar():
                        try:
                            password = NuevaContraseña.get()
                            if password == "":
                                messagebox.showerror(title="Error", message="Introduzca una contraseña válida y complete ambos campos")
                                NuevaContraseña.set("")
                                ConfNuevaCont.set("")
                            elif ConfNuevaCont.get() != password:
                                raise Exception("No coinciden")
                            else:
                                User.setPassword(password)
                                self.registro.toFile()
                                Cedula.set("")
                                Contraseña.set("")

                                NuevaContraseñalbl.destroy()
                                NuevaContraseñatxt.destroy()
                                ConfNuevaContlbl.destroy()
                                ConfNuevaConttxt.destroy()
                                Cambiarbtn.destroy()

                                temp = Label(self.mainFrame_other, textvariable="", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w")
                                temp.pack(fill=X,pady=500)

                                messagebox.showinfo(title="Éxito", message= f"Contraseña del usuario {User.getNombre().split('-')[0]} {User.getNombre().split('-')[1]} actualizada correctamente")
                        except:
                            messagebox.showerror(title="Error", message="Las contraseñas no coinciden, vuelva a intentarlo")
                            NuevaContraseña.set("")
                            ConfNuevaCont.set("")

    def eliminarUsuario(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Eliminarbtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Eliminar usuario", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        Label(self.mainFrame_other, text = "Ingrese los datos del usuario que desea eliminar (sin espacios ni puntos)", font=("Times",14), bg="#fcfcfc", fg="#616583").pack(fill=X)

        # Datos
        Cedula = StringVar()
        Label(self.mainFrame_other, text="Cédula o identificación", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w").pack(fill=X, pady=(10,2))
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Cedula, width=150).pack(pady=(2,5),padx=(2,600))

        Contraseña = StringVar()
        Label(self.mainFrame_other, text="Contraseña actual", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w").pack(fill=X,pady=(10,2))
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Contraseña, width=150, show="·").pack(pady=(2,5),padx=(2,600))

        Button(self.mainFrame_other, text="Eliminar", font=("Helvetica", 10), bd=0, fg="#000", width=10, command= lambda: eliminar()).pack(padx=(100,0))

        temp = Label(self.mainFrame_other, textvariable="", font=("Times",12), fg="#616583", bg="#fcfcfc", anchor="w")
        temp.pack(fill=X,pady=500)

        def eliminar():
            Id = Cedula.get()
            elim = False
            try:
                Id = int(Id)
                User: Usuario = self.registro.buscarUsuario(Id)
                if User == None:
                    messagebox.showerror(title="Error", message="Identificación no registrada")
                    Cedula.set("")
                    elim = False
                else:
                    elim = True
            except:
                messagebox.showerror(title="Error", message="Por favor ingrese una identificación válida")
                Cedula.set("")
            if elim:
                verif = False
                try:
                    Pwd = Contraseña.get()
                    if Pwd == "":
                        raise Exception("No pwd")
                    elif User.getPassword() != Pwd:
                        messagebox.showerror(title="Error", message="Contraseña incorrecta")
                        Contraseña.set("")
                        verif = False
                    else:
                        verif = True
                except:
                    messagebox.showerror(title="Error", message="Por favor ingrese una contraseña válida")
                    Contraseña.set("")
                if verif:
                    Y_N = messagebox.askyesno("", f"Estás seguro que quieres eliminar al usuario {User.getNombre().split('-')[0]} {User.getNombre().split('-')[1]}?")
                    if Y_N == True:
                        self.registro.eliminar(Id)
                        self.registro.toFile()
                        Cedula.set("")
                        Contraseña.set("")
                        messagebox.showinfo("Eliminado", f"El usuario {User.getNombre().split('-')[0]} {User.getNombre().split('-')[1]} fue eliminado correctamente")
                        os.system(f"rm -r 'C:/Users/santi/Documents/Estructura de datos/Prácticas/Practica 2/Sources/{User.getNombre()}'")

    def entrada(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Bandejabtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Bandeja de entrada", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        
        if self.User.getBandeja() == None:
            Label(self.mainFrame_other, text="No has recibido ningún mensaje", font=("Helvetica",13), bg="#fcfcfc", fg="#000").pack(fill=X, pady= 214)
        else:
            self.bandejaEntrada()

    def bandejaEntrada(self):
        Mensajes = self.User.getMensajes()
        
        botones = {}
        for msj in range(len(Mensajes)):
            variable = f"boton_{msj}"
            botones[variable] = Button(self.mainFrame_other, text = f"{Mensajes[msj][0]} de {Mensajes[msj][1]}          {Mensajes[msj][2]}", anchor="w")
        cont = 0
        for titulo, value in botones.items():
            if cont == len(Mensajes)-1:
                pad = 427-((len(Mensajes)-1)*26)
                botones[titulo].pack(fill=X, pady=(0,pad))
            else:
                botones[titulo].pack(fill=X)
            botones[titulo].config(command= lambda i=cont: leer(i))
            cont += 1

        
        def leer(i):
            messagebox.showinfo(Mensajes[i][2],f"{Mensajes[i][0]}\nDe: {Mensajes[i][1].split('-')[0]} {Mensajes[i][1].split('-')[1]}\n\n{Mensajes[i][2]}\n-----\n{Mensajes[i][3].split('|')[3]}")
            self.registro.buscarUsuario(self.User.getId()).leerMensaje(Mensajes[i][3])
            self.registro.importar()
            self.entrada()


    def leidos(self, t = False):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Leidosbtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Mensajes leídos", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        
        if self.User.getLeidos() == None:
            Label(self.mainFrame_other, text="No tienes mensajes leídos", font=("Helvetica",13), bg="#fcfcfc", fg="#000").pack(fill=X, pady= 214)
        else:
            self.mensajesLeidos(0)
            
    def mensajesLeidos(self, index):
        for wi in self.mainFrame_other.winfo_children():
            wi.destroy()
        Mensaje = self.User.getLastMLeidos()[index].split("|")
        fech = Mensaje[0]
        remitente = Mensaje[1]
        titulo = Mensaje[2]
        cuerpo = Mensaje[3]
        Label(self.mainFrame_other, text=fech, font=("Times", 15), bg="#fcfcfc", fg="#616583", anchor="w").pack(fill=X,pady=5)
        Label(self.mainFrame_other, text=f"De: {remitente.split('-')[0]} {remitente.split('-')[1]}", font=("Times", 15), bg="#fcfcfc", fg="#616583", anchor="w").pack(fill=X,pady=(5,10))
        Label(self.mainFrame_other, text=titulo.upper(), font=("Times", 14), bg="#fcfcfc", fg="#616583", anchor="w").pack(fill=X,pady=(5,0))
        Label(self.mainFrame_other, text=cuerpo, font=("Times", 12), bg="#fcfcfc", fg="#616583", anchor="w").pack(fill=X,pady=(0,230))
        Button(self.mainFrame_other, text = "Siguiente", command= lambda: siguiente()).pack(anchor="se",padx=50,pady=25)
        index += 1

        def siguiente():
            if index < len(self.User.getLastMLeidos()):
                self.mensajesLeidos(index)
            else:
                for wi in self.mainFrame_other.winfo_children():
                    wi.destroy()
                Label(self.mainFrame_other, text="No tienes más mensajes leídos", font=("Helvetica",13), bg="#fcfcfc", fg="#000").pack(fill=X, pady= 214)     

    def borradores(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Borradoresbtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Borradores", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)

        if self.User.getBorradores() == None:
            Label(self.mainFrame_other, text="No tienes mensajes en borradores", font=("Helvetica",13), bg="#fcfcfc", fg="#000").pack(fill=X, pady= 214)
        else:
            self.verBorradores()

    def verBorradores(self):
        Data = self.User.ultimoBorrador().split("|")
        Label(self.mainFrame_other, text = Data[0], font=("Times",13), bg="#fcfcfc", fg="#616583").grid(column=0,row=0, columnspan=5, pady=6)
        
        # Datos
        Label(self.mainFrame_other, text = "Id:           ", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=1, pady=5)
        Id = ttk.Entry(self.mainFrame_other, font=("Times",12))
        Id.insert(0, Data[1])
        Id.grid(column=1,row=1, pady=5, padx=(0,170))


        Label(self.mainFrame_other, text = "Titulo:       ", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=2, pady=5)

        Titulo = ttk.Entry(self.mainFrame_other, font=("Times",12), width=77)
        Titulo.insert(0,str(Data[2]))
        Titulo.grid(column=1,row=2, pady=5, columnspan=4)

        Label(self.mainFrame_other, text = "Mensaje                                                                                                                                                                          ", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=3, pady=(5,1), columnspan=5)
        Mens = Text(self.mainFrame_other, font=("Times",12), width=99, height=14)
        Mens.insert("1.0", Data[3])
        Mens.grid(column=0,row=4, pady=(1,5), padx=5, columnspan=5, rowspan=10)

        Enviarbtn = Button(self.mainFrame_other, text="Enviar", command=lambda: enviar(Mens))
        Enviarbtn.grid(column=3,row=14, pady= (0,13))
        Descartarbtn = Button(self.mainFrame_other, text="Descartar", command= lambda: descartar())
        Descartarbtn.grid(column=4,row=14, pady= (0,13))

        def enviar(Mens):
            try:
                if Id.get() == "":
                    messagebox.showerror("Error", "Por favor ingrese una identificación")
                else:
                    id = int(Id.get())
            except:
                messagebox.showerror("Error", "Identificación inválida")
                Id.insert(0,"")
            if self.registro.buscarUsuario(id) == None:
                messagebox.showerror("Error", "Identificación no registrada")
            else:
                title = Titulo.get()
                m = Mens.get("1.0",END)[:len(Mens.get("1.0",END)) - 1]
                destinatario: Usuario = self.registro.buscarUsuario(id)
                destinatario.recibirMensaje(self.User.getNombre(),title,m)
                self.User.usarBorrador()
                self.registro.importar()
                self.borradores()

        def descartar():
            if Id.get() != "" or Titulo.get() != "" or Mens.get("1.0", END)[:len(Mens.get("1.0",END)) - 1] != "":
                Y_N = messagebox.askyesno("Advertencia", "Seguro que desea descartar el mensaje?")
                if Y_N:
                    self.User.usarBorrador()
                    self.registro.importar()
                    self.borradores() 


    def redactarMensaje(self):
        # Limpiar el frame para evitar conflictos :)
        self.clear_frame(self.Redactarbtn)

        # Titulo de sección
        Label(self.mainFrame_top, text="Redactar mensaje", font=("Times",20), bg="#fcfcfc", fg="#616583").pack(fill=X, pady=5)
        Label(self.mainFrame_other, text = "*En el campo Id ingrese la identificación del usuario al que desea enviar el mensaje (mensaje sin tildes)", font=("Times",13), bg="#fcfcfc", fg="#616583").grid(column=0,row=0, columnspan=5, pady=6)
        
        # Datos
        Label(self.mainFrame_other, text = "Id:    ", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=1, pady=5)
        Id = StringVar()
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Id).grid(column=1,row=1, pady=5)

        Label(self.mainFrame_other, text = "Titulo:", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=2, pady=5)
        Titulo = StringVar()
        ttk.Entry(self.mainFrame_other, font=("Times",12), textvariable=Titulo, width=77).grid(column=1,row=2, pady=5, columnspan=4)

        Label(self.mainFrame_other, text = "Mensaje                                                                                                                                                                          ", font=("Times",12), bg="#fcfcfc", fg="#000").grid(column=0, row=3, pady=(5,1), columnspan=5)
        Mens = Text(self.mainFrame_other, font=("Times",12), width=99, height=14)
        Mens.grid(column=0,row=4, pady=(1,5), padx=5, columnspan=5, rowspan=10)
        
        Enviarbtn = Button(self.mainFrame_other, text="Enviar", command= lambda: enviar(Mens))
        Enviarbtn.grid(column=2,row=14, pady= (0,13))
        Guardarbtn = Button(self.mainFrame_other, text="Guardar como borrador", command= lambda: guardar(Mens))
        Guardarbtn.grid(column=3,row=14, pady= (0,13))
        Descartarbtn = Button(self.mainFrame_other, text="Descartar", command=lambda: descartar(Mens))
        Descartarbtn.grid(column=4,row=14, pady= (0,13))

        def enviar(Mens):
            try:
                if Id.get() == "":
                    messagebox.showerror("Error", "Por favor ingrese una identificación")
                else:
                    id = int(Id.get())
            except:
                messagebox.showerror("Error", "Identificación inválida")
                Id.set("")
            if self.registro.buscarUsuario(id) == None:
                messagebox.showerror("Error", "Identificación no registrada")
            else:
                title = Titulo.get()
                m = Mens.get("1.0",END)[:len(Mens.get("1.0",END)) - 1]
                destinatario: Usuario = self.registro.buscarUsuario(id)
                destinatario.recibirMensaje(self.User.getNombre(),title,m)
                self.User.usarBorrador()
                self.registro.importar()
                Id.set("")
                Titulo.set("")
                Mens.delete("1.0",END)
    
        def guardar(Mens):
            try:
                if Id.get() == "":
                    messagebox.showerror("Error", "Por favor ingrese una identificación")
                else:
                    id = int(Id.get())
            except:
                messagebox.showerror("Error", "Identificación inválida")
                Id.set("")
            if self.registro.buscarUsuario(id) == None:
                messagebox.showerror("Error", "Identificación no registrada")
            else:
                title = Titulo.get()
                m = Mens.get("1.0",END)[:len(Mens.get("1.0",END)) - 1]
                self.registro.buscarUsuario(self.User.getId()).guardarBorrador(str(id),title,m)
                self.registro.importar()
                Id.set("")
                Titulo.set("")
                Mens.insert("1.0","")

        def descartar(Mens):
            if Id.get() != "" or Titulo.get() != "" or Mens.get("1.0", END)[:len(Mens.get("1.0",END)) - 1] != "":
                Y_N = messagebox.askyesno("Advertencia", "Seguro que desea descartar el mensaje?")
                if Y_N:
                    Id.set("")
                    Titulo.set("")
                    Mens.insert("1.0","")


    def clear_frame(self,btn: Button):
        for w1 in self.mainFrame_top.winfo_children():
            w1.destroy()
        for w2 in self.mainFrame_other.winfo_children():
            w2.destroy()
        
        self.Bandejabtn.config(state=NORMAL)
        self.Leidosbtn.config(state=NORMAL)
        self.Redactarbtn.config(state=NORMAL)
        self.Borradoresbtn.config(state=NORMAL)
        if self.tipo == "administrador":
            self.Modificarbtn.config(state=NORMAL)
            self.ModContraseñabtn.config(state=NORMAL)
            self.Eliminarbtn.config(state=NORMAL)

        btn.config(state=DISABLED)

    def mainbuttonHover(self, btn: Button):
        btn["relief"] = SUNKEN
        btn["borderwidth"] = 1

    def mainbuttonHover_leave(self, btn: Button):
        btn["relief"] = FLAT



class Login:
    def __init__(self):
        self.registro = Registro()
        self.registro.importar()
        self.root = Tk()
        self.root.title("Login Usuario")
        self.root.geometry("400x500")
        self.root.resizable(width=0, height=0)

        # Frame para mostrar "Inicio de sesión"
        self.mainFrame_top = Frame(self.root, height=50, bd=0, relief=SOLID)
        self.mainFrame_top.pack(side="top",fill=X)

        # Frame para usuario y contraseña
        self.mainFrame = Frame(self.root, bd=0, relief=SOLID, bg ="#f1f1f1")
        self.mainFrame.pack(expand=YES, fill=BOTH)
        
        # Titulo del programa
        self.titulo = Label(self.mainFrame_top, text="Inicio de sesión", font=("Times",30), fg="#616583", bg="#f1f1f1", pady=50)
        self.titulo.pack(expand=YES,fill=BOTH)

        # Label y textbox para ingresar el Id
        Idlbl = Label(self.mainFrame, text = "Identificación", font=("Times",14), fg="#616583", bg="#f1f1f1", anchor="w")
        Idlbl.pack(fill=X, padx=20, pady=5)

        self.Id = StringVar()
        self.Idtxt = ttk.Entry(self.mainFrame,font=("Times", 14), textvariable=self.Id)
        self.Idtxt.pack(fill=X, padx=20, pady=10)

        # Label y textbox para ingresar la contraseña
        Pwdlbl = Label(self.mainFrame, text = "Contraseña", font=("Times",14), fg="#616583", bg="#f1f1f1", anchor="w")
        Pwdlbl.pack(fill=X, padx=20,pady=5)

        self.Pwd = StringVar()
        self.Pwdtxt = ttk.Entry(self.mainFrame,font=("Times", 14), textvariable=self.Pwd)
        self.Pwdtxt.pack(fill=X, padx=20, pady=10)
        self.Pwdtxt.config(show="·")

        # Boton para iniciar sesion
        self.Iniciarbtn = Button(self.mainFrame, text="Iniciar sesión", font=("Times", 15, BOLD), bg="#52a5e0", bd=0, fg="#fff", command=self.iniciarSesion)
        self.Iniciarbtn.pack(fill=X, padx=20, pady=20)

        # Estilizando el botón :)
        self.Iniciarbtn.bind("<Enter>", lambda event: self.buttonhover())
        self.Iniciarbtn.bind("<Leave>", lambda event: self.buttonhover_leave())

        self.root.mainloop()
    
    def iniciarSesion(self):
        # Verificación de credenciales de usuario
        Id = self.Idtxt.get()
        Pwd = self.Pwdtxt.get()
        try:
            if self.registro.buscarUsuario(int(Id)) != None:
                user: Usuario = self.registro.buscarUsuario(int(Id))
                if Pwd == user.getPassword():
                    self.root.destroy()
                    Interfaz(user, user.getStatus(), self.registro)
                elif Pwd == "":
                    messagebox.showerror(message="Por favor introduzca una contraseña", title="Error")
                else:
                    self.Pwd.set("")
                    messagebox.showerror(message="Contraseña incorrecta", title="Error")
            else:
                self.Id.set("")
                self.Pwd.set("")
                messagebox.showerror(message="Identificación no registrada", title="Error")
        except:
            self.Id.set("")
            self.Pwd.set("")
            messagebox.showerror(message="Porfavor introduzca usuario y contraseña válidos", title="Error")
        
    def buttonhover(self):
        self.Iniciarbtn["bg"] = "#0F5A90"

    def buttonhover_leave(self):
        self.Iniciarbtn["bg"] = "#52a5e0"

