import math

class Kalkulator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.history=[]

    def Dodawanie(self):
        #self.history.append(str(self.a) + " + " + str(self.b) + " = " + str(self.a+self.b))
        return self.a+self.b

    def Odejmowanie(self):
        self.history.append(str(self.a) + " - " + str(self.b) + " = " + str(self.a - self.b))
        return self.a-self.b

    def Mnozenie(self):
        self.history.append(str(self.a) + " * " + str(self.b) + " = " + str(self.a * self.b))
        return self.a*self.b

    def Dzielenie(self):
        if self.b==0:
            self.history.append("Próbowano dzielić przez zero :(")
            return print ("Nie dziel przez zero")
        else:
            self.history.append(str(self.a) + " / " + str(self.b) + " = " + str(self.a / self.b))
            return self.a/self.b

    def Historia(self):
        licznik=1
        print ("Historia operacji:")
        for x in self.history:
            print (str(licznik) +": " + x)
            licznik+=1

    def Pierwiastek(self):
        self.history.append("Pierwiastek z " + str(self.a) + " to " + str(math.sqrt(self.a)))
        return math.sqrt(self.a)

    def Potega(self):
        self.history.append("Postega z " + (self.a) + " to " + str(self.a*self.a))
        return self.a*self.a

    def ProcentAzB(self):
        self.history.append("Procent " + str(self.a) + " z " + str(self.b) + " to " + str((self.a/self.b*100))+"%")
        return (str((self.a/self.b*100))+"%")

    def Fibbo(self):
        self.history.append("Liczono ciąg Fibbonacziego do " + str(a))
        ciag = [1,1]
        for x in range(self.a-2):
            ciag.append(ciag[x] + ciag[(x + 1)])
        return ciag

    def LiczFibbo(self):
        suma=0
        ciag=self.Fibbo()
        for x in ciag:
            suma+=x
        self.history.append("Liczono sumę ciągu Fibbonacziego do " + str(a) + " i wyszło " + str(suma))
        return suma

    def IsEqual(self):
        self.history.append(str(self.a) + " + " + str(self.b) + " = " + str(self.a + self.b))
        if self.a==self.b:
            self.history.append("Porównano A i B - są równe")
            return "Równe"

        elif self.a>self.b:
            self.history.append("Porównano A i B - A jest większe od B")
            return "A jest większe od B"

        elif self.a<self.b:
            self.history.append("Porównano A i B - A jest mniejsze od B")
            return "A jest mniejsze od B"

    def mozliwosci(self):
        print ("Wybierz cyfrę, by dokonać odpowiednią operację")
        print("1 - Dodawanie")
        print("2 - Odejmowanie")
        print("3 - Mnożenie")
        print("4 - Dzielenie")
        print("5 - Pierwiastek")
        print("6 - Potęga")
        print("7 - Procent A z B")
        print("8 - Ciąg Fibbonaciego")
        print("9 - Suma ciągu Fibbonaciego")
        print("10 - Sprawdzenie, która liczba jest większa")
        print("11 - Historia operacji")
        print("12 - wyświetlenie opcji")

#----------------------KONIEC KALKULATORA------------------------------------------


#kreski="-----------------------------------------------------------"
#
# print ("Witaj w moim skromnym kalkulatorze")
# cal.mozliwosci()
# o= input("To co robimy?")
#
# while  o != 0:
#     if o == '1':
#         print("Dodawanie")
#         cal.a = int(input("Podaj liczbę 1: "))
#         cal.b = int(input("Podaj liczbę 2: "))
#         print(cal.Dodawanie())
#     elif o == '2':
#         print("Odejmowanie")
#         cal.a = int(input("Podaj liczbę 1: "))
#         cal.b = int(input("Podaj liczbę 2: "))
#         print (cal.Odejmowanie())
#     elif o == '3':
#         print("Mnożenie")
#         cal.a = int(input("Podaj liczbę 1: "))
#         cal.b = int(input("Podaj liczbę 2: "))
#         print (cal.Mnozenie())
#     elif o == '4':
#         print("Dzielenie")
#         cal.a = int(input("Podaj liczbę 1: "))
#         cal.b = int(input("Podaj liczbę 2: "))
#         print (cal.Dzielenie())
#     elif o == '5':
#         print("Pierwiastek")
#         cal.a = int(input("Podaj liczbę: "))
#         print (cal.Pierwiastek())
#     elif o == '6':
#         print("Potęga")
#         cal.a = int(input("Podaj liczbę: "))
#         print (cal.Potega())
#     elif o == '7':
#         print("Procent A z B")
#         cal.a = int(input("Podaj A: "))
#         cal.b = int(input("Podaj B: "))
#         print (cal.ProcentAzB())
#     elif o == '8':
#         print("Ciąg Fibbonaciego")
#         cal.a = int(input("Podaj liczbę: "))
#         print (cal.Fibbo())
#     elif o == '9':
#         print("Suma ciągu Fibbonaciego")
#         cal.a = int(input("Podaj liczbę: "))
#         print (cal.LiczFibbo())
#     elif o == '10':
#         print("Porównywanie")
#         cal.a = int(input("Podaj liczbę 1: "))
#         cal.b = int(input("Podaj liczbę 2: "))
#         print (cal.IsEqual())
#     elif o == '11':
#         print (cal.Historia())
#     elif o == '12':
#         cal.mozliwosci()  # <-zamiana na cal.mozliwosci powoduje "0 positional arguments but 1 was given"
#     else: print("Wybrano z poza listy")
#
#     print(kreski)
#     o = input("To co robimy?")