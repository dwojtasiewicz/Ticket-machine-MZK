from tkinter import *
from Give_Back import *
from Throwing_coins import *
from Coins import *
from Ticket import *

class Maschine(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.ticket = []
        self.choose_ticket = []
        self.sum_coins = 0.0  # suma wrzuconych monet
        self.sum_ticket = 0.0  # suma za bilety

        self.text = ""  # tekst na screenie

        self.monety_wrzucane = []  # lista wrzuconych monet
        self.reszta = 0.0  # reszta
        self.monety_w_automacie = []  # lista obiektow monet
        self.suma_w_automacie = 0.0  # suma monet znajdujących się w automacie
        self.monety_reszta = []  # lista monet ktore zwraca

        self.buy_ticket = []

        self.inicjalize_coins()
        self.inicjalize_ticket()
        self.create_widgets()
        self.center()

    def create_widgets(self):

        self.parent.title("Automat biletowy MPK")
        self.pack(fill=X, expand=True)

        leftFrame=Frame(self)
        leftFrame.pack(side=LEFT,fill=Y)
        sideFrame=Frame(self)
        sideFrame.pack(side=RIGHT,fill=Y)

        # rodzaje biletow
        k_bilet1 = Button(leftFrame, text="Bilet normalny 20 min\n1,70zł", height=5, width=25, bg="#9F9FDF",overrelief=SUNKEN,command=lambda: self.keys_operation(0))
        k_bilet1.pack(fill=Y, anchor=N)

        k_bilet2 = Button(leftFrame, text="Bilet ulgowy 20 min\n1,40zł", height=5, width=25, bg="#9F9FDF",overrelief=SUNKEN,command=lambda: self.keys_operation(1))
        k_bilet2.pack(fill=Y, anchor=N)

        k_bilet3 = Button(leftFrame, text="Bilet normalny 40 min\n2,20zł", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN,command=lambda: self.keys_operation(2))
        k_bilet3.pack(fill=Y, anchor=N)

        k_bilet4 = Button(leftFrame, text="Bilet ulgowy 40 min\n1,70zł", height=5, width=25, bg="#9F9FDF",overrelief=SUNKEN,command=lambda: self.keys_operation(3))
        k_bilet4.pack(fill=Y, anchor=N)

        k_bilet5 = Button(leftFrame, text="Bilet normalny 60 min\n2,80zł", height=5, width=25, bg="#9F9FDF",overrelief=SUNKEN,command=lambda: self.keys_operation(4))
        k_bilet5.pack(fill=Y, anchor=N)

        k_bilet6 = Button(leftFrame, text="Bilet ulgowy 60 min\n2,40zł", height=5, width=25, bg="#9F9FDF",overrelief=SUNKEN, command=lambda: self.keys_operation(5))
        k_bilet6.pack(fill=Y, anchor=N)

        # Wyświetlacz
        self.screen = Text(sideFrame, width=25, height=10, wrap=WORD)
        self.screen.pack(fill=Y, anchor=N)
        self.screen.insert(0.0, "Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

        #wrzuc monety
        key_wrzuc = Button(sideFrame, text="Wrzuć monete",width=25, height=4,bg="#55A41C", overrelief=SUNKEN,command=self.throw_coins)
        key_wrzuc.pack(fill=Y, anchor=N)
        #zwroc monety
        key_oddaj = Button(sideFrame, text="Zwróć monety",width=25, height=4,bg="#C91F16", overrelief=SUNKEN,command=lambda: self.g_b_coins())
        key_oddaj.pack(fill=Y, anchor=N)
        #kup
        key_kup = Button(sideFrame, text="KUP", width=25, height=4, bg="white", overrelief=SUNKEN,command=lambda: self.keys_operation(11))
        key_kup.pack(fill=Y, anchor=N)
        #wez reszte
        key_oddaj = Button(sideFrame, text="Wez reszte", width=25, height=2, bg="#A7A7A7", overrelief=SUNKEN,command=lambda: self.take_coins())
        key_oddaj.pack(fill=Y, anchor=N)

        #autor
        autor=Label(sideFrame,text="Autor: \nDominika Wojtasiewicz",fg="red",pady=7)
        autor.pack(fill=Y, anchor=N)

        key_cofnij = Button(sideFrame, text="od nowa", width=25, height=2, bg="#A7A7A7", overrelief=SUNKEN,command=lambda: self.keys_operation(10))
        key_cofnij.pack(fill=Y, anchor=N)

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def inicjalize_coins(self):
        """Tworzenie monet"""
        nominal = [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
        ilosc = [3, 5, 4, 0, 12, 0, 14, 0, 4, 0, 55, 100]
       # ilosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.monety_w_automacie = [Coin(nom=nominal[x], il=ilosc[x]) for x in range(12)]  #wpisanie do listy stanu monet w automacie

    def inicjalize_ticket(self):
        """Tworzenie biletow"""
        nazwy = ["Normalny 20 min","Ulgowy 20 min","Normalny 40 min","Ulgowy 40 min","Normalny 60 min","Ulgowy 60 min"]
        cena = [1.70, 1.40, 2.20, 1.70, 2.80, 2.40]

        self.ticket = [Ticket(name=nazwy[x], prize=cena[x]) for x in range(6)]

    def throw_coins(self):
        """Mechanizm wrzucania monet"""
        pocket = Tk()
        pocket.title("Portfel")
        pckt = Throwing_coins(pocket) #??
        pocket.mainloop()

        moneta = pckt.get_coin()
        if moneta != 0.0:
            self.sum_coins += moneta
            self.sum_coins = round(self.sum_coins, 2) #zaokraglanie sumy monet
            self.monety_wrzucane.append(moneta)#dodanie na koniec listy zmiennej moneta
            # print(self.monety_wrzucane)
            self.write("Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

    def g_b_coins(self):
        """mechanizm wyrzucania monet"""  # !!!!!!!!!!!!!!!!!!!!
        self.monety_reszta = [x for x in self.monety_wrzucane]
        print("zwrócone :", self.monety_reszta)
        self.monety_wrzucane = []
        self.sum_coins = 0.0
        self.screen.delete(0.0, END)
        self.screen.insert(0.0, "Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))
        # test
       # print("zwrócone :", self.monety_reszta)
        # print("Monety wrzucone :", self.monety_wrzucane)

    def take_coins(self):
        """Odebranie reszty"""
        print("reszta :", self.monety_reszta)
        mach = Tk()
        mach.title("WEŹ RESZTĘ!")
        gbc = Give_Back(mach, self.monety_reszta, "Twoja reszta")
        mach.mainloop()
        self.monety_reszta = []
        self.text = ""
        self.sum_ticket =0.0
        self.write("Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

    def take_product(self):
        """Odebranie produktu"""
        prod = Tk()
        prod.title("WEŹ BILET/Y !!!")
        gbc = Give_Back(prod, self.buy_ticket, "Twoje bilety ")
        prod.mainloop()
        self.buy_ticket = []
        self.write("Nazwa:"+self.text + "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

    def write(self, text):
        """Wypisywanie komunikatów na screenie"""
        self.screen.delete(0.0, END)
        self.screen.insert(0.0, text)

    def rest(self, ticket):
        """Oblicza resztę"""
        # dodawanie wrzuconych monet do monet w maszynie
        for j in self.monety_wrzucane:
            for k in self.monety_w_automacie:
                if j == k.get_nominal():
                    k.inc()

        # oblicanie sumy w automacie
        for i in self.monety_w_automacie:
            self.suma_w_automacie += i.wartosc()
        self.suma_w_automacie = round(self.suma_w_automacie, 2)


        for obj in self.monety_w_automacie:
            print(obj)
            print("-------")

        if self.reszta < self.suma_w_automacie:
            # obliczanie reszty
            for l in self.monety_w_automacie:
                logic = True
                while logic:
                    if (round(self.reszta, 2) - l.get_nominal() >= 0) and (l.get_ilosc() > 0):
                        self.monety_reszta.append(l.get_nominal())
                        self.reszta -= l.get_nominal()
                        self.reszta = round(self.reszta, 2)
                        l.dec()
                    else:
                        logic = False
                if self.reszta == 0.0:
                    break

            if self.reszta == 0.0:
                self.monety_wrzucone = []
                self.sum_coins = 0.0
                self.sum_ticket = 0.0
                self.take_product()
                self.text = ""
                self.write("Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins) + "\nWEZ RESZTE ")
            else:
                for j in self.monety_reszta:
                    for k in self.monety_w_automacie:
                        if j == k.get_nominal():
                            k.inc()

                for j in self.monety_wrzucane:
                    for k in self.monety_w_automacie:
                        if j == k.get_nominal():
                            k.dec()

                print("reszta :", self.monety_reszta)
                self.monety_reszta = [x for x in self.monety_wrzucane]
                self.monety_wrzucane = []
                self.sum_coins = 0.0
                self.text = ""
                self.write("Wrzuć odliczoną kwotę!! \nWybierz ponownie ")

    def keys_operation(self, key):

        # od nowa czyli wyczyszczenie list
        if key == 10:
            self.choose_ticket = []
            self.text = ""
            self.sum_ticket = 0.0
            self.buy_ticket = []
            self.write("Nazwa:"+self.text + "\nKwota:" + str(self.sum_ticket)+ "\nWrzucono:" + str(self.sum_coins))
        #  produktu
        obj = ""
        if (key >= 0) and (key <= 5):
            change = key
            for i in self.ticket:
                if change == i.get_nr():
                    obj = i

            moneta = obj.get_cena()
            print(moneta)
            if moneta != 0.0:
                self.sum_ticket += moneta
                self.sum_ticket = round(self.sum_ticket, 2)  # zaokraglanie sumy monet
                print(self.sum_ticket)
                self.text += "\n" +str(obj.get_nazwa())
                self.buy_ticket.append(obj.get_nazwa())
                self.write("Nazwa:" + self.text + "\nKwota:" + str(self.sum_ticket) + "\nWrzucono:" + str(self.sum_coins))


        if (key == 11) and not (self.text == ""):
            if self.sum_coins > self.sum_ticket:
                self.reszta = self.sum_coins - self.sum_ticket
                print("Reszta :", self.reszta)
                self.rest(obj)

            elif self.sum_coins == self.sum_ticket:
                self.reszta = 0.0
                self.sum_coins = 0.0

                # dodawanie wrzuconych monet do monet w maszynie
                for i in self.monety_wrzucane:
                    for j in self.monety_w_automacie:
                        if i == j.get_nominal():
                            j.inc()

                #self.buy_ticket.append(obj.get_nazwa())
                self.monety_wrzucane = []
                self.text = ""
                self.write("Nazwa:" + self.text + "\nKwota:" + str(self.sum_ticket) + "\nWrzucono:" + str(self.sum_coins))
                self.take_product()
            else:
                self.write("Za mało pieniędzy !!\nWybierz ponownie ")
                self.text = ""

        elif self.text == "":
            self.write("Nie wybrałeś biletu !!")
            self.text = ""

    def take_coins(self):
        """Odebranie reszty"""
        print("reszta :", self.monety_reszta)
        mach = Tk()
        mach.title("WEŹ RESZTĘ !!!")
        gbc = Give_Back(mach, self.monety_reszta, "Twoja reszta")
        mach.mainloop()
        self.monety_reszta = []
        self.text = ""
        self.write("Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

    def take_ticket(self):
        """Odebranie biletu"""
        prod = Tk()
        prod.title("Odbierz bilet!!!")
        gbc = Give_Back(prod, self.kupione_bilety, "Twoje bilety ")
        prod.mainloop()
        self.kupione_bilety = []
        self.text = ""
        self.write("Nazwa:"+self.text+ "\nKwota:" + str(self.sum_ticket)+"\nWrzucono:" + str(self.sum_coins))

    def write(self, text):
        """Wypisywanie komunikatów na screenie"""
        self.screen.delete(0.0, END)
        self.screen.insert(0.0, text)


