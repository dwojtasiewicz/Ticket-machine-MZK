
class Ticket:
    count=0
    def __init__(self, name = "", prize = 0.0):
        """Inicjalizuj"""
        self.__nazwa = name
        self.__cena = prize
        self.__nr_produktu = Ticket.count
        Ticket.counting()
    def __str__(self):
        text = ""
        text += str(self.__nazwa + " :" + str(self.__cena))
        return text


    @staticmethod
    def counting():
        Ticket.count += 1

    def get_cena(self):
        """Zwraca cenę produktu"""
        return self.__cena

    def get_nazwa(self):
        """Zwraca nazwę produktu"""
        return self.__nazwa

    def get_nr(self):
        """Zwraca numer produktu"""
        return self.__nr_produktu
