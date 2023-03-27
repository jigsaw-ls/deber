from tkinter import *
from tkinter import messagebox
from nmap import *
from tkinter import ttk
from scapy.all import ARP, Ether, srp
import mysql.connector
from twilio.rest import Client 

conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Root970303*",
        database="ECUSECRET"
)




def recovery_p():
	run2 = conexion.cursor()
	run2.execute("update CREATEU set password = sha('{}') where username = '{}' and recovery = '{}';".format(pas.get(),user.get(),recov.get()))
	conexion.commit()
	vl = run2.fetchall()
	vl1 = run2.rowcount
	if vl1 == 1: 
		messagebox.showinfo("Suseccfull","Cambio exitoso de contraseña\n Usuario : '{}'".format(user.get()))
	else:
		messagebox.showinfo("Error","Datos Ingresados Erroneos")

def register_1():
	run = conexion.cursor()
	run.execute("INSERT INTO CREATEU (name,lastn,username,password,recovery) VALUES ('{}','{}','{}',sha('{}'),'{}')".format(name.get(),lastn.get(),username.get(),password.get(),recovery.get()))
	conexion.commit()
	messagebox.showinfo("Suseccfull","EL usuario a sido creado \nsatisfactoriamente")




def login():
	run1 =conexion.cursor()
	run1.execute("SELECT * FROM CREATEU where username= '{}' and password= sha('{}')".format(username.get(),password.get()))
	vl = run1.fetchall()
	vl1 = run1.rowcount
	if  vl1 == 1:
		messagebox.showinfo("Inicio de Sesion correcto","Bienvnido usuario: {}".format(username.get()))
		windows.destroy()
		windows_principal()
	else:
		messagebox.showinfo("Inicio de Sesion incorrecto","Credenciales no existentes")

def mostrar_menu(event):
    menu_click.post(event.x_root, event.y_root)



def tlo():
	windows1.destroy()
	Ecua_Secret()


def tla():
	recovery.destroy()
	Ecua_Secret()

def salir():
	condicion = messagebox.askquestion("Salir","Deceas Salir")
	if condicion == "yes":
		windows.destroy()


def enviar_txt():
	contenido = men.get("1.0","end")

	account_sid = 'AC76d30fd10deeb7ea9b90a206ff2e7986' 
	auth_token = '82a30f87d88b6e09108a676a010acf71' 
	client = Client(account_sid, auth_token) 
 
	message = client.messages.create(  
				messaging_service_sid='MG57a4f6ee29ad804852c84eb7b8a2fd0e', 
				body='{}'.format(contenido),
				to='{}'.format(numcell.get()) 
				) 

	print(message.sid)






	men.delete("1.0","end")


def send_sms():
	ss = Toplevel(menu1)
	ss.geometry("300x300")
	ss.title("Envio de SmS")
	ss.resizable(False,False)
	
	global numcell
	numcell = StringVar()


	msj = Label(ss,text="Numero de Tlf",font=("Dyuthi",15)).place(x=65,y=60)
	numc = Entry(ss,textvariable=numcell).place(x=65,y=80)

	global men
	msj = Label(ss,text="Cuerpo del Mensaje",font=("Dyuthi",15)).place(x=65,y=120)
	men = Text(ss,width=20,height=5)
	men.place(x=65,y=150)
	bt1 = Button(ss,text="Enviar Mesaje",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="10",height="1",cursor="hand2",command=enviar_txt).place(x=100,y=260)

	ss.mainloop()

def wirles_connect():
	wc = Toplevel(menu1)
	wc.resizable(False,False)
	wc.geometry("600x250")
	wc.title("Dispositivos conectados a la red" )

# Crear Treeview
	tabla = ttk.Treeview(wc)
	tabla["columns"] = ("ip", "mac", "hostname")
	tabla.heading("#0", text="ID")
	tabla.heading("ip", text="Dirección IP")
	tabla.heading("mac", text="Dirección MAC")
	tabla.heading("hostname", text="Nombre de Host")
	tabla.column("#0", width=50)
	tabla.column("ip", width=150)
	tabla.column("mac", width=150)
	tabla.column("hostname", width=200)
	tabla.pack()

# Obtener dispositivos conectados
	devices = []
	arp = ARP(pdst='192.168.100.1/24')
	ether = Ether(dst='ff:ff:ff:ff:ff:ff')
	packet = ether/arp
	result = srp(packet, timeout=3, verbose=0)[0]
	for sent, received in result:
		devices.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': ""})

