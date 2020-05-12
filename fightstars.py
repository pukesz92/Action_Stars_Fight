from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk, Image
from pygame import mixer
import webbrowser

#Globális változók létrehozása és a képek átméretezése történik itt
harcos1_neve = None
harcos2_neve = None
harcos1_pontszam = None
harcos2_pontszam = None

mai_forma1_szamlalo = 0
mai_forma2_szamlalo = 0
new = 1
url = "https://github.com/pukesz92"

mixer.init() #initalizalja a mixert

playgomb = Image.open("play.png")
playgomb = playgomb.resize((250, 200), Image.ANTIALIAS)
playgomb.save("play.png", "png")

#Akcióhős osztály, init metódus=konstruktor segítségével példányosítás
class Akciohos:
    def __init__(self, nev, kor, pontszam):
        self.nev = nev
        self.kor = kor
        self.pontszam = pontszam

#a paraméterek a stringvar tartalmait kapják. (Valamelyik harcos neve)
def harc(a,b):

    #A gombra kattintva az insert mező tartalma törlődik és csak a legfrissebb információ látszik
    szovegide.delete('1.0', END)
    szovegide2.delete('1.0', END)
    szovegide3.delete('1.0', END)

    harcos1_neve = a.get()
    harcos2_neve = b.get()

    pluszero1 = random.randint(-5, 5)
    pluszero2 = random.randint(-5, 5)

    if harcos1_neve == "Jason Statham":
        harcos1_pontszam = Jason_Statham.pontszam
        mai_forma1 = harcos1_pontszam + pluszero1

        mai_forma1kiir = str(mai_forma1)
        harcos1_pontszamkiir=str(harcos1_pontszam)

        kiir = harcos1_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma1kiir
        szovegide.insert(0.0, kiir)
    elif harcos1_neve == "Arnold Schwarzenegger":
        harcos1_pontszam = Arnold_Schwarzenegger.pontszam
        mai_forma1 = harcos1_pontszam + pluszero1

        mai_forma1kiir = str(mai_forma1)
        harcos1_pontszamkiir = str(harcos1_pontszam)

        kiir = harcos1_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma1kiir
        szovegide.insert(0.0, kiir)
    elif harcos1_neve == "Wesley Snipes":
        harcos1_pontszam = Wesley_Snipes.pontszam
        mai_forma1 = harcos1_pontszam + pluszero1

        mai_forma1kiir = str(mai_forma1)
        harcos1_pontszamkiir = str(harcos1_pontszam)

        kiir = harcos1_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma1kiir
        szovegide.insert(0.0, kiir)


    if harcos2_neve == "Jason Statham":
        harcos2_pontszam = Jason_Statham.pontszam
        mai_forma2 = harcos2_pontszam + pluszero2

        mai_forma2kiir = str(mai_forma2)
        harcos2_pontszamkiir = str(Jason_Statham.pontszam)

        kiir = harcos2_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma2kiir
        szovegide2.insert(0.0, kiir)
    elif harcos2_neve == "Arnold Schwarzenegger":
        harcos2_pontszam = Arnold_Schwarzenegger.pontszam
        mai_forma2 = harcos2_pontszam + pluszero2

        mai_forma2kiir = str(mai_forma2)
        harcos2_pontszamkiir = str(Arnold_Schwarzenegger.pontszam)

        kiir = harcos2_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma2kiir
        szovegide2.insert(0.0, kiir)
    elif harcos2_neve == "Wesley Snipes":
        harcos2_pontszam = Wesley_Snipes.pontszam
        mai_forma2 = harcos2_pontszam + pluszero2

        mai_forma2kiir = str(mai_forma2)
        harcos2_pontszamkiir = str(Wesley_Snipes.pontszam)

        kiir = harcos2_neve + " a mai harc során a pontozók döntése alapján ennyi pontott szerzett: " + mai_forma2kiir
        szovegide2.insert(0.0, kiir)

    if mai_forma1 > mai_forma2:
        gyoztes = "A győztes a piros sarokból: " + harcos1_neve
        szovegide3.insert(0.0, gyoztes)
    elif mai_forma1 == mai_forma2:
        dontetlen = "A csata döntetlen lett"
        szovegide3.insert(0.0, dontetlen)
    else:
        gyoztes = "A győztes a kék sarokból: " + harcos2_neve
        szovegide3.insert(0.0, gyoztes)

def zene_gomb():
    mixer.music.load("disco.mp3")
    mixer.music.play()

#Példányok (harcosok)
Jason_Statham = Akciohos("Jason Statham", 52, 95)
Arnold_Schwarzenegger = Akciohos("Arnold Schwarzenegger", 72, 98)
Wesley_Snipes = Akciohos("Wesley Snipes", 57, 92)

