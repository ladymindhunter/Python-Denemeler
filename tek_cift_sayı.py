def tek():
    print("Girdiğiniz sayı bir tek sayıdır!")

def çift():
    print("Girdiğiniz sayı bir çift sayıdır!")

sayı=input("Lütfen bir sayı giriniz: ")
if int(sayı)%2==0:
    çift()
else:
    tek()
