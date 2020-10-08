




def prihlasenie():
    print("Zvolilo sa prihlasenie")
    f = open("login.txt", "r+")
    meno = input("Zadajte prihlasovacie meno: ")
    heslo = input("Zadajte heslo: ")
    for x in f:
        if x == meno:
            return
    f.close()
    return

def registracia():
    print("Vytvorenie noveho prihlasovacieho konta")
    meno = input("Zadajte prihlasovacie meno: ")
    heslo = input("Zadajte heslo: ")
    f = open("login.txt", "w")
    f.writelines(meno + "\n")
    f.writelines(heslo + "\n")
    f.close()
    print("Zaznam bol uspesne pridany")
    menu()

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