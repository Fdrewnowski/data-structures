from tkinter import *
import tkinter as t
import World


class GuiWorld(t.Frame):

    world = World
    gui = []
    ch = 4

    def set_image(self, other):
        x = other.get_x()
        y = other.get_y()
        sign = other.get_sign()
        if sign == 'H':
            t.Label(self.leftframe, image=self.humanImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'G':
            t.Label(self.leftframe, image=self.grassImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'g':
            t.Label(self.leftframe, image=self.guaranaImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'h':
            t.Label(self.leftframe, image=self.hogweedImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'T':
            t.Label(self.leftframe, image=self.turtleImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'F':
            t.Label(self.leftframe, image=self.foxImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'S':
            t.Label(self.leftframe, image=self.sheepImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 's':
            t.Label(self.leftframe, image=self.sow_thistleImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'A':
            t.Label(self.leftframe, image=self.antelopeImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'd':
            t.Label(self.leftframe, image=self.deadlyImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'W':
            t.Label(self.leftframe, image=self.wolfImg, borderwidth=0).grid(row=x, column=y)
        elif sign == 'C':
            t.Label(self.leftframe, image=self.cyberImg, borderwidth=0).grid(row=x, column=y)

    def load(self):
        print("load world")
        for r in range(15):
            self.gui.append([])
            for c in range(15):
                self.gui.append(t.Label(self.leftframe, image=self.null, borderwidth=0).grid(row=r, column=c))
        self.world.load()
        self.world.draw()

    def save(self):
        print("save the world")
        self.world.save()

    def superpower(self):
        H = self.world.get_human()
        if H is not None and H.get_super_power() == 0:
            H.set_super_power(10)
            print("Superpower activated!")
        else:
            log = "To early to use!" + '\n'
            self.world.add_log(log)
            print("To early to use!")

    def next_turn(self):
        self.gui.clear()
        self.world.log=""
        for r in range(15):
            self.gui.append([])
            for c in range(15):
                self.gui.append(t.Label(self.leftframe, image=self.null, borderwidth=0).grid(row=r, column=c))

        self.clear_log()
        log="Turn:"+str(self.world.get_turn())+ '\n'
        self.world.add_log(log)
        self.world.action(self.ch)
        self.add_log(self.world.log)
        self.ch = 4

    def __init__(self):
        self.world = World.World(self)
        root = Tk()

        self.root = root
        t.Frame.__init__(self, root)
        root.title("Filip Drewnowski 171689")
        root.resizable(width="FALSE", height="FALSE")
        root.geometry('880x480')

        self.gui = []
        self.null = PhotoImage(file="pic/null5.gif")
        self.grassImg = PhotoImage(file="pic/grass.gif")
        self.antelopeImg = PhotoImage(file="pic/antelope.gif")
        self.deadlyImg = PhotoImage(file="pic/deadly_nightshade.gif")
        self.foxImg = PhotoImage(file="pic/fox.gif")
        self.guaranaImg = PhotoImage(file="pic/guarana.gif")
        self.hogweedImg = PhotoImage(file="pic/hogweed.gif")
        self.humanImg = PhotoImage(file="pic/human.gif")
        self.sheepImg = PhotoImage(file="pic/sheep.gif")
        self.sow_thistleImg = PhotoImage(file="pic/sow_thistle.gif")
        self.turtleImg = PhotoImage(file="pic/turtle.gif")
        self.wolfImg = PhotoImage(file="pic/wolf.gif")
        self.cyberImg = PhotoImage(file="pic/android.gif")

        self.leftframe = t.Frame()
        self.leftframe.pack(side=LEFT)
        for r in range(15):
            self.gui.append([])
            for c in range(15):
                self.gui.append(t.Label(self.leftframe, image=self.null, borderwidth=0).grid(row=r, column=c))

        self.rightframe = t.Frame()
        self.log = t.Text(self.rightframe, height=50, width=100)
        self.log.pack()
        self.rightframe.pack(side=LEFT)

        root.bind('<Left>', self.left_key)
        root.bind('<Right>', self.right_key)
        root.bind('<Up>', self.up_key)
        root.bind('<Down>', self.down_key)
        root.bind('<n>', self.n_key)
        root.bind('<s>', self.s_key)

        self.menubar = t.Menu(self)
        self.opcje = t.Menu(self, self.menubar, tearoff=0)
        self.opcje.add_command(label="Save", command=self.save)
        self.opcje.add_command(label="Load", command=self.load)
        self.menubar.add_cascade(label="Load or Save", menu=self.opcje)
        root.config(menu=self.menubar)
        self.superpow = t.Menu(self, self.menubar, tearoff=0)
        self.superpow.add_command(label="Superpower", command=self.superpower)
        self.menubar.add_cascade(label="Superpower", menu=self.superpow)
        root.config(menu=self.menubar)
        self.next_t = t.Menu(self, self.menubar, tearoff=0)
        self.next_t.add_command(label="Next turn", command=self.next_turn)
        self.menubar.add_cascade(label="Next turn", menu=self.next_t)
        root.config(menu=self.menubar)

        root.mainloop()

    def left_key(self, event):
        self.ch = 1
        self.next_turn()

    def right_key(self, event):
        self.ch = 0
        self.next_turn()

    def up_key(self, event):
        self.ch = 3
        self.next_turn()

    def down_key(self, event):
        self.ch = 2
        self.next_turn()

    def n_key(self, event):
        self.ch = 4
        self.next_turn()

    def s_key(self, event):
        self.superpower()

    def clear_log(self):
        self.log.config(state="normal")
        self.log.delete("1.0", t.END)
        self.log.config(state="disable")

    def add_log(self, comment):
        self.log.config(state="normal")
        self.log.insert(t.END, comment+"\n")
        self.log.config(state="disable")

















