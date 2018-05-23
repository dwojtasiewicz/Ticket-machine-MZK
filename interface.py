from tkinter import *

def main():
    try:
        root = Tk()
        root.title("Automat biletowy MPK")
        root.geometry("550x550")
        root.mainloop()

    except:
        print("Błąd w module main!!\nTworzenie okna głównego ")

if __name__=="__main__":
    main()