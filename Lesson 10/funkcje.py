#Funckje - blok kodu ktory wykonuje jakies zadanie i mozna go uzywac wiele razy. Ulatawiaja one czytanie i poslugiwanie sie kodem.
#ARGUMENTY!
#ZWRACANIE!
#STARAMY sie alby funckje bylky proste, czytelnme, elastyczne i kazda wykonywala jedno zadanie.

def srednia_ocen( imie_ucznia: str, liczba_ocen = 5):
  lista = []
  for i in range(liczba_ocen):
    ocena = int(input('Wpisz ocene: '))
    lista.append(ocena)
  avg = sum(lista)/len(lista)
  lista.clear()
  return avg



# def wypisz_srednia_do_pliku(srednia):
#   #wypisywanie do pliku



for u in range(1):
  srednia = srednia_ocen('Black<White', 3)
  #wypisz_srednia_do_pliku(srednia)
  print(f'srednia dla ucznia to {srednia}\n')

