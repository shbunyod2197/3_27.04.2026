# # 26
class Oyinchi:
    def __init__(self, ism):
        self.ism = ism

    def oynash(self):
        print("O‘ynayapti")

class Geymer(Oyinchi):
    def oynash(self):
        print("Video o‘yin o‘ynayapti")

a1 = Oyinchi("Ali")
a2 = Geymer("Vali")

a1.oynash()
a2.oynash()


# # 27
class Suv:
    def __init__(self, hajm):
        self.hajm = hajm

    def ichish(self):
        print("Ichildi")

class IchimlikSuv(Suv):
    def ichish(self):
        print("Toza suv ichildi")

a = IchimlikSuv(1.5)
a.ichish()


# # 28
class Kurs:
    def __init__(self, nomi):
        self.nomi = nomi

    def boshlash(self):
        print("Kurs boshlandi")

class PythonKurs(Kurs):
    def boshlash(self):
        print("Python kurs boshlandi")

a1 = Kurs("Umumiy kurs")
a2 = PythonKurs("Python")

a1.boshlash()
a2.boshlash()


# # 29
class Uy:
    def __init__(self, manzil):
        self.manzil = manzil

    def info(self):
        print("Uy mavjud")

class Villa(Uy):
    def info(self):
        print("Bu villa")

a = Villa("Chorvoq")
a.info()


# # 30
class Oqituvchi:
    def __init__(self, ism):
        self.ism = ism

    def dars(self):
        print("Dars bermoqda")

class DasturlashUstoz(Oqituvchi):
    def dars(self):
        print("Python darsi bermoqda")

a1 = Oqituvchi("Ali")
a2 = DasturlashUstoz("Vali")

a1.dars()
a2.dars()
