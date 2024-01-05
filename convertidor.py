from tkinter import *

raiz = Tk()

def winbintodec(): #BINARIO A DECIMAL
    raiz1 = Tk()
    raiz1.resizable(False,False)
    raiz1.geometry("400x400")
    width = 400 # Width 
    height = 300 # Height
    screen_width = raiz1.winfo_screenwidth()  # Width of the screen
    screen_height = raiz1.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    winbd = Frame(raiz1,width=300,height=300)
    titulo = Label(winbd, text="Binary to decimal\n", anchor="center",justify="center",font=("Times",15)) 
    titulo.grid(row=0, column=0)
    textonumero = Label(winbd, text="Insert your number: ") 
    textonumero.grid(row=1,column=0)
    cuadronumero = Entry(winbd, width=30)
    cuadronumero.grid(row=1,column=1)
    etiqueta = Label(raiz1)
    etiqueta.place(x=180,y=100)
    def BintoDec():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        string = cuadronumero.get()#se pide el numero
        list(string)
        result = 0
        #Aqui se va a guardar el NUMERO
        j = 0
        for i in string:#ciclo que recorre cada uno de los indices del arreglo
            if i == 1 or i == '1':#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                result = result + binary[j]#se agrega un 1, similar a un true
                j = j + 1
                # print("result:",result)
                # print("String:",string)
                # print("i:",i)
                # print("j:",j) 
            elif i == 0 or i == '0':
                
                result = result + 0#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
                j = j+1
        #imprimo el resultado del binario
        etiqueta["text"] = result
    btn = Button(raiz1, text="Convert", command=BintoDec,width=20)
    btn.place(x=130,y=150)
    winbd.pack()
    raiz1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    raiz1.mainloop()
    

def windectobin():# DECIMAL A BINARIO
    raiz2 = Tk()
    raiz2.resizable(False,False)
    raiz2.geometry("400x400")
    width = 400 # Width 
    height = 300 # Height
    screen_width = raiz2.winfo_screenwidth()  # Width of the screen
    screen_height = raiz2.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    windb = Frame(raiz2,width=300,height=300)
    titulo = Label(windb, text="Decimal to Binary\n", anchor="center",justify="center",font=("Times",15)) 
    titulo.grid(row=0, column=0)
    textonumero = Label(windb, text="Insert your number: ") 
    textonumero.grid(row=1,column=0)
    cuadronumero2 = Entry(windb, width=30)
    cuadronumero2.grid(row=1,column=1)
    etiqueta2 = Label(raiz2)
    etiqueta2.place(x=180,y=100)
    #FUNCION
    def DecToBin():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        n = int(float(cuadronumero2.get()))#se pide el numero
        result = ""#Aqui se va a guardar el binario

        for i in binary:#ciclo que recorre cada uno de los indices del arreglo
            if n > i or n == i:#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                n = n - i#se le resta el indice
                result = result + '1'#se agrega un 1, similar a un true
                # print('debug: '+result) /IGNORAR/
                # print(n)
                # print(i) 
            else:
                result = result + '0'#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        etiqueta2["text"] = result#imprimo el resultado del binario
    btn = Button(raiz2, text="Convert", command=DecToBin,width=20)
    btn.place(x=130,y=150)
    windb.pack()
    raiz2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    raiz2.mainloop()
    