# Agregar dispositivos al Treeview
	for i, device in enumerate(devices):
		tabla.insert("", END, text=str(i+1), values=(device['ip'], device['mac'], device['hostname']))




	wc.mainloop()

def botnet_jgrt():
	botnet_w = Toplevel(menu1)
	botnet_w.geometry("500x400")
	botnet_w.resizable(False,False)
	botnet_w.title("Botnet Jigsaw-Root")
	botnet_w.config(bg="black")
	




	botnet_w.mainloop()


def vl_victima():
	vl_r = Toplevel(menu1)
	vl_r.title("See More Victims")
	vl_r.resizable(False,False)
	vl_r.geometry("1250x500")

	
	tabla = ttk.Treeview(vl_r,height="20")

	tabla["columns"]= ("name","lastn","direcc","numcell","gmail","numced","socialac")

	tabla.column("#0", width=50)
	tabla.column("name", width=170)
	tabla.column("lastn", width=170)
	tabla.column("direcc", width=170)
	tabla.column("numcell", width=150)
	tabla.column("gmail", width=200)
	tabla.column("numced", width=150)
	tabla.column("socialac", width=200)


	tabla.heading("#0", text="ID")
	tabla.heading("name", text="Nombres CP",anchor=CENTER)
	tabla.heading("lastn", text="Apellidos CP",anchor=CENTER)
	tabla.heading("direcc", text="Dirección VV",anchor=CENTER)
	tabla.heading("numcell", text="Número CL",anchor=CENTER)
	tabla.heading("gmail", text="Correo EL",anchor=CENTER)
	tabla.heading("numced", text="Cedula NM",anchor=CENTER)
	tabla.heading("socialac", text="Redes SO",anchor=CENTER)
	tabla.pack()


	run = conexion.cursor()
	run.execute("SELECT * FROM VICTIMA")
	for row in run:
		tabla.insert("", END, text=row[0], values=row[1:])

	vl_r.mainloop()


