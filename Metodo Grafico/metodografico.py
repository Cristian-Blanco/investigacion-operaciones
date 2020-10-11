import sympy as sym
from sympy import symbols, plot_implicit, And
from sympy.plotting import plot

#VARIABLES
x, y = symbols('x, y') #Declaramos las variables X,Y
diccionario = {} #Este diccionario lo utilizaremos para guardar los maximos o Minimos (Depende el caso)
lista = [] #La lista nos ayudara a organizar los maximos y minimos para los ejercicios 6 en adelante


#VARIABLES CON FUNCIONES
primer_ejercicio = y < (5-2*x)
segundo_ejercicio = y <= 5
tercer_ejercicio = 2*(2*x-y)<2*(x+y)-4 


#Funciones Para ejercicios de MAXIMOS Y MINIMOS
#Funcion del Ejercicio 6
def primerFuncionMaximos(x,y):
    p = 4*x+6*y     #Evaluamos los puntos en la funcion P(x,y)
    diccionario[p]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto
#Funcion del Ejercicio 7
def segundoFuncionMaximos(x,y):
    p = 6*x + 3*y   #Evaluamos los puntos en la funcion P(x,y)
    diccionario[p]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto
#Funcion del Ejercicio 8
def tercerFuncionMinimos(x,y):
    p = 9*x - y   #Evaluamos los puntos en la funcion P(x,y)
    diccionario[p]= (x,y) #Guardamos el resultado y los valores x,y
    text = "x: "+str(x)+" y: "+str(y) #realizamos un texto para el usuario
    return text #retornamos el texto


#Ejercicio de graficar Sistemas de Ecuaciones
print("EJERCICIO 1.\nGrafica y < 5-2x")
plot_implicit(primer_ejercicio, (x,-100,100), (y,-100,100))#Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 2.\nGrafica y <= 5")
plot_implicit(segundo_ejercicio, (x,-50,50), (y,-50,50))#Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 3.\nGrafica 2(2x-y)<2(x+y)-4")
plot_implicit(tercer_ejercicio, (x,-100,100), (y,-100,100)) #Obtenemos la region a estudiar plot_implicit(function,(range))

print("\n\nEJERCICIO 4.\nGrafica: \n  2x+y > 3\n  2y-1 > 0\n  x>=y")
plot_implicit(And(2*x+y > 3, 2*y - 1 > 0, x>=y), (x,-10,10), (y,-10,10))#Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))

print("\n\nEJERCICIO 5.\nGrafica: \n  2x+3y <= 60\n  x >= 0\n  y >= 0")
plot_implicit(And((2*x+3*y)<=60, x >= 0, y >= 0), (x,-40,40), (y,-40,40))#Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))



