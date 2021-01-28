print("""

Hata ve İstisnalar

""")

sayi1 = int(input("İlk sayı: "))
sayi2 = int(input("İkinci Sayı: "))
print(sayi1 / sayi2)

# -------------------------------------------

try:
    sayi1 = int(input("İlk sayı: "))
    sayi2 = int(input("İkinci Sayı: "))
    print(sayi1 / sayi2)

except ZeroDivisionError:
    print("Paydaya sıfır girilemez !!")

# -------------------------------------------

try:
    sayi1 = int(input("İlk sayı: "))
    sayi2 = int(input("İkinci Sayı: "))
    print(sayi1 / sayi2)

except ZeroDivisionError:
    print("Paydaya sıfır girilemez !!")

except ValueError:
    print("Düzgün formatta giriş yapılmadı !!")

# -------------------------------------------

try:
    sayi1 = int(input("İlk sayı: "))
    sayi2 = int(input("İkinci Sayı: "))
    print(sayi1 / sayi2)

except:
    print("Çalışma esnasında bir hata ile karşılaşıldı..")

# -------------------------------------------

try:
    sayi1 = int(input("İlk sayı: "))
    sayi2 = int(input("İkinci Sayı: "))
    print(sayi1 / sayi2)

except ValueError:
    print("Düzgün formatta giriş yapılmadı !!")

except:
    print("Tanımlı olmayan bir hata mevcut..")