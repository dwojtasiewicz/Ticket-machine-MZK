from interface import Maschine
from tkinter import *
def main():
    #try:
        root = Tk()
        root.geometry("389x515")
       # tlo = Canvas(root, width=1000, height=550, bg="white")
        #tlo.pack()

        root.resizable(width=False, height=False)


        app=Maschine(root)
        root.mainloop()
  #  except:
   #     print("Błąd w module main!!\nTworzenie okna głównego ")

if __name__=="__main__":
    main()