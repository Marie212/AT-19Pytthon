import random
def contras(): 
    letter = "abcdefghijklmnopqrstuvwxyz"
    mayusc = letter.upper()
    number = "0123456789"

    passw1= random.choice(letter)
    passw2= random.choice(mayusc)
    passw3= random.choice(number)
    passw4 = passw1 + passw2+ passw3
    passw6 = ""
    passw = letter + mayusc + number
    limit = random.randint(6, 13)

    for i in range(0, limit):
        passw5= random.choice(passw)
        passw6 = passw6 + passw5  
    codigo = passw6 + passw4
    return codigo

#while True:
def menus():
    print("MENU\n1. Generar codigo\n2. obtener codigo\n3. salir")
    opc = input("Ingrese una opcion: ")
    return opc
while True:
    cuentas = []
    opcion = menus()
    while opcion == "1":
        cuenta = input("ingrese la cuenta para la cual quiere generar codigo: ")
        x = cuenta
        y = contras()
        dic = {
            'cuen': x,
            'contras': y
        }
        #x = cuenta
        #y = contras()
        cuentas.append({'cuent': x, 'contras': y})
        print(cuentas)
        #print("la contraseña fue generada con exito, elija otra opcion")
        resp = input("la contraseña fue generada con exito, quiere generar otra contraseña?:\n 1. si\n 2. No\n")
        if resp == "2":
            menus()
        #print("MENU\n1. Generar codigo\n2. obtener codigo\n3. salir")
        #opcion = input("Ingrese una opcion: ")
        opcion2 = menus()
        while opcion2 == "2":
            print(cuentas)
            for c in cuentas:
                buscar = input("ingrese la cuenta de la cual quiere ver la contraseña: ")
                #print ("password: ", cuentas.get(buscar, "no entramos la cuenta"))
                if buscar == c['cuent']:
                    print('tu password de ' + buscar + ' es: ', c['contras'])
                    resp2 = input("quiere ver otra contraseña?:\n 1. si\n 2. No\n")
                if resp2 == "2":
                    menus()
                #opcion3 = menu ()
    if opcion == "3":
        break