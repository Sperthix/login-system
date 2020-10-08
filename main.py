

def prihlasenie():
    uspech = False
    f = open("login.txt", "r")
    meno = input("Zadajte prihlasovacie meno: ")
    meno = meno + "\n"
    heslo = input("Zadajte heslo: ")
    heslo = heslo + "\n"
    for x in f:
        # print("Aktualny zaznam je: " + x)
        # print("Zadane meno je: " + meno)
        if x == meno:
            # print("rozpoznal som meno")
            y = f.readline()
            if y == heslo:
                print("Prihlasenie bolo uspesne")
                uspech = True
                break
                return
            else:
                print("Nespravne heslo")
                prihlasenie()
    if not uspech:
        print("Prihlasenie nebolo uspesne, navrat do hlavneho menu")
        menu()
    f.close()
    menu()


def registracia():
    print("Vytvorenie noveho prihlasovacieho konta")
    meno = input("Zadajte prihlasovacie meno: ")
    heslo = input("Zadajte heslo: ")
    f = open("login.txt", "a")
    f.writelines(meno + "\n")
    f.writelines(heslo + "\n")
    f.writelines("\n")
    f.close()
    print("Zaznam bol uspesne pridany")
    menu()


def vypis_zoznamu():
    return


def menu():
    i = input("Chcete sa prihlasit (1), vytvorit ucet? (2), alebo ukoncit program? (0)")
    if i.isdigit():
        if int(i) == 1:
            prihlasenie()
        elif int(i) == 2:
            registracia()
        elif int(i) == 0:
            return
        else:
            print("nesprávny vstup")
            menu()
    else:
        print("Zadaj cislo")
        menu()


menu()
