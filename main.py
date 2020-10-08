




def prihlasenie():
    print("Zvolilo sa prihlasenie")
    return

def registracia():
    print("Zvolila sa registracia")
    return


def pridaj_zaznam():
    return


def prejdi_zoznam():
    return

def menu():
    i = input("Chcete sa prihlasit (1), vytvorit ucet? (2), alebo ukoncit program? (0)")
    if int(i) == 1:
        prihlasenie()
    elif int(i) == 2:
        registracia()
    elif int(i) == 0:
        return
    else:
        print("nesprávny vstup")
        menu()

menu()





#f = open("login.txt", "r+")
#text = f.read("login.txt")
#f.close()