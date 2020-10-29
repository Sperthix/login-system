import sys
from tkinter import *
from tkinter import messagebox


def prihlasenie():
    uspech = False
    druhypokus = False
    f = open("login.txt", "r")
    meno = vstup_meno.get() + "\n"
    heslo = vstup_heslo.get() + "\n"
    for x in f:
        if x == meno:
            y = f.readline()
            if y == heslo:
                kontrola.showinfo("Login system", "Prihlásenie bolo úspešné.")
                uspech = True
                break
            else:
                odpoved = kontrola.askyesno("Login system", "Nesprávne heslo, chcete zopakovat prihlasenie?")
                if odpoved == 1:
                    druhypokus = True
                    break
                else:
                    menu()
                break
    f.close()
    if uspech:
        menu()
    elif druhypokus:
        prihlasenie_gui()
    else:
        kontrola.showerror("Login system", "Prihlasenie nebolo uspesne, navrat do hlavneho menu")
        menu()


def prihlasenie_gui():
    tlacidlo_login.grid_forget()
    tlacidlo_spat.grid_forget()
    label_info.grid_forget()

    vstup_meno.delete(0, END)
    vstup_heslo.delete(0, END)

    vstup_meno.config(text="")
    vstup_heslo.config(text="")

    label_info.config(text="Pre prihlásenie prosím zadajte Vaše meno a heslo.")
    label_meno.config(text="Meno: ")
    label_heslo.config(text="Heslo: ")

    tlacidlo_login.config(text="Login", command=prihlasenie)
    tlacidlo_spat.config(text="Spat", command=menu)

    label_info.grid(row=3, columnspan=2)
    label_meno.grid(row=0, column=0, sticky=E)
    label_heslo.grid(row=1, column=0, sticky=E)
    vstup_meno.grid(row=0, column=1)
    vstup_heslo.grid(row=1, column=1)
    tlacidlo_login.grid(row=2, column=1, pady=10)
    tlacidlo_spat.grid(row=2, column=0)


def registracia():
    meno = vstup_meno.get() + "\n"
    heslo = vstup_heslo.get() + "\n"

    #sken textaku pre duplicitu
    f = open("login.txt", "r")
    uz_regnute = False
    for x in f:
        y = f.readline()
        y = f.readline()
        if x == meno:
            uz_regnute = True
            f.close()
            kontrola.showinfo("Login system", "Vytvorena nova registracia.")
            break
    if not uz_regnute:
        # pridanie noveho loginu na koniec textaku
        f = open("login.txt", "a")
        f.writelines(meno)
        f.writelines(heslo)
        f.writelines("\n")
        f.close()
        menu()
    else:
        kontrola.showerror("Login system", "Pouzivatelske meno sa uz pouziva, prosim zvolte ine.")
        registracia_gui()


def registracia_gui():
    tlacidlo_login.grid_forget()
    tlacidlo_spat.grid_forget()
    label_info.grid_forget()

    vstup_meno.delete(0, END)
    vstup_heslo.delete(0, END)

    label_info.config(text="Vytvorenie noveho uctu:")
    label_meno.config(text="Zadajte uzivatelske meno: ")
    label_heslo.config(text="Zadajte heslo: ")

    tlacidlo_login.config(text="Registruj", command=registracia)
    tlacidlo_spat.config(text="Spat", command=menu)

    label_info.grid(row=0, columnspan=2)
    label_meno.grid(row=1, column=0, sticky=E)
    label_heslo.grid(row=2, column=0, sticky=E)
    vstup_meno.grid(row=1, column=1)
    vstup_heslo.grid(row=2, column=1)
    tlacidlo_login.grid(row=3, column=1, pady=10)
    tlacidlo_spat.grid(row=3, column=0)


def menu():
    label_info.grid_forget()
    label_meno.grid_forget()
    label_heslo.grid_forget()
    vstup_meno.grid_forget()
    vstup_heslo.grid_forget()
    tlacidlo_login.grid_forget()
    tlacidlo_spat.grid_forget()

    label_info.config(text="Vitajte v prihlasovacom systeme!")
    tlacidlo_login.config(text="Prihlasenie", command=prihlasenie_gui)
    tlacidlo_spat.config(text="Registracia", command=registracia_gui)

    label_info.grid(row=0, columnspan=2, column=0)
    tlacidlo_login.grid(row=1, column=0)
    tlacidlo_spat.grid(row=1, column=1, pady=20)


login = Tk()

label_info = Label(login)
label_meno = Label(login)
label_heslo = Label(login)
kontrola = messagebox

vstup_meno = Entry(login)
vstup_heslo = Entry(login)

tlacidlo_login = Button(login)
tlacidlo_spat = Button(login)

menu()
login.mainloop()