def up_vic():
	run = conexion.cursor()
	run.execute("insert into VICTIMA(name,lastn,direcc,numcell,gmail,numced,socialac) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(nombre.get(),apellido.get(),direccion.get(),numcell.get(),gmail.get(),cedula.get(),social.get()))
	conexion.commit()





def rg_victima():
	rg_v = Toplevel(menu1)
	rg_v.resizable(False,False)
	rg_v.geometry("550x350")
	rg_v.config(bg="black")
	rg_v.title("Register Victim")
	t1 = Label(rg_v,text="Ingreso de Datos de Victima",font=("Dyuthi",20),bg="black",fg="red").pack()
	na1 = Label(rg_v,text="Nombre Completos",font=("Dyuthi",15),bg="black",fg="green").place(x=10,y=60)
	la1 = Label(rg_v,text="Apellidos Completos",font=("Dyuthi",15),bg="black",fg="green").place(x=188,y=60)
	di1 = Label(rg_v,text="Direcion Domiciliaria",font=("Dyuthi",15),bg="black",fg="green").place(x=370,y=60)
	nu1 = Label(rg_v,text="Numero Celular",font=("Dyuthi",15),bg="black",fg="green").place(x=10,y=130)
	gm1 = Label(rg_v,text="Correo Electronico",font=("Dyuthi",15),bg="black",fg="green").place(x=188,y=130)
	nc1 = Label(rg_v,text="Numero de Cedula",font=("Dyuthi",15),bg="black",fg="green").place(x=370,y=130)
	so1 = Label(rg_v,text="Redes Sociales",font=("Dyuthi",15),bg="black",fg="green").place(x=210,y=190)
	global nombre
	global apellido
	global direccion
	global numcell
	global gmail
	global cedula
	global social

	nombre = StringVar()
	apellido = StringVar()
	direccion = StringVar()
	numcell = StringVar()
	gmail = StringVar()
	cedula = StringVar()
	social = StringVar()

	nna1 = Entry(rg_v,textvariable=nombre).place(x=10,y=80)
	lla1 = Entry(rg_v,textvariable=apellido).place(x=188,y=80)
	ddi1 = Entry(rg_v,textvariable=direccion).place(x=370,y=80)
	nnu1 = Entry(rg_v,textvariable=numcell).place(x=10,y=150)
	ggm1 = Entry(rg_v,textvariable=gmail).place(x=188,y=150)
	nnc1 = Entry(rg_v,textvariable=cedula).place(x=370,y=150)
	sso1 = Entry(rg_v,textvariable=social).place(x=188,y=210)



	bt1 = Button(rg_v,text="Registrar",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="12",height="1",cursor="hand2",command=up_vic).place(x=150,y=300)

	bt2 = Button(rg_v,text="Retroceder",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="12",height="1",cursor="hand2",command=rg_v.destroy).place(x=290,y=300)



	rg_v.mainloop()


def windows_principal():
	global menu1

	menu1 = Tk()
	menu1.title("Agencia de Servicio Secreto Ecuatoriano")
	menu1.resizable(False,False)
	menu1.geometry("600x300")
	img_bg = PhotoImage(file="img/menu_principal/secret.png")
	img_bg1 = Label(menu1, image = img_bg,bd=2).place(x=0,y=0,relwidth=1,relheight=1)
	

	#####
	global menu_click
	menu_click = Menu(menu1, tearoff=0)
	
	menu_click.add_command(label="Motrar Conectados",command=wirles_connect)
	menu_click.add_command(label="Enviar SMS",command=send_sms)
	menu_click.add_command(label="Desactivar Redes")
	menu_click.add_command(label="Botnet-Jigsaw-Root",command=botnet_jgrt)
	menu1.bind("<Button-3>", mostrar_menu)
	#######





	menu_principal = Menu(menu1)

	elm1 = Menu(menu_principal,tearoff=0)
	elm1.add_command(label="Ingresar Datos de la Victima",command=rg_victima)
	elm1.add_command(label="Ver Datos de la Victima",command=vl_victima)
	elm1.add_command(label="Eliminar Datos de la Victima",command=lambda: print('Opción 1 seleccionada'))
	menu_principal.add_cascade(label="Datos V-ESP",menu=elm1)





	elm2 = Menu(menu_principal, tearoff=0)
	elm2.add_command(label="Prueba1",command=lambda: print('Opción 1 seleccionada'))
	elm2.add_command(label="Prueba2",command=lambda: print('Opción 2 seleccionada'))
	menu_principal.add_cascade(label="Escaner-Vuln", menu=elm2)



	elm3 = Menu(menu_principal, tearoff=0)
	elm3.add_command(label="Prueba1",command=lambda: print('Opción 1 seleccionada'))
	elm3.add_command(label="Prueba2",command=lambda: print('Opción 2 seleccionada'))
	menu_principal.add_cascade(label="Exploit-Win", menu=elm3)



	menu1.config(menu=menu_principal)
	menu1.mainloop()


def recovery_1():
	windows1.destroy()
	global recovery
	recovery = Tk()
	recovery.title("Recuperar Contraseña")
	recovery.geometry("250x450")
	recovery.resizable(False,False)
	img_bg1 = PhotoImage(file="img/login/military.png")
	t1 = Label(recovery,text="Cambiar Contraseña",font=("Dyuthi",20),fg="red").pack()
	im1_bg1 = Label(recovery, image = img_bg1,bd=2).pack()
	us = Label(recovery,text="Usuario",font=("Dyuthi",12),fg="yellow").place(x=10,y=200)
	pa = Label(recovery,text="Recovery",font=("Dyuthi",12),fg="blue").place(x=10,y=250)
	np = Label(recovery,text="Nueva Contraseña",font=("Dyuthi",12),fg="red").place(x=10,y=300)
	global user
	global pas
	global recov

	user = StringVar()
	pas = StringVar()
	recov = StringVar()

	usu1 = Entry(recovery,textvariable=user).place(x=10,y=215)
	pas1 = Entry(recovery,textvariable=recov).place(x=10,y=265)
	rec1 = Entry(recovery,textvariable=pas,show="*").place(x=10,y=315)
	bt1 = Button(recovery,text="Cambiar Contraseña",command=recovery_p,font=("Dyuthi",9),bd=3,width="15").place(x=50,y=360)
	bt2 = Button(recovery,text="Menu-Principal",command=tla,font=("Dyuthi",9),width="15",bd=3).place(x=50,y=400)
	recovery.mainloop()

def createaccount():
	windows.destroy()
	global windows1
	windows1 = Tk()
	windows1.title("Register Agencia SS ECU")
	windows1.resizable(False,False)
	windows1.geometry("400x300")
	t1 = LabelFrame(windows1,text="Regitrar Cuenta SS ECU",bd=5,width="365",height="275",font=("Dyuthi",20),fg="red").place(x=18,y=10)
	global name
	global lastn
	global username
	global password
	global recovery
	
	name = StringVar()
	lastn = StringVar()
	username = StringVar()
	password = StringVar()
	recovery = StringVar()
	na = Label(windows1, text="Nombres Completos",font=("Dyuthi",12)).place(x=30,y=50)
	la = Label(windows1, text="Apellidos Completos",font=("Dyuthi",12)).place(x=235,y=50)
	us = Label(windows1,text="Usuario",font=("Dyuthi",12)).place(x=30,y=100)
	pa = Label(windows1,text="Contraseña",font=("Dyuthi",12)).place(x=285,y=100)
	ke = Label(windows1,text="Key Recovery",font=("Dyuthi",12)).place(x=155,y=150)

	na1 = Entry(windows1,textvariable=name,width="17").place(x=30,y=70)
	la1 = Entry(windows1,textvariable=lastn,width="16").place(x=235,y=70)
	us1 = Entry(windows1,textvariable=username,width="17").place(x=30,y=120)
	pa1 = Entry(windows1,textvariable=password,width="16",show="*").place(x=235,y=120)
	ke1 = Entry(windows1,textvariable=recovery,width="17").place(x=130,y=170)
	bt1 = Button(windows1,text="Registrar",width="18",bd=3,font=("Dyuthi",9),bg="yellow",cursor="hand2",command=register_1).place(x=127,y=200)
	bt2 = Button(windows1,text="Recovery-Pass",width="7",bd=3,font=("Dyuthi",9),bg="blue",cursor="hand2",command=recovery_1).place(x=120,y=235)
	bt3 = Button(windows1,text="Retroceder",width="7",bd=3,font=("Dyuthi",9),bg="red",cursor="hand2",command=tlo).place(x=210,y=235)

	windows1.mainloop()







def Ecua_Secret():
	global windows
	windows = Tk()
	windows.geometry("600x400")
	windows.resizable(False,False)

	############

	frame = Frame(windows,width="250",height="400",bd=15,relief="groove", bg="purple").place(x=0,y=0)
	img = PhotoImage(file="img/login/geo.png")
	img_lbl = Label(frame, image = img).place(x=60,y=20)

	t1 = Label(frame,text="Instituto \nSuperior Guayaquil",font=("Dyuthi",15),fg="sky blue", bg="brown").place(x=45,y=200)
	t2 = Label(frame,text="Creador por\nJigsaw-Root",font=("Dyuthi",15),fg="sky blue",bg="brown").place(x=70,y=270)
	t3 = Label(frame,text="Derechos de autor reservado °", font=("Dyuthi",9),fg="sky blue",bg="brown").place(x=45, y=340)

	###########

	frame1 = Frame(windows,width="350",height="400",bd=15,relief="sunken",).place(x=250,y=0)
	img1 = PhotoImage(file = "img/login/login.png")

	ubi_img = Label(frame1, image = img1,).place(x=350,y=20)
	log = Label(frame1, text="Agencia Ecuatoriana SS",font=("Lato Black",20),fg="red").place(x=290,y=180)
	us1 = Label(frame1,text="Usuario",font=("Gidugu",14),fg="black").place(x=280,y=217)
	pas1 = Label(frame1,text="Contraseña",font=("Gidugu",14),fg="black").place(x=280,y=267)
	global username
	global password


	username = StringVar()
	password = StringVar()

	u1 = Entry(frame1,textvariable=username,width="20",bd=3).place(x=280,y=240)
	p1 = Entry(frame1,textvariable=password,width="20",bd=3,show="*").place(x=280,y=290)

	bt1 = Button(frame1,text="Iniciar Sesion",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="30",height="1",cursor="hand2",command=login).place(x=310,y=325)
	bt2 = Button(frame1,text="Crear Cuenta",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="8",height="1",cursor="hand2",command=createaccount).place(x=340,y=355)
	bt3 = Button(frame1,text="-Salir-",fg="black",bg="green",bd=2,font=("Dyuthi",9),width="8",height="1",cursor="hand2", command=salir).place(x=440,y=355)







	windows.mainloop()






Ecua_Secret()
#windows_principal()
