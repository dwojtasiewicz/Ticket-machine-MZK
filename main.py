from tkinter import *
from interface import _Interface_

def main():
    try:
        root = Tk()
        root.geometry("1000x550")
       # tlo = Canvas(root, width=1000, height=550, bg="white")
        #tlo.pack()


        app=_Interface_(root)
        root.mainloop()
    except:
        print("Błąd w module main!!\nTworzenie okna głównego ")

if __name__=="__main__":
    main()