#Az ablak
ablak = Tk()
ablak.title("Action Stars Fight 1.0")
ablak.iconbitmap('c:/Users/Puki István/PycharmProjects/Action_Stars_Fight/harc.ico')
ablak.geometry("1020x640")
ablak.config(bg="LightGray")

#A framek

def raise_frame(frame):
    frame.tkraise()

f1 = Frame(ablak)
f2 = Frame(ablak, width=1020, height=640)
f3 = Frame(ablak)
f4 = Frame(ablak)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

#A menüsor létrehozása

menubar = Menu(ablak)
ablak.config(menu=menubar)

#Almenü

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fájl", menu=subMenu)
subMenu.add_command(label="Kilépés", command=lambda: ablak.destroy())

subMenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Információk", menu=subMenu2)
subMenu2.add_command(label="Kapcsolat", command=lambda: kapcs_ablak())

subMenu2.add_command(label="Játék", command=lambda: vissza())

#A piros sarokban label és legördülő menü
Label(f1, text="A piros sarokban:", background="red", font="Helvetica 12 bold", fg="white").grid(row=0, column=0)
harcos_a = StringVar(f1)
harcos_a.set("Válasz ki a harcosod")
harcos1 = OptionMenu(f1, harcos_a, Jason_Statham.nev, Arnold_Schwarzenegger.nev, Wesley_Snipes.nev)
harcos1.grid(row=0, column=1, padx=5, pady=5)

#A kék sarokban label és legördülő menü
Label(f1, text="A kék sarokban:", background="blue", font="Helvetica 12 bold", fg="white").grid(row=1, column=0)
harcos_b = StringVar(f1)
harcos_b.set("Válasz ki a harcosod")
harcos2 = OptionMenu(f1, harcos_b, Jason_Statham.nev, Arnold_Schwarzenegger.nev, Wesley_Snipes.nev)
harcos2.grid(row=1, column=1, padx=5, pady=5)

#Táblázat
cols = ("Név", "Kor", "Alap pontszám")
table = ttk.Treeview(f1, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
table.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
table.insert("", "end", values=(Jason_Statham.nev, Jason_Statham.kor, Jason_Statham.pontszam))
table.insert("", "end", values=(Arnold_Schwarzenegger.nev, Arnold_Schwarzenegger.kor, Arnold_Schwarzenegger.pontszam))
table.insert("", "end", values=(Wesley_Snipes.nev, Wesley_Snipes.kor, Wesley_Snipes.pontszam))

#Text mezők létrehozása, szöveg kiiratása a függvényben
szovegide = Text(f1, width=45, height=3, wrap=WORD)
szovegide.grid(row=0, column=3, padx=5, pady=5)
szovegide2 = Text(f1, width=45, height=3, wrap=WORD)
szovegide2.grid(row=1, column=3, padx=5, pady=5)
szovegide3 = Text(f1, width=45, height=3, wrap=WORD)
szovegide3.grid(row=2, column=3, padx=5, pady=5)

#Induljon a harc gomb
gomb = Button(f1, text="Induljon a harc!", command=lambda: harc(harcos_a, harcos_b), font="Helvetica 12 bold").grid(row=2, columnspan=2, padx=10, pady=10)

#Zene gomb és a kép betöltése a gombon
photo2 = PhotoImage(file='play.png')
zene = Button(f1, image=photo2, command=lambda: zene_gomb())
zene.grid(row=3, column=3)

#f2
def openweb():
    webbrowser.open(url, new=new)

def kapcs_ablak():
    raise_frame(f2)

    frame1 = Frame(f2, width=1020, height=210, background="Cyan")
    frame1.grid(row=0, column=0)

    frame2 = Frame(f2, width=1020, height=210, background="LightGray")
    frame2.grid(row=1, column=0)

    frame3 = Frame(f2, width=1020, height=104, background="Cyan")
    frame3.grid(row=2, column=0)

    frame3 = Frame(f2, width=1020, height=104, background="LightGray")
    frame3.grid(row=3, column=0)

    Label(f2, text="Action Stars Fight 1.0 Készítette: Puki István", font="Helvetica 30 bold",  background="cyan", fg="gray").grid(row=0, column=0)
    Label(f2, text="E-mail: pukinho92@gmail.com", font="Helvetica 30 bold", background="Gray", fg="cyan").grid(row=1, column=0)

    Gomb_link = Button(f2, text="GitHub", width=50, background="white", command=lambda: openweb()).grid(row=2, column=0)
    Gomb_jatek = Button(f2, text="Vissza a játékhoz", width=50, background="white", command=lambda: vissza()).grid(row=3, column=0)

def vissza():
    raise_frame(f1)

raise_frame(f1)
ablak.mainloop()