def iptobin():# DECIMAL A BINARIO
    raiz3 = Tk()
    raiz3.resizable(False,False)
    raiz3.geometry("400x400")
    width = 600 # Width 
    height = 300 # Height
    screen_width = raiz3.winfo_screenwidth()  # Width of the screen
    screen_height = raiz3.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    winipb = Frame(raiz3,width=600,height=300)
    titulo = Label(winipb, text="Ip to Binary IP\n", anchor="center",justify="center",font=("Times",15)) 
    titulo.grid(row=0, column=0)
    textonumero = Label(winipb, text="Insert your number: ") 
    textonumero.grid(row=1,column=0)
    textonumero.place(x=0,y=30)
    octeto1 = Entry(winipb, width=10)
    octeto1.grid(row=2,column=0)
    punto1 = Label(winipb, text=" . ")
    punto1.grid(row=2, column=1)
    octeto2 = Entry(winipb, width=10)
    octeto2.grid(row=2,column=2)
    punto2 = Label(winipb, text=" . ")
    punto2.grid(row=2, column=3)
    octeto3 = Entry(winipb, width=10)
    octeto3.grid(row=2,column=4)
    punto3 = Label(winipb, text=" . ")
    punto3.grid(row=2, column=5)
    octeto4 = Entry(winipb, width=10)
    octeto4.grid(row=2,column=6)
    etiqueta2 = Label(raiz3)
    etiqueta2.place(x=180,y=100)
    def IpToBin1():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        n = int(float(octeto1.get()))#se pide el numero
        result = ""#Aqui se va a guardar el binario

        for i in binary:#ciclo que recorre cada uno de los indices del arreglo
            if n > i or n == i:#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                n = n - i#se le resta el indice
                result = result + '1'#se agrega un 1, similar a un true
                # print('debug: '+result) /IGNORAR/
                # print(n)
                # print(i) 
            else:
                result = result + '0'#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct1["text"] = result
        IpToBin2()
        IpToBin3()
        IpToBin4()
    def IpToBin2():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        n = int(float(octeto2.get()))#se pide el numero
        result = ""#Aqui se va a guardar el binario

        for i in binary:#ciclo que recorre cada uno de los indices del arreglo
            if n > i or n == i:#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                n = n - i#se le resta el indice
                result = result + '1'#se agrega un 1, similar a un true
                # print('debug: '+result) /IGNORAR/
                # print(n)
                # print(i) 
            else:
                result = result + '0'#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct2["text"] = result
    def IpToBin3():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        n = int(float(octeto3.get()))#se pide el numero
        result = ""#Aqui se va a guardar el binario

        for i in binary:#ciclo que recorre cada uno de los indices del arreglo
            if n > i or n == i:#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                n = n - i#se le resta el indice
                result = result + '1'#se agrega un 1, similar a un true
                # print('debug: '+result) /IGNORAR/
                # print(n)
                # print(i) 
            else:
                result = result + '0'#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct3["text"] = result
    def IpToBin4():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        n = int(float(octeto4.get()))#se pide el numero
        result = ""#Aqui se va a guardar el binario

        for i in binary:#ciclo que recorre cada uno de los indices del arreglo
            if n > i or n == i:#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                n = n - i#se le resta el indice
                result = result + '1'#se agrega un 1, similar a un true
                # print('debug: '+result) /IGNORAR/
                # print(n)
                # print(i) 
            else:
                result = result + '0'#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct4["text"] = result

    res_oct1 = Label(winipb)
    res_oct1.place(x=180,y=100)
    res_oct1.grid(row=3, column=0)
    res_oct2 = Label(winipb)
    res_oct2.place(x=220,y=100)
    res_oct2.grid(row=3, column=1)
    res_oct3 = Label(winipb)
    res_oct3.place(x=260,y=100)
    res_oct3.grid(row=3, column=2)
    res_oct4 = Label(winipb)
    res_oct4.place(x=300,y=100)
    res_oct4.grid(row=3, column=3)
    btn = Button(raiz3, text="Convert",width=20, command=IpToBin1)
    btn.place(x=130,y=150)

    winipb.pack()
    raiz3.geometry('%dx%d+%d+%d' % (width, height, x, y))
    raiz3.mainloop()

