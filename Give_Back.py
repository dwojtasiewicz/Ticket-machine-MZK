from interface import *
class Give_Back(Frame):
    def __init__(self, master, bc, text):
        """Inicjalizacja okno"""
        self.typ = text
        self.coins = bc
        super(Give_Back, self).__init__(master)
        self.grid()
        self.create_widgets(master)
        self.center()

    def create_widgets(self, X):
        """Tworzy widgety """
        topFrame = Frame(self)
        topFrame.pack(fill=Y)
        lowFrame = Frame(self)
        lowFrame.pack(side=BOTTOM,fill=Y)

        self.coins_list = Text(topFrame, width=25, height=20, bg="white")
        self.coins_list.pack()
        self.write_coins()


        self.key1 = Button(lowFrame, text="WEZ", height=3, width=28, background="red", command=lambda: self.back(X))
        self.key1.pack()

    def write_coins(self):
        """Wypełnienie listy monet"""
        lista = ""
        lista += self.typ + " :\n"
        for i in self.coins:
            lista += str(i) + "\n"

        self.coins_list.insert(0.0, lista)#wpisywanie do listy

    def back(self, X):
        """Ustal wartość pieniążka, zamyka okno"""
        X.quit()
        X.destroy()

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
