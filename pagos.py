from tkinter import *

#diseño de la ventana prinicipal

ventana = Tk()
ventana.title("Sistema Bouffet - mk")
ventana.geometry("1400x800")
ventana.resizable(0,0)
ventana.config(bg="darkblue")

#estableciendo las fuentes
Title=("MS Sans Serif",25)
Subtitle=("Courier", 16, "italic")

#marco de titulo principal
marcoSuperior=Frame(ventana,bd=10, relief=RIDGE, bg="blue")
marcoSuperior.pack(side=TOP)
#titulo principal
tituloPrincipal=Label(marcoSuperior,text="Sistema de Pagos",font=Title,fg="white",bg="blue",width=53)
tituloPrincipal.grid(row=0,column=0)

#Marcos secundarios
marcoMenu=Frame(ventana,bd=10,relief=RIDGE,bg="blue")
marcoMenu.pack(side=LEFT)
marcoCosto=Frame(marcoMenu,bd=2,relief=RIDGE,bg="blue")
marcoCosto.pack(side=BOTTOM)
marcoComida=LabelFrame(marcoMenu, text="Platos",bd=5,font=Subtitle,relief=RIDGE, bg="lightgray")
marcoComida.pack(side=LEFT)
marcoBebidas=LabelFrame(marcoMenu, text="Bebidas",bd=5,font=Subtitle,relief=RIDGE, bg="lightgray")
marcoBebidas.pack(side=LEFT)
marcoPostres=LabelFrame(marcoMenu, text="Platos",bd=5,font=Subtitle,relief=RIDGE, bg="lightgray")
marcoPostres.pack(side=LEFT)
#Marcos para los el lado derecho.
marcoDerecho=Frame(ventana,bd=10,relief=RIDGE,bg="blue")
marcoDerecho.pack(side=RIGHT)
marcoCalculadora=Frame(marcoDerecho,bd=5,relief=RIDGE,bg="blue")
marcoCalculadora.pack()
marcoRecibo=Frame(marcoDerecho,bd=5,relief=RIDGE,bg="blue")
marcoRecibo.pack()
marcoBotones=Frame(marcoDerecho,bd=5,relief=RIDGE,bg="blue")
marcoBotones.pack()

#comida
#etiqueta y boton para seleccionar
Panchos = Checkbutton(marcoComida,text="Panchos",font=Subtitle,onvalue=1,offvalue=0).grid(row=0, column=0, sticky=W)
Sandwich = Checkbutton(marcoComida,text="Sandwich",font=Subtitle,onvalue=1,offvalue=0).grid(row=1, column=0, sticky=W)
Facturas = Checkbutton(marcoComida,text="Facturas",font=Subtitle,onvalue=1,offvalue=0).grid(row=2, column=0, sticky=W)
Pizza = Checkbutton(marcoComida,text="Pizza",font=Subtitle,onvalue=1,offvalue=0).grid(row=3, column=0, sticky=W)
Tortas = Checkbutton(marcoComida,text="Tortas",font=Subtitle,onvalue=1,offvalue=0).grid(row=4, column=0, sticky=W)
Alfajores = Checkbutton(marcoComida,text="Alfajores",font=Subtitle,onvalue=1,offvalue=0).grid(row=5, column=0, sticky=W)
Golosinas = Checkbutton(marcoComida,text="Golosinas",font=Subtitle,onvalue=1,offvalue=0).grid(row=6, column=0, sticky=W)
Chocolates = Checkbutton(marcoComida,text="Chocolates",font=Subtitle,onvalue=1,offvalue=0).grid(row=7, column=0, sticky=W)
#cajas de texto para cada comida
textPanchos=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=0,column=1)
textSanwich=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=1,column=1)
textFacturas=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=2,column=1)
textPizza=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=3,column=1)
textTortas=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=4,column=1)
textAlfajores=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=5,column=1)
textGolosinas=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=6,column=1)
textChocolate=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=7,column=1)

#Bebidas
#etiqueta y boton check
Pepsi = Checkbutton(marcoBebidas,text="Pepsi",font=Subtitle,onvalue=1,offvalue=0).grid(row=0, column=0, sticky=W)
Cocacola = Checkbutton(marcoBebidas,text="Cocacola",font=Subtitle,onvalue=1,offvalue=0).grid(row=1, column=0, sticky=W)
SevenUp = Checkbutton(marcoBebidas,text="SevenUp",font=Subtitle,onvalue=1,offvalue=0).grid(row=2, column=0, sticky=W)
Fanta = Checkbutton(marcoBebidas,text="Fanta",font=Subtitle,onvalue=1,offvalue=0).grid(row=3, column=0, sticky=W)
Baggio = Checkbutton(marcoBebidas,text="Baggio",font=Subtitle,onvalue=1,offvalue=0).grid(row=4, column=0, sticky=W)
Agua_saborizada = Checkbutton(marcoBebidas,text="Agua_saborizada",font=Subtitle,onvalue=1,offvalue=0).grid(row=5, column=0, sticky=W)
Agua = Checkbutton(marcoBebidas,text="Agua",font=Subtitle,onvalue=1,offvalue=0).grid(row=6, column=0, sticky=W)
Soda = Checkbutton(marcoBebidas,text="Soda",font=Subtitle,onvalue=1,offvalue=0).grid(row=7, column=0, sticky=W)
#cajas de texto para cada comida
textPepsi=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=0,column=1)
textCocacola=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=1,column=1)
textSevenUp=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=2,column=1)
textFanta=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=3,column=1)
textBaggio=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=4,column=1)
textagua_saborizada=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=5,column=1)
textAgua=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=6,column=1)
textSoda=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED).grid(row=7,column=1)#
# Se puede agregar otra fila igual solo hay que poner el marco correspondiente y  añadirle el nombre de variables y nombre

