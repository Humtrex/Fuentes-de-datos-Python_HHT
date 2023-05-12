from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter.messagebox as msgbox

class Widgets:
    def __init__(self): 

        self.raiz = Tk()
        
        self.raiz.title("Muestra Widgets")

        self.nombre = StringVar()
        self.Apaterno = StringVar()
        self.Amaterno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()

        #Frames
        mainFrame=ttk.Frame(self.raiz, padding="5 10 20 10")
        mainFrame.grid(column=0, row=0)
                
        datosFrame = ttk.Frame(mainFrame, padding="5 3 30 10",relief="raised") 
        datosFrame.grid(column=0, row=0,columnspan=2,rowspan=3)  

        aficionesFrame = ttk.Frame(mainFrame,padding="5 3 15 15",relief="raised")  
        aficionesFrame.grid(column=0, row=4, columnspan=2)

        ocupacionFrame = ttk.Frame(mainFrame,padding="10 10 10 25")
        ocupacionFrame.grid(column=2,row=0, rowspan=3)

        estadoFrame = ttk.Frame(mainFrame,padding="10 10 10 25")
        estadoFrame.grid(column=2,row=4)

        #Entrys
        self.nombreEntry = ttk.Entry(datosFrame, textvariable=self.nombre) 
        self.nombreEntry.grid(column=1, row=0, sticky=(W,E), columnspan=2)
        self.ApaternoEntry = ttk.Entry(datosFrame, textvariable=self.Apaterno) 
        self.ApaternoEntry.grid(column=1, row=1, sticky=(W,E), columnspan=2)
        self.AmaternoEntry = ttk.Entry(datosFrame, textvariable=self.Amaterno) 
        self.AmaternoEntry.grid(column=1, row=2, sticky=(W,E), columnspan=2)
        self.correoEntry = ttk.Entry(datosFrame, textvariable=self.correo) 
        self.correoEntry.grid(column=1, row=3, sticky=(W,E), columnspan=2)
        self.movilEntry = ttk.Entry(datosFrame, textvariable=self.movil) 
        self.movilEntry.grid(column=1, row=4, sticky=(W,E), columnspan=2)   

        #Labels
        ttk.Label(datosFrame, text="Nombre:",padding=(5,10,5,10)).grid(column=0, row=0) 
        ttk.Label(datosFrame, text="A.Paterno: ",padding=(5,10,5,10)).grid(column=0, row=1)
        ttk.Label(datosFrame, text="A.Materno:",padding=(5,10,5,10)).grid(column=0, row=2) 
        ttk.Label(datosFrame, text="Correo: ",padding=(5,10,5,10)).grid(column=0, row=3)
        ttk.Label(datosFrame, text="Movil:",padding=(5,10,5,10)).grid(column=0, row=4) 
        
        ttk.Label(aficionesFrame, text="Aficiones:",padding=(5,5,5,5)).grid(column=0, row=0)

        #Checkbutton
        self.aficiones = BooleanVar()
        self.aficiones2 = BooleanVar()
        self.aficiones3 = BooleanVar()
        chkLeer = ttk.Checkbutton(aficionesFrame, text="Leer",variable = self.aficiones) 
        chkLeer.grid(column=0, row=2)   
        chkMusica = ttk.Checkbutton(aficionesFrame, text="Musica",variable = self.aficiones2) 
        chkMusica.grid(column=1, row=2) 
        chkVideojuegos = ttk.Checkbutton(aficionesFrame, text="Videojuegos",variable = self.aficiones3) 
        chkVideojuegos.grid(column=3, row=2) 

        #Radiobutton
        self.ocupacion = StringVar()
        estudiante=ttk.Radiobutton(ocupacionFrame, text='Esudiante', variable=self.ocupacion, value ='Estudiante')
        estudiante.grid(column=0,sticky=W)
        empleado=ttk.Radiobutton(ocupacionFrame, text='Empleado', variable=self.ocupacion, value ='Empleado')
        empleado.grid(column=0,sticky=W)
        desempleado=ttk.Radiobutton(ocupacionFrame, text='Desempleado', variable=self.ocupacion, value ='Desempleado')
        desempleado.grid(column=0,sticky=W)

        #Combobox
        self.estado = StringVar()
        comboEstados = ttk.Combobox(estadoFrame, textvariable=self.estado)
        comboEstados.grid()
        comboEstados['values'] = ("Aguascalientes","Baja California","Baja California Sur", "Campeche",
                            "Coahuila","Colima","Chiapas","Chihuahua","Durango","Distrito Federal","Guanajuato",
                            "Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos", "Nayarit", 
                            "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
                            "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", 
                            "Zacatecas")

        #Buttons
        guardar=ttk.Button(mainFrame,text="Guardar",command=self.guardar)
        guardar.grid(column=0,row=5, sticky=(W))

        cancelar=ttk.Button(mainFrame,text="Cancelar",command=self.limpiar_campos)
        cancelar.grid(column=1, row=5, sticky=(W))

        cancelar=ttk.Button(mainFrame,text="Ver datos",command=self.ver_datos)
        cancelar.grid(column=2, row=5, sticky=(W))

        self.raiz.mainloop()

    # Función para guardar los datos en un archivo CSV
    def guardar(self):
        # Obtener los datos del formulario
        nombre = self.nombre.get()
        a_paterno = self.Apaterno.get()
        a_materno = self.Amaterno.get()
        correo = self.correo.get()
        movil = self.movil.get()

        estado = self.estado.get()

        ocupacion = self.ocupacion.get()

        aficiones = self.aficiones.get()
        aficiones2 = self.aficiones2.get()
        aficiones3 = self.aficiones3.get()

        with open("datos.csv", "a", newline="") as archivo:
            if archivo.tell() == 0:
                archivo.write("Nombre,A_paterno,A_materno,Correo,Movil,Leer,Musica,Videojuegos,Estado,Ocupacion\n")
            
            linea = f"{nombre},{a_paterno},{a_materno},{correo},{movil},{aficiones},{aficiones2},{aficiones3},{estado},{ocupacion}\n"
            
            archivo.write(linea)

        # mostrar mensaje de confirmación
        msgbox.showinfo("Guardar datos", "Los datos han sido guardados correctamente.")

        # Reiniciar campos del formulario
        self.nombreEntry.delete(0, "end")
        self.ApaternoEntry.delete(0, "end")
        self.AmaternoEntry.delete(0, "end")
        self.correoEntry.delete(0,"end")
        self.movilEntry.delete(0, "end")
        self.aficiones.set(False)
        self.aficiones2.set(False)
        self.aficiones3.set(False)
        self.estado.set("Estados(32)")
        self.ocupacion.set("")

    def limpiar_campos(self):
        # Reiniciar campos del formulario
        self.nombreEntry.delete(0, "end")
        self.ApaternoEntry.delete(0, "end")
        self.AmaternoEntry.delete(0, "end")
        self.correoEntry.delete(0,"end")
        self.movilEntry.delete(0, "end")
        self.aficiones.set(False)
        self.aficiones2.set(False)
        self.aficiones3.set(False)
        self.estado.set("Estados(32)")
        self.ocupacion.set("")

    def ver_datos(self):
        #Abrir el archivo para lectura
        with open('datos.csv', 'r') as archivo:
            datos = []
            #Leer cada línea del archivo y agregar a la lista de datos
            for linea in archivo:
                datos.append(linea.strip().split(','))

        #Crear una nueva ventana emergente
        ventana = Toplevel(self.raiz)
        ventana.title("Datos almacenados")

        #Agregar una tabla de datos a la ventana emergente
        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                ttk.Label(ventana, text=dato, width=20, borderwidth=1, relief='solid').grid(row=fila, column=columna)       

Widgets() 