#MAXIMIZAR Y MINIMIZAR UNA FUNCION SUJETA A RESTRICCIONES
#EJERCICIO 6
print("\n\nEJERCICIO 6.\nMaximizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 4x + 6y\n     S.A : 2X+Y<=180\n           x+2y<=160\n           x+y<=100\n           x>=0\n           y>=0")
print("Primero Dibujamos las rectas de las Restricciones:\n   2x+y-180=0\n   x+2y-160=0\n   x+y-100=0\n   x=0\n   y=0")
plot(180-2*x,(160-x)/2,100-x,0,(x,-100,100)) #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")
plot_implicit(And(2*x+y<=180, x+2*y<=160, x+y <=100, x>=0, y>= 0),(x,-100,100), (y,-100,100)) #Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))
#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([2*x+y-180, x+y-100], dict=True)
inter_2 = sym.solve([x+2*y-160, x+y-100], dict=True)
inter_3 = sym.solve([2*x+y-180, y+0], dict=True)
inter_4 = sym.solve([x+0, y+0], dict=True)
inter_5 = sym.solve([x+2*y-160, x+0], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+primerFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+primerFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+primerFuncionMaximos(inter_3[0][x],inter_3[0][y])+"\n4:"+primerFuncionMaximos(inter_4[0][x],inter_4[0][y])+"\n5:"+primerFuncionMaximos(inter_5[0][x],inter_5[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[-1]]    #obtenemos la tupla del Maximo en el diccionario
print("El maximo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor maximo : "+str(lista[-1]))



#EJERCICIO 7 
# EJEMPLO CREADO "MAXIMIZAR LA FUNCION SUJETA A LAS RESTRICCIONES"
print("\n\nEJERCICIO 7.\nMaximizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 6x + 3y\n     S.A : x-3y<=7\n           3x+y<=14\n           y-x<=21")
print("Primero Dibujamos las rectas de las Restricciones:\n   x-3y-7=0\n   3x+y-14=0\n   y-x-21=0")
plot((7-x)/-3, 14-3*x, 21+x, (x,-50,50)) #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")
plot_implicit(And(x-3*y<=7, 3*x+y<=14, y-x<=21),(x,-50,50), (y,-50,50)) #Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))

diccionario={}
lista=[]
#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([x-3*y-7, 3*x+y-14], dict=True)
inter_2 = sym.solve([3*x+y-14, y-x-21], dict=True)
inter_3 = sym.solve([y-x-21, x-3*y-7], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+segundoFuncionMaximos(inter_1[0][x],inter_1[0][y])+"\n2:"+segundoFuncionMaximos(inter_2[0][x],inter_2[0][y])+"\n3:"+segundoFuncionMaximos(inter_3[0][x],inter_3[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[-1]]    #obtenemos la tupla del Maximo en el diccionario
print("El maximo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor maximo : "+str(lista[-1]))



#EJERCICIO 8 
# EJEMPLO CREADO "MINIMIZAR LA FUNCION SUJETA A LAS RESTRICCIONES"
print("\n\nEJERCICIO 8.\nMinimizar La Funcion sujeta a Las siguientes Restricciones:")
print("Max. P = 9*x - y\n     S.A : 3x+6y>=18\n           7x+3y>=10\n           x+y<=5")
print("Primero Dibujamos las rectas de las Restricciones:\n   3x+6y-18=0\n   7x+3y-10=0\n   x+y-5=0")
plot((18-3*x)/6, (10-7*x)/3, 5-x, (x,-10,10)) #Graficamos todas las rectas igualadas a Y plot(function,function,...,(range))
print("Ahora solo escojemos la zona de estudio que es la siguiente:\n")
plot_implicit(And(3*x+6*y>=18, 7*x+3*y>=10, x+y<=5),(x,-10,10), (y,-10,10)) #Obtenemos la region a estudiar plot_implicit(And(function,function,...),(range))

diccionario={}
lista=[]
#el sym.solve nos ayuda a resolver ecuaciones igualadas a 0
inter_1 = sym.solve([x+y-5, 7*x+3*y-10], dict=True)
inter_2 = sym.solve([3*x+6*y-18, x+y-5], dict=True)
inter_3 = sym.solve([3*x+6*y-18, 7*x+3*y-10], dict=True)
print("Los puntos extremos son los siguientes:\n")
print("1:"+tercerFuncionMinimos(inter_1[0][x],inter_1[0][y])+"\n2:"+tercerFuncionMinimos(inter_2[0][x],inter_2[0][y])+"\n3:"+tercerFuncionMinimos(inter_3[0][x],inter_3[0][y]))
for i in diccionario.keys(): #añadimos las llaves de los diccionarios a la lista
    lista.append(i)
lista.sort()    #organizamos la lista de menor a mayor
valores = diccionario[lista[0]]    #obtenemos la tupla del minimo en el diccionario
print("El minimo absoluto es el punto (x: "+str(valores[0])+" y: "+str(valores[1])+")\n ya que evaluados en la funcion P da como valor minimo : "+str(lista[0]))