# etiquetas de totales y entradas para los valores.
costoComida=Label(marcoCosto, text="Total comida", font=Subtitle, bd=10, bg="Green", fg="white").grid(row=0,column=0)
casillaCostoComida=Entry(marcoCosto,font=Subtitle,bd=10, width=14,state="readonly").grid(row=0,column=1,padx=5)
costoBebida=Label(marcoCosto, text="Total Bebida", font=Subtitle, bd=10, bg="Green", fg="white").grid(row=1,column=0)
casillaCostoBebida=Entry(marcoCosto,font=Subtitle,bd=10, width=14,state="readonly").grid(row=1,column=1)

subtotal=Label(marcoCosto, text="Subtotal",font=Subtitle,bd=10,bg="Green",fg="white").grid(row=0,column=2)
casillasubtotal=Entry(marcoCosto, font=Subtitle, bd=10,width=14,state="readonly").grid(row=0, column=3,padx=41)
IVA= Label(marcoCosto, text="I.V.A",font=Subtitle,bd=10,bg="Green",fg="white").grid(row=1,column=2)
casillaIVA =Entry(marcoCosto, font=Subtitle, bd=10,width=14,state="readonly").grid(row=1, column=3)
TOTAL= Label(marcoCosto, text="TOTAL",font=Subtitle,bd=10,bg="Green",fg="white").grid(row=2,column=2)
casillaTotal =Entry(marcoCosto, font=Subtitle, bd=10,width=14,state="readonly").grid(row=2, column=3)


#calculadora de ayuda

pantallaCalculadora =Entry(marcoCalculadora,font=("arial",18,"bold"),width=33,bd=4).grid(row=0,column=0,columnspan=4)
boton7=Button(marcoCalculadora,text="7",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=1,column=0)
boton8=Button(marcoCalculadora,text="8",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=1,column=1)
boton9=Button(marcoCalculadora,text="9",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=1,column=2)
botonMas=Button(marcoCalculadora,text="+",font=Subtitle,fg="blue",bg="lightgray",bd=6,width=9).grid(row=1,column=3)

boton4=Button(marcoCalculadora,text="4",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=2,column=0)
boton5=Button(marcoCalculadora,text="5",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=2,column=1)
boton6=Button(marcoCalculadora,text="6",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=2,column=2)
botonMenos=Button(marcoCalculadora,text="-",font=Subtitle,fg="blue",bg="lightgray",bd=6,width=9).grid(row=2,column=3)

boton3=Button(marcoCalculadora,text="3",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=3,column=0)
boton2=Button(marcoCalculadora,text="2",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=3,column=1)
boton1=Button(marcoCalculadora,text="1",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=3,column=2)
botonMulti=Button(marcoCalculadora,text="*",font=Subtitle,fg="blue",bg="lightgray",bd=6,width=9).grid(row=3,column=3)

BotonIgual=Button(marcoCalculadora,text="=",font=Subtitle,fg="blue",bg="lightgray",bd=6,width=9).grid(row=4,column=0)
botonBorrar=Button(marcoCalculadora,text="C",font=Subtitle,fg="white",bg="red",bd=6,width=9).grid(row=4,column=1)
boton0=Button(marcoCalculadora,text="0",font=Subtitle,fg="white",bg="blue",bd=6,width=9).grid(row=4,column=2)
botonDivision=Button(marcoCalculadora,text="/",font=Subtitle,fg="blue",bg="lightgray",bd=6,width=9).grid(row=4,column=3)

#recibo
textRecibo=Text(marcoRecibo,font=("Arial",12,"bold"),bd=3,width=48,height=12).grid(row=0,column=0)
#botones
botonTotal=Button(marcoBotones,text="Total",font=Subtitle,fg="white",bg="blue",bd=4,padx=5).grid(row=0,column=0)
botonRecibo=Button(marcoBotones,text="Recibo",font=Subtitle,fg="white",bg="blue",bd=4,padx=5).grid(row=0,column=1)
botonGuardar=Button(marcoBotones,text="Guardar",font=Subtitle,fg="white",bg="blue",bd=4,padx=5).grid(row=0,column=2)
botonEnviar=Button(marcoBotones,text="Enviar",font=Subtitle,fg="white",bg="blue",bd=4,padx=5).grid(row=0,column=3)
botonBorrar=Button(marcoBotones,text="Borrar",font=Subtitle,fg="white",bg="blue",bd=4,padx=5).grid(row=0,column=4)
ventana.mainloop()
