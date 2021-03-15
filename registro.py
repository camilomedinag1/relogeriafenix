from tkinter import *
import tkinter
import mysql.connector
from tkinter import messagebox
from paramiko import *
import os
import paramiko

# conexion base de datos

mydb = mysql.connector.connect(
  host="192.168.0.20",
  user="root",
  password="camilomedinag1",
  database="estado"
  
)



mywindow = Tk()
mywindow.geometry("300x550")
mywindow.title("Estado de Relojes")
mywindow.resizable(False,False)
mywindow.config(background = "#E9F0F0")
main_title = Label(text="Registro Relojes", font=("Cambria", 13), bg="#7DC9D9", width="550", height="2")
main_title.pack()


nombre_label = Label(text="Nombre", bg="#E9F0F0")
nombre_label.place(x=22, y=70)
apellido_label = Label(text="Apellido", bg="#E9F0F0")
apellido_label.place(x=22, y=130)
cedula_label = Label(text="Cedula", bg="#E9F0F0")
cedula_label.place(x=22, y=190)
factura_label = Label(text="Factura", bg="#E9F0F0")
factura_label.place(x=22, y=250)
marca_label = Label(text="Marca", bg="#E9F0F0")
marca_label.place(x=22, y=310)
modelo_label = Label(text="Modelo", bg="#E9F0F0")
modelo_label.place(x=22, y=370)
celular_label = Label(text="Celular", bg="#E9F0F0")
celular_label.place(x=22, y=430)



nombre = StringVar()
apellido = StringVar()
cedula = StringVar()
factura = StringVar()
marcha = StringVar()
modelo = StringVar()
celular = StringVar()

nombre_entry = Entry(textvariable=nombre, width="40")
apellido_entry = Entry(textvariable=apellido, width="40")
cedula_entry = Entry(textvariable=cedula, width="40")
factura_entry = Entry(textvariable=factura, width="40")
marcha_entry = Entry(textvariable=marcha, width="40")
modelo_entry = Entry(textvariable=modelo, width="40")
celular_entry = Entry(textvariable=celular, width="40")

nombre_entry.place(x=22, y=100)
apellido_entry.place(x=22, y=160)
cedula_entry.place(x=22, y=220)
factura_entry.place(x=22, y=280)
marcha_entry.place(x=22, y=340)
modelo_entry.place(x=22, y=400)
celular_entry.place(x=22, y=460)


#insertar los datos en la db
def fun():
    nombrea = nombre.get()
    apellidoa = apellido.get()
    cedulaa = cedula.get()
    facturaa = factura.get()
    marchaa = marcha.get()
    modeloa = modelo.get()
    celulara = celular.get()
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO relog (nombre, apellido, cedula, factura, marcha, modelo, estado, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nombrea,apellidoa,cedulaa,facturaa,marchaa,modeloa,1,celulara)
    mycursor.execute(sql, val)
    mydb.commit()
   
    nombre.set("")
    apellido.set("")
    cedula.set("")
    factura.set("")
    marcha.set("")
    modelo.set("")
    celular.set("")
    
    messagebox.showinfo("Registro Exitoso" , "Se registro un nuevo producto")
    



submit_btn = Button(mywindow, text="Registrar", command= fun , width="30", height="2", bg="#7DC9D9" )
submit_btn.place(x=33, y=500)