def BinIPtoIP():# DECIMAL A BINARIO
    raiz4 = Tk()
    raiz4.resizable(False,False)
    raiz4.geometry("400x400")
    width = 600 # Width 
    height = 300 # Height
    screen_width = raiz4.winfo_screenwidth()  # Width of the screen
    screen_height = raiz4.winfo_screenheight() # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    winbiptoip = Frame(raiz4,width=600,height=300)
    titulo = Label(winbiptoip, text="Binary IP to IP\n", anchor="center",justify="center",font=("Times",15)) 
    titulo.grid(row=0, column=0)
    textonumero = Label(winbiptoip, text="Insert your number: ") 
    textonumero.grid(row=1,column=0)
    textonumero.place(x=0,y=30)
    octeto1 = Entry(winbiptoip, width=10)
    octeto1.grid(row=2,column=0)
    punto1 = Label(winbiptoip, text=" . ")
    punto1.grid(row=2, column=1)
    octeto2 = Entry(winbiptoip, width=10)
    octeto2.grid(row=2,column=2)
    punto2 = Label(winbiptoip, text=" . ")
    punto2.grid(row=2, column=3)
    octeto3 = Entry(winbiptoip, width=10)
    octeto3.grid(row=2,column=4)
    punto3 = Label(winbiptoip, text=" . ")
    punto3.grid(row=2, column=5)
    octeto4 = Entry(winbiptoip, width=10)
    octeto4.grid(row=2,column=6)
    etiqueta2 = Label(raiz4)
    etiqueta2.place(x=180,y=100)
    def BINTOIP():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        string = octeto1.get()#se pide el numero
        list(string)
        result = 0
        #Aqui se va a guardar el NUMERO
        j = 0
        for i in string:#ciclo que recorre cada uno de los indices del arreglo
            if i == 1 or i == '1':#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                result = result + binary[j]#se agrega un 1, similar a un true
                j = j + 1
                # print("result:",result)
                # print("String:",string)
                # print("i:",i)
                # print("j:",j) 
            elif i == 0 or i == '0':
                
                result = result + 0#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
                j = j+1#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct1["text"] = result
        BINTOIP2()
        BINTOIP3()
        BINTOIP4()
    def BINTOIP2():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        string = octeto2.get()#se pide el numero
        list(string)
        result = 0
        #Aqui se va a guardar el NUMERO
        j = 0
        for i in string:#ciclo que recorre cada uno de los indices del arreglo
            if i == 1 or i == '1':#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                result = result + binary[j]#se agrega un 1, similar a un true
                j = j + 1
                # print("result:",result)
                # print("String:",string)
                # print("i:",i)
                # print("j:",j) 
            elif i == 0 or i == '0':
                
                result = result + 0#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
                j = j+1#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
        res_oct2["text"] = result
    def BINTOIP3():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        string = octeto3.get()#se pide el numero
        list(string)
        result = 0
        #Aqui se va a guardar el NUMERO
        j = 0
        for i in string:#ciclo que recorre cada uno de los indices del arreglo
            if i == 1 or i == '1':#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                result = result + binary[j]#se agrega un 1, similar a un true
                j = j + 1
                # print("result:",result)
                # print("String:",string)
                # print("i:",i)
                # print("j:",j) 
            elif i == 0 or i == '0':
                
                result = result + 0#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
                j = j+1
                res_oct3["text"] = result 
    def BINTOIP4():
        binary = [128,64,32,16,8,4,2,1]#Estos numeros van a restar al numero ingresado
        string = octeto4.get()#se pide el numero
        list(string)
        result = 0
        #Aqui se va a guardar el NUMERO
        j = 0
        for i in string:#ciclo que recorre cada uno de los indices del arreglo
            if i == 1 or i == '1':#si es menor o igual que el indice ejemplo 196 > que 128, entonces...
                result = result + binary[j]#se agrega un 1, similar a un true
                j = j + 1
                # print("result:",result)
                # print("String:",string)
                # print("i:",i)
                # print("j:",j) 
            elif i == 0 or i == '0':
                
                result = result + 0#Si no cabe o no se cumple la condicion se pone un false o 0 y se pasa al siguiente indice hasta los 8 
                j = j+1
        res_oct4["text"] = result

    res_oct1 = Label(winbiptoip)
    res_oct1.place(x=180,y=100)
    res_oct1.grid(row=3, column=0)
    res_oct2 = Label(winbiptoip)
    res_oct2.place(x=220,y=100)
    res_oct2.grid(row=3, column=1)
    res_oct3 = Label(winbiptoip)
    res_oct3.place(x=260,y=100)
    res_oct3.grid(row=3, column=2)
    res_oct4 = Label(winbiptoip)
    res_oct4.place(x=300,y=100)
    res_oct4.grid(row=3, column=3)
    btn = Button(raiz4, text="Convert",width=20, command=BINTOIP)
    btn.place(x=130,y=150)

    winbiptoip.pack()
    raiz4.geometry('%dx%d+%d+%d' % (width, height, x, y))
    raiz4.mainloop()

raiz.resizable(False,False)
raiz.geometry("400x400")
width = 400 # Width 
height = 400 # Height
screen_width = raiz.winfo_screenwidth()  # Width of the screen
screen_height = raiz.winfo_screenheight() # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 

menu = Frame(raiz, width=400,height=400)
conv = Label(menu, text="Binary convertor", anchor='center',font=("Times",20))
conv.grid(row=0, column=0 )
btn_bintodec = Button(raiz, text="Binary to Decimal",activeforeground="blue",font="Times",justify="center",width=20,command=winbintodec)
btn_bintodec.place(x=90,y=100)
btn_dectobin = Button(raiz, text="Decimal to Binary",activeforeground="blue",font="Times",justify="center",width=20,command=windectobin)
btn_dectobin.place(x=90,y=170)
btn_iptobin = Button(raiz, text="IP to Binary IP",activeforeground="blue",font="Times",justify="center",width=20,command=iptobin)
btn_iptobin.place(x=90,y=240)
btn_bintoip = Button(raiz, text="Binary IP to IP",activeforeground="blue",font="Times",justify="center",width=20,command=BinIPtoIP)
btn_bintoip.place(x=90,y=310)
menu.pack()
#raiz.eval('tk::PlaceWindow . center')#centers the window
raiz.geometry('%dx%d+%d+%d' % (width, height, x, y))

raiz.mainloop()



