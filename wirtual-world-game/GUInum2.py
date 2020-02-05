import tkinter as t
from Swiat import Swiat
from Czlowiek import Czlowiek
from Antylopa import Antylopa
from Barszczyk import Barszczyk
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from Wilcza_jagoda import Wilcza_jagoda
from Wilk import Wilk
from Zolw import Zolw
from Cyberowca import Cyberowca


class Example(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)
        root.title("Filip Drewnowski")
        root.resizable(width="FALSE", height="FALSE")
        root.geometry('600x800')
        self.przycisk = t.Button(self, text="Nowa tura", command=self.wykonajTure)
        self.komentarze = t.Text(self)
        self.s = t.Scrollbar(self)
        self.s.config(command=self.komentarze.yview)

        root.bind('<Left>', self.left_key)
        root.bind('<Right>', self.right_key)
        root.bind('<Up>', self.up_key)
        root.bind('<Down>', self.down_key)
        root.bind('<n>', self.n_key)
        root.bind('<Button-1>', self.left_click)
        self.pola = []
        for i in range(20):
            self.pola.append([])
            for j in range(20):
                self.pola[i].append(t.Label(self, text="", bg="misty rose"))

        self.menubar = t.Menu(self)
        self.opcje = t.Menu(self, self.menubar, tearoff=0)
        self.opcje.add_command(label="Zapisz", command=self.zapiszGre)
        self.opcje.add_command(label="Wczytaj", command=self.wczytajGre)
        self.menubar.add_cascade(label="Zapisz/wczytaj", menu=self.opcje)
        root.config(menu=self.menubar)
        self.swiat = None
        self.zwierzak = None
        self.zwierzaki = t.Menu(self, self.menubar, tearoff=0)

        self.zwierzaki.add_command(label="Antylopa", command=self.set_antylopa)
        self.zwierzaki.add_command(label="Barszczyk", command=self.set_barszcz)
        self.zwierzaki.add_command(label="Cyberowca", command=self.set_cyberowca)
        self.zwierzaki.add_command(label="Guarana", command=self.set_guarana)
        self.zwierzaki.add_command(label="Lis", command=self.set_lis)
        self.zwierzaki.add_command(label="Mlecz", command=self.set_mlecz)
        self.zwierzaki.add_command(label="Owca", command=self.set_owca)
        self.zwierzaki.add_command(label="Trawa", command=self.set_trawa)
        self.zwierzaki.add_command(label="Wilcza jagoda", command=self.set_wilczajagoda)
        self.zwierzaki.add_command(label="Wilk", command=self.set_wilk)
        self.zwierzaki.add_command(label="Zolw", command=self.set_zolw)

        self.menubar.add_cascade(label="Zwierzaki", menu=self.zwierzaki)
        root.config(menu=self.menubar)

        for i in range(20):
            for j in range(20):
                self.pola[i][j].place(x=0 + 30 * j, y=50 + 30 * i, width=30, height=30)

        self.przycisk.place(x=0, y=0, height=50, width=600)
        self.s.place(x=580, y=650, height=150, width=20)
        self.komentarze.place(x=0, y=650, height=150, width=600)
        self.komentarze.config(yscrollcommand=self.s.set)
        self.komentarze.config(state="disabled")
        self.swiat = Swiat(self)
        self.czlowiek = self.swiat.getCzlowiek()

    def set_antylopa(self):
        self.zwierzak = Antylopa(-1, -1, self.swiat)

    def set_lis(self):
        self.zwierzak = Lis(-1, -1, self.swiat)

    def set_barszcz(self):
        self.zwierzak = Barszczyk(-1, -1, self.swiat)

    def set_owca(self):
        self.zwierzak = Owca(-1, -1, self.swiat)

    def set_cyberowca(self):
        self.zwierzak = Cyberowca(-1, -1, self.swiat)

    def set_wilk(self):
        self.zwierzak = Wilk(-1, -1, self.swiat)

    def set_zolw(self):
        self.zwierzak = Zolw(-1, -1, self.swiat)

    def set_trawa(self):
        self.zwierzak = Trawa(-1, -1, self.swiat)

    def set_wilczajagoda(self):
        self.zwierzak = Wilcza_jagoda(-1, -1, self.swiat)

    def set_guarana(self):
        self.zwierzak = Guarana(-1, -1, self.swiat)

    def set_mlecz(self):
        self.zwierzak = Mlecz(-1, -1, self.swiat)

    def setKolor(self, kolor, x, y):
        self.pola[y][x].config(bg=kolor)

    def wykonajTure(self):
        if not self.czlowiek.czyMojaKolej():
            self.swiat.wykonajTure()

    def zapiszGre(self):
        self.swiat.zapiszGre()

    def wczytajGre(self):
        self.swiat.wczytajGre()
        self.czlowiek = self.swiat.getCzlowiek()

    def dodajKomentarz(self, komentarz):
        self.komentarze.config(state="normal")
        self.komentarze.insert(t.END, komentarz + "\n")
        self.komentarze.config(state="disabled")

    def czyscKomenty(self):
        self.komentarze.config(state="normal")
        self.komentarze.delete('1.0', t.END)
        self.komentarze.config(state="disabled")

    def left_key(self, event):
        if self.czlowiek.czyMojaKolej():
            self.czlowiek.idzLEFT()
            self.swiat.dokonczTure()

    def right_key(self, event):
        if self.czlowiek.czyMojaKolej():
            self.czlowiek.idzRIGHT()
            self.swiat.dokonczTure()

    def up_key(self, event):
        if self.czlowiek.czyMojaKolej():
            self.czlowiek.idzUP()
            self.swiat.dokonczTure()

    def down_key(self, event):
        if self.czlowiek.czyMojaKolej():
            self.czlowiek.idzDOWN()
            self.swiat.dokonczTure()

    def n_key(self, event):
        if self.czlowiek.czyMojaKolej():
            self.czlowiek.setNiesmiertelnosc()
            self.swiat.dokonczTure()

    def left_click(self, event):
        if root.winfo_pointery() - root.winfo_rooty() < 50:
            return
        x = int(root.winfo_pointerx() - root.winfo_rootx())
        y = int(root.winfo_pointery() - root.winfo_rooty())
        x = int(x / 30)
        y = int((y - 50) / 30)
        if x >= 0 and x <= 19 and y <= 19 and y >= 0 and not self.swiat.czyPoleZajete(x, y):
            self.swiat.dodajOrganizm(self.zwierzak, x, y)
            self.swiat.rysowanie()


if __name__ == "__main__":
    root = t.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()