barramenu = Menu(mywindow)
mywindow.config(menu=barramenu)
def funcion():
    otra_ventana1 = tkinter.Toplevel(mywindow)
    mywindow.iconify()
    otra_ventana1.geometry("800x550")
    otra_ventana1.title("Buscar por cedula")
    otra_ventana1.resizable(True,True)
    otra_ventana1.config(background = "#E9F0F0")
    bc_title = Label(otra_ventana1, text="Buscar por cedula", font=("Cambria", 13), bg="#7DC9D9", width="550", height="2")
    bc_title.pack()
    bc_label = Label(otra_ventana1,text="Numero de cedula", bg="#E9F0F0")
    bc_label.place(x=22, y=70)
    cedula1 = StringVar()
    cedula1_entry = Entry(otra_ventana1,textvariable=cedula1, width="40")
    cedula1_entry.place(x=22, y=100)
   
    
    def buscarc():
        #busqueda en la db
        cd = cedula1.get()
        mycursor1 = mydb.cursor()

        sql = "SELECT (nombre) FROM relog WHERE cedula =" + cd
    
        mycursor1.execute(sql)
        
        myresult = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Nombre:", bg="#E9F0F0")
        bc_label.place(x=22, y=150)
        bc_label = Label(otra_ventana1,text=myresult, bg="#E9F0F0")
        bc_label.place(x=22, y=170)
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (apellido) FROM relog WHERE cedula =" + cd
    
        mycursor1.execute(sql)
        
        myresult1 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Apellido:", bg="#E9F0F0")
        bc_label.place(x=92, y=150)
        bc_label = Label(otra_ventana1,text=myresult1, bg="#E9F0F0")
        bc_label.place(x=92, y=170)
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (cedula) FROM relog WHERE cedula =" + cd
    
        mycursor1.execute(sql)
        
        myresult2 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Cedula:", bg="#E9F0F0")
        bc_label.place(x=159, y=150)
        bc_label = Label(otra_ventana1,text=myresult2, bg="#E9F0F0")
        bc_label.place(x=152, y=170) #cada 70
        
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (factura) FROM relog WHERE cedula = "+ cd
    
        mycursor1.execute(sql)
        
        myresult3 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Factura:", bg="#E9F0F0")
        bc_label.place(x=229, y=150)
        bc_label = Label(otra_ventana1,text=myresult3, bg="#E9F0F0")
        bc_label.place(x=230, y=170) #cada 70
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (marcha) FROM relog WHERE cedula ="+ cd
    
        mycursor1.execute(sql)
        
        myresult4 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Marca:", bg="#E9F0F0")
        bc_label.place(x=292, y=150)
        bc_label = Label(otra_ventana1,text=myresult4, bg="#E9F0F0")
        bc_label.place(x=292, y=170) #cada 70
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (modelo) FROM relog WHERE cedula ="+ cd
    
        mycursor1.execute(sql)
        
        myresult4 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Modelo:", bg="#E9F0F0")
        bc_label.place(x=362, y=150)
        bc_label = Label(otra_ventana1,text=myresult4, bg="#E9F0F0")
        bc_label.place(x=362, y=170) #cada 70
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (estado) FROM relog WHERE cedula =" + cd
    
        mycursor1.execute(sql)
        
        myresult5 = mycursor1.fetchall()
        
        estado = myresult5
        
        num =  estado[-1]
        
        
        r = ""
        
        if (estado == [(1,)]):
            r = "Pendiente de cotizacion"
        else:    
            if  (estado == [(2,)]):
                r = "Pendiente de repiesto"
            else:
                if  (estado == [(3,)]):
                    r = "En reparacion"
                else:
                    if  (estado == [(4,)]):
                        r = "En observacion"
                    else:    
                        if  (estado == [(5,)]):
                            r = "En Sincronozacion"
                        else:
                            if (estado == [(6,)]):
                                r = "Listo para entrgar"    
                            else: 
                                 r= "Entregado"
            
        
                    
               
        bc_label = Label(otra_ventana1,text="Estado:", bg="#E9F0F0")
        bc_label.place(x=282, y=100)
        bc_label = Label(otra_ventana1,text=r, bg="#E9F0F0")
        bc_label.place(x=325, y=100) #cada 70
        
        myCursor1 = mydb.cursor()

        sql = "SELECT (celular) FROM relog WHERE cedula = "+ cd
    
        mycursor1.execute(sql)
        
        myresult8 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana1,text="Celular:", bg="#E9F0F0")
        bc_label.place(x=502, y=150)
        bc_label = Label(otra_ventana1,text=myresult8, bg="#E9F0F0")
        bc_label.place(x=502, y=170) #cada 70
        
        mycursor1 = mydb.cursor()
        
        
        
    bc_btn = Button(otra_ventana1, text="Buscar", command= buscarc, width="30", height="2", bg="#7DC9D9" )
    bc_btn.place(x=300, y=440)    
    #modificar estado
    
    def seleccionar1():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a cotizacion")
        #info4.place(x=50, y=350)
        
        mycursor9 = mydb.cursor()

        sql = "UPDATE relog SET estado = 1 WHERE cedula = " + este 

        mycursor9.execute(sql)

        mydb.commit()
        
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a cotizacion")
        pencoti.set(None)
    def seleccionar2():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a pendiente de repuesto")
        #info4.place(x=50, y=350)
        
        mycursor10 = mydb.cursor()

        sql = "UPDATE relog SET estado = 2  WHERE cedula =" + este

        mycursor10.execute(sql)

        mydb.commit()
        
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a pendiente de repuesto")
        penrepu.set(None)
    
    def seleccionar3():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a en reparacio")
        #info4.place(x=50, y=350)
        
        mycursor11 = mydb.cursor()

        sql = "UPDATE relog SET estado = 3 WHERE cedula = " + este

        mycursor11.execute(sql)

        mydb.commit()   
        
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a en reparacio")   
        enreparacion.set(None)      
    
    def seleccionar4():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a en Observacion")
        #info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 4 WHERE cedula =" + este

        mycursor12.execute(sql)

        mydb.commit()
        
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a en Observacion")   
        enobse.set(None)    
        
        
                    
    def seleccionar5():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a en sincromizacion")
        #info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 5 WHERE cedula =" + este

        mycursor12.execute(sql)

        mydb.commit() 
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a en sincromizacion")   
        ensincro.set(None) 
        
        
    def seleccionar6():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a en listo para ser recogido")
        #info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 6 WHERE cedula =" + este

        mycursor12.execute(sql)

        mydb.commit()
        
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a en listo para ser recogido")   
        listo.set(None) 
        # llamada automatica
    
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("192.168.0.20", username="camilo", password="camilomedinag1")
        
        comando = client.exec_command("mkdir -p /home/camilo/Workspace/sub1/")
        
        print(comando)
        
     
        
        
    # aqui iria la llamada automatica
    
    
    def seleccionar7():
        cd = cedula1.get()
        este = "'"+ cd +"'"
        #info4 = Label(otra_ventana1)
        #info4.config(text="Se cambio el estado a en Articulo entreagdo")
        #info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 7 WHERE cedula =" + este

        mycursor12.execute(sql)

        mydb.commit()
        messagebox.showinfo("Registro Exitoso" , "Se cambio el estado a en Articulo entreagdo")   
        entregado.set(None)     
        
    pencoti = IntVar()
    penrepu = IntVar()        
    enreparacion =IntVar()
    enobse = IntVar()
    ensincro = IntVar()
    listo = IntVar()                
    entregado = IntVar()        


    Radiobutton(otra_ventana1, text="Pendiente de cotizacion", variable=pencoti, value=1, 
                 command=seleccionar1,).pack(anchor="e")
    Radiobutton(otra_ventana1, text="pendiente de repuesto  ", variable=penrepu, value=1, 
                 command=seleccionar2).pack(anchor="e")
    Radiobutton(otra_ventana1, text="En reparacion          ", variable=enreparacion, value=1, 
                 command=seleccionar3,).pack(anchor="e")
    Radiobutton(otra_ventana1, text="En observacion         ", variable=enobse, value=1, 
                 command=seleccionar4).pack(anchor="e")
    Radiobutton(otra_ventana1, text="En sincronizacion      ", variable=ensincro, value=1, 
                 command=seleccionar5,).pack(anchor="e")
    Radiobutton(otra_ventana1, text="Listo para entrega     ", variable=listo, value=1, 
                 command=seleccionar6).pack(anchor="e")
    Radiobutton(otra_ventana1, text="Entregado al cliente   ", variable=entregado, value=1, 
                 command=seleccionar7).pack(anchor="e")
    
    
    
    

    
    
