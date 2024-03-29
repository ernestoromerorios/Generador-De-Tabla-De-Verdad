from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import numpy as np

def tabla(*args):
	global lab,main_frame
	lab.destroy()
	main_frame.destroy()
	variables = []
	func = inp.get()
	if len(func) == 0:
		
		messagebox.showerror(message="¡Campo De Texto Vacío!\nPor favor ingrese al menos una variable.",title="Error")

	else:

		for i in func:
			if (i.upper()).isalpha() and (not(i.upper() in variables)):
				variables.append(i.upper()) 

		if len(variables) > 10:

			messagebox.showwarning(message="¡Muchas Variables!\nPor favor ingrese sólo hasta diez variables.",title="Advertencia")
		
		else:

			variables = sorted(variables) 

			dicc = {
			'True':'1',
			'False':'0',
			True:'1',
			False:'0',
			'1':'1',
			'0':'0',
			}

			main_frame = Frame(root) #Pone una nueva Frame para poder utilizar muchos datos y bajar con la barra hacía todos ellos
			main_frame.pack(fill=BOTH, expand=1)

			# Crea una Canva
			my_canvas = Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

			# Añade la barra a canva
			my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			# Configura la camba
			my_canvas.configure(yscrollcommand=my_scrollbar.set,bg='#CCC')
			my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

			# Crea otra Frame dentro de canva
			second_frame = Frame(my_canvas,bg='#CCC')

			# Añade la nueva Frame a la ventana de canva
			my_canvas.create_window((0,0), window=second_frame, anchor="nw")
			
			text = '\t'

			lab = Label(second_frame,text=f"Función:   {transformacion(func).upper()}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
			lab.pack(pady=5)

			for i in range (len(variables)):
				text += variables[i] + '\t'
			
			text += "Resultado"
			
			lab = Label(second_frame,text=f"{text}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
			lab.pack(pady=5)

			for j in range (2**len(variables)):
				
				aux = str(bin(j))
				text = ''
				binary = ''
				b = False
				for i in aux:
								
					if b:
						text += str(i) + '\t'
						binary += str(i)

					if i == 'b':
						b = True

				aux = str(aux)
				aux = ''

				while (len(aux)+(len(text)) != (len(variables)*2)):
					
					aux += '0' + '\t'
					binary = '0' + binary

				res = ''
				num = 0
				text = aux + text
				expr = func

				for i in range(len(expr)):

					if expr[i].isalpha():
						num = variables.index(expr[i].upper())
						res += binary[num]
					else:
						res += expr[i]
					if num == len(variables):
						num = 0

				num = 0
				expr = transformacion(res)
				#print(res)
				#print(func) a+b
				#print(res) 0+0

				try:
					#print(res)
					res = str(dicc[eval(expr)])
					text += res

					lab = Label(second_frame,text=f"{text}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
					lab.pack(pady=5)
				
				except:
				
					messagebox.showerror(message="¡Error en la escritura de la función!\nPor favor ingrese al apartado de ayuda para más información.",title="Error De Sintaxis")
					break

def ayuda():
	
	top = Toplevel() 
	top.configure(background='#333333') 
	top.title('Ayuda') 
	top.geometry('800x500') 
	btn2.config(state='disable') 
	
	l = Label(top,text="Generador De Tabla De Verdad ",fg='#FFF',bg='#333333',font=('Garamond bold', 15, 'bold italic'))
	l.place(x=250,y=30)

	l = Label(top,text="El programa puede calcular una tabla de verdad de hasta 10 variables.",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=150,y=100)

	l = Label(top,text="Debe recordar que un parentesis de más o un operador sin variable pueden generar errores.",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=60,y=125)

	l = Label(top,text="A continuación se muestran algunos los ejemplos de cómo se ingresan las funciones booleanas:",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=50,y=150)

	l = Label(top,text="Operador AND   ─>   . ó *  ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=220)

	l = Label(top,text="Operador OR   ─>   + ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=270)

	l = Label(top,text="Operador NOT   ─>   ~ ó '  ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=320)

	l = Label(top,text="Operador XOR   ─>   ^   ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=370)

	l = Label(top,text="Ejemplo: (~a+b)*(a+b+c) ó ('a+b).(a+b+c) ",fg='#FFF',bg='#333333',font=('Garamond bold', 14, 'bold'))
	l.place(x=250,y=420)

	def on_close():  
		top.destroy() 
		btn2.config(state='normal')  

	top.protocol("WM_DELETE_WINDOW", on_close)				


def transformacion(funcion):
	aux = ''
	for i in funcion:
		if i.isnumeric():
			aux += i
		elif i == "*" or i == ".":
			aux += " and "
		elif i == "+":
			aux += " or "
		elif i == "~" or i == "'":
			aux += " not "
		else:
			aux += i

	return aux
				

root = Tk()
root.title('\tGenerador Tabla De Verdad')
root.configure(background='#CCC') 
root.geometry('550x550')

lab = Label(root)
main_frame = Frame(root)

inp = StringVar()
inpt = Entry(textvar=inp,width=35)
inpt.pack(pady=5)

btn = Button(root,text='Enviar',fg='#000',bg='#FF9D00',font=('Helvetica', 10, 'bold'),command=tabla)
btn.pack(pady=5)

btn2 = Button(root,text='Ayuda',fg='#000',bg='#39CC68',font=('Helvetica', 10, 'bold'),command=ayuda)
btn2.pack(pady=5)

l = Label(root,text="Ernesto Romero Rios ®",fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
l.place(x=5,y=5)

inpt.focus()
root.bind("<Return>",tabla)

root.mainloop()

