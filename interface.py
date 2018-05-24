from tkinter import *
from tkinter import Frame,Button

class _Interface_(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.parent.title("Automat biletowy MPK")
        self.pack(fill=X, expand=True)



        topFrame=Frame(self)
        topFrame.pack()

        bottomFrame=Frame(self)
        bottomFrame.pack()
        lowFrame=Frame(self)
        lowFrame.pack()
        sideFrame=Frame(self)
        sideFrame.pack(side=RIGHT,fill=Y)


        k_bilet1=Button(topFrame, text="Bilet normalny 20 min", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN)
        k_bilet1.pack(side=LEFT, fill=X, expand=YES,anchor=W, padx=10, pady=10)

        k_bilet2=Button(topFrame , text="Bilet ulgowy 20 min", height=5,width=25,bg="#9F9FDF", overrelief= SUNKEN)
        k_bilet2.pack(side=LEFT, fill=X, expand=YES,anchor=W,padx=10,pady=10)

        k_bilet3=Button( bottomFrame, text="Bilet normalny 40 min", height=5,width=25,bg="#9F9FDF", overrelief= SUNKEN)
        k_bilet3.pack(side=LEFT, fill=BOTH,expand=YES, anchor=W,padx=10,pady=10)

        k_bilet4 = Button(bottomFrame, text="Bilet ulgowy 40 min", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN)
        k_bilet4.pack(side=LEFT, fill=X, expand=YES, anchor=W, padx=10, pady=10)

        k_bilet5 = Button(lowFrame, text="Bilet normalny 60 min", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN)
        k_bilet5.pack(side=LEFT, fill=X, expand=YES, anchor=N, padx=10, pady=10)

        k_bilet6 = Button(lowFrame, text="Bilet ulgowy 60 min", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN)
        k_bilet6.pack(side=LEFT, fill=Y, expand=YES, anchor=N, padx=10, pady=10)

        k_pusch_money= Button(sideFrame, text="Wrzuć monete", height=5, width=25, bg="#9F9FDF", overrelief=SUNKEN)
        k_pusch_money.pack(side=LEFT, fill=Y, expand=YES, anchor=N, padx=10, pady=10)
