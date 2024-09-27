lista = [1, 2, 2, 3, 1, 5, 1, 2, 6, 3, 6]
unikalne_liczby = []
for liczba in lista:
  if liczba not in unikalne_liczby:
    unikalne_liczby.append(liczba)

print(unikalne_liczby)