def funcion2():
    otra_ventana2 = tkinter.Toplevel(mywindow)
    mywindow.iconify()
    otra_ventana2.geometry("800x550")
    otra_ventana2.title("Buscar por factura")
    otra_ventana2.resizable(False,False)
    otra_ventana2.config(background = "#E9F0F0")
    bf_title = Label(otra_ventana2, text="Buscar por facturas", font=("Cambria", 13), bg="#7DC9D9", width="550", height="2")
    bf_title.pack()
    bf_label = Label(otra_ventana2,text="Numero de Factura", bg="#FFEEDD")
    bf_label.place(x=22, y=70)
    factura1 = StringVar()
    factura1_entry = Entry(otra_ventana2,textvariable=factura1, width="40")
    factura1_entry.place(x=22, y=100)
    
    
    def buscarf():
        #busqueda en la db
        f = factura1.get()
        mycursor1 = mydb.cursor()

        sql = "SELECT (nombre) FROM relog WHERE factura ="+ f
    
        mycursor1.execute(sql)
        
        myresult = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Nombre:", bg="#E9F0F0")
        bf_label.place(x=22, y=150)
        bf_label = Label(otra_ventana2,text=myresult, bg="#E9F0F0")
        bf_label.place(x=22, y=170)
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (apellido) FROM relog WHERE factura = " + f
    
        mycursor1.execute(sql)
        
        myresult1 = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Apellido:", bg="#E9F0F0")
        bf_label.place(x=92, y=150)
        bf_label = Label(otra_ventana2,text=myresult1, bg="#E9F0F0")
        bf_label.place(x=92, y=170)
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (cedula) FROM relog WHERE factura =" + f
    
        mycursor1.execute(sql)
        
        myresult2 = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Cedula:", bg="#E9F0F0")
        bf_label.place(x=152, y=150)
        bf_label = Label(otra_ventana2,text=myresult2, bg="#E9F0F0")
        bf_label.place(x=152, y=170) #cada 70
        
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (factura) FROM relog WHERE factura =" + f
    
        mycursor1.execute(sql)
        
        myresult3 = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Factura:", bg="#E9F0F0")
        bf_label.place(x=222, y=150)
        bf_label = Label(otra_ventana2,text=myresult3, bg="#E9F0F0")
        bf_label.place(x=222, y=170) #cada 70
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (marcha) FROM relog WHERE factura = " + f
    
        mycursor1.execute(sql)
        
        myresult4 = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Marca:", bg="#E9F0F0")
        bf_label.place(x=292, y=150)
        bf_label = Label(otra_ventana2,text=myresult4, bg="#E9F0F0")
        bf_label.place(x=292, y=170) #cada 70
        
        
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (modelo) FROM relog WHERE factura =" + f
    
        mycursor1.execute(sql)
        
        myresult4 = mycursor1.fetchall()
    
        
        bf_label = Label(otra_ventana2,text="Modelo:", bg="#E9F0F0")
        bf_label.place(x=362, y=150)
        bf_label = Label(otra_ventana2 ,text=myresult4, bg="#E9F0F0")
        bf_label.place(x=362, y=170) #cada 70
        
        mycursor1 = mydb.cursor()

        sql = "SELECT (estado) FROM relog WHERE factura =" + f
    
        mycursor1.execute(sql)
        
        myresult5 = mycursor1.fetchall()
        
        estado = str(myresult5)
        
        
        r = ""
        
        if (estado == "1"):
            r = "estado" + "pendiente de cotizacion"
        else:    
            if  (estado == "2"):
                r = "pendiente de repiesto"
            else:
                if  (estado == "3"):
                    r = "en reparacion"
                else:
                    if  (estado == "4"):
                        r = "en observacion"
                    else:    
                        if  (estado == "5"):
                            r = "en Sincronozacion"
                        else :
                            r = "listo"    
            
            
        
                    
               
        bc_label = Label(otra_ventana2,text="Estado:", bg="#E9F0F0")
        bc_label.place(x=432, y=150)
        bc_label = Label(otra_ventana2,text=r, bg="#E9F0F0")
        bc_label.place(x=432, y=170) #cada 70
        
        
        
        myCursor1 = mydb.cursor()

        sql = "SELECT (celular) FROM relog WHERE factura = "+ f
    
        mycursor1.execute(sql)
        
        myresult8 = mycursor1.fetchall()
    
        
        bc_label = Label(otra_ventana2,text="Celular:", bg="#E9F0F0")
        bc_label.place(x=502, y=150)
        bc_label = Label(otra_ventana2,text=myresult8, bg="#E9F0F0")
        bc_label.place(x=502, y=170) #cada 70
        
        mycursor1 = mydb.cursor()
        
        
        
    def seleccionar1f():
            
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a cotizacion")
        info4.place(x=50, y=350)
        
        mycursor9 = mydb.cursor()

        sql = "UPDATE relog SET estado = 1 WHERE factura = " + este 

        mycursor9.execute(sql)

        mydb.commit()
        
    def seleccionar2f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a pendiente de repuesto")
        info4.place(x=50, y=350)
        
        mycursor10 = mydb.cursor()

        sql = "UPDATE relog SET estado = 2  WHERE factura =" + este

        mycursor10.execute(sql)

        mydb.commit()
    
    def seleccionar3f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a en reparacio")
        info4.place(x=50, y=350)
        
        mycursor11 = mydb.cursor()

        sql = "UPDATE relog SET estado = 3 WHERE factura = " + este

        mycursor11.execute(sql)

        mydb.commit()            
    
    def seleccionar4f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a en Observacion")
        info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 4 WHERE factura =" + este

        mycursor12.execute(sql)

        mydb.commit()
        
        
                    
    def seleccionar5f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a en sincromizacion")
        info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 5 WHERE factura =" + este

        mycursor12.execute(sql)

        mydb.commit() 
        
        
    def seleccionar6f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a en listo para ser recogido")
        info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 6 WHERE factura =" + este

        mycursor12.execute(sql)

        mydb.commit()     
        
        
    # aqui iria la llamada automatica
    
    
    def seleccionar7f():
        cdf = factura1.get()
        este = "'"+ cdf +"'"
        info4 = Label(otra_ventana2)
        info4.config(text="Se cambio el estado a en Articulo entreagdo")
        info4.place(x=50, y=350)
        
        mycursor12 = mydb.cursor()

        sql = "UPDATE relog SET estado = 7 WHERE factura =" + este

        mycursor12.execute(sql)

        mydb.commit()     
        
    pencoti = IntVar()
    penrepu = IntVar()        
    enreparacion =IntVar()
    enobse = IntVar()
    ensincro = IntVar()
    listo = IntVar()                
    entregado = IntVar()        


    Radiobutton(otra_ventana2, text="Pendiente de cotizacion", variable=pencoti, value=1, 
                 command=seleccionar1f,).pack(anchor="e")
    Radiobutton(otra_ventana2, text="pendiente de repuesto  ", variable=penrepu, value=1, 
                 command=seleccionar2f).pack(anchor="e")
    Radiobutton(otra_ventana2, text="En reparacion          ", variable=enreparacion, value=1, 
                 command=seleccionar3f,).pack(anchor="e")
    Radiobutton(otra_ventana2, text="En observacion         ", variable=enobse, value=1, 
                 command=seleccionar4f).pack(anchor="e")
    Radiobutton(otra_ventana2, text="En sincronizacion      ", variable=ensincro, value=1, 
                 command=seleccionar5f,).pack(anchor="e")
    Radiobutton(otra_ventana2, text="Listo para entrega     ", variable=listo, value=1, 
                 command=seleccionar6f).pack(anchor="e")
    Radiobutton(otra_ventana2, text="Entregado al cliente   ", variable=entregado, value=1, 
                 command=seleccionar7f).pack(anchor="e")
    

    bf_btn = Button(otra_ventana2, text="Buscar", command= buscarf , width="30", height="2", bg="#7DC9D9" )
    bf_btn.place(x=300, y=440)    
    

    
   


buscarmenu=Menu(barramenu, tearoff=0)
buscarmenu.add_command(label="Buscar Por Factura", command=funcion2)
buscarmenu.add_command(label="Buscar Por Cedula", command=funcion)



barramenu.add_cascade(label="Buscar", menu=buscarmenu)

mywindow.mainloop()