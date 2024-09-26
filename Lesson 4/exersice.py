ilosc = int(input("Podaj liczbe ocen: "))

oceny = []

for i in range(ilosc):
  ocena = int(input("Podaj oceny: "))
  oceny.append(ocena)

print(oceny)

"""#1 sposob
suma = 0
for i in range(ilosc):
  suma += oceny[i]

#2 sposob
suma = 0
for mark in oceny:
  suma += mark
#[1, 2, 3]
# mark = 1
#mark = 2"""

#3 sposob
suma = sum(oceny)

print(suma / ilosc)