import sys
from tkinter import *


def prihlasenie():
    uspech = False
    f = open("login.txt", "r")
    meno = vstup_meno.get() + "\n"
    heslo = vstup_heslo.get() + "\n"
    for x in f:
        # print("Aktualny zaznam je: " + x)
        # print("Zadane meno je: " + meno)
        if x == meno:
            # print("rozpoznal som meno")
            y = f.readline()
            if y == heslo:
                label_info.config(text="Prihlásenie bolo úspešné.")
                uspech = True
                break
            else:
                label_info.config(text="Nesprávne heslo, zadajte prosím správne meno a heslo.")
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


def menu():
    i = input("Chcete sa prihlasit (1), vytvorit ucet? (2), alebo ukoncit program? (0)")
    if i.isdigit():
        if int(i) == 1:
            prihlasenie()
        elif int(i) == 2:
            registracia()
        elif int(i) == 0:
            sys.exit()
        else:
            print("nesprávny vstup")
            menu()
    else:
        print("Zadaj cislo")
        menu()


login = Tk()

label_info = Label(login, text="Pre prihlásenie prosím zadajte Vaše meno a heslo.")
label_meno = Label(login, text="Meno: ")
label_heslo = Label(login, text="Heslo: ")

vstup_meno = Entry(login)
vstup_heslo = Entry(login)

tlacidlo_login = Button(login, text="Login", command=prihlasenie)

label_info.grid(row=3, columnspan=2)
label_meno.grid(row=0, column=0, sticky=E)
label_heslo.grid(row=1, column=0, sticky=E)
vstup_meno.grid(row=0, column=1)
vstup_heslo.grid(row=1, column=1)
tlacidlo_login.grid(row=2, columnspan=2)


login.mainloop()
menu()

