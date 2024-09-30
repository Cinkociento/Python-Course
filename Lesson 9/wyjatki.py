#WYJATEK - exception - meahcanizm obslugi bledow w kodzie, pozwala na ich identyfikacje i reakcje.
import sys

"""try:
  liczba = int(input('podaj liczbe: '))
  print(liczba/2)
except :
  print('you are stupid')
"""

"""try:
  liczba = int(input('podaj liczbe: '))
  print(liczba/2)
except :
  print('you are stupid')
finally:
  print('Nigers is the best!')"""


#wznoszenie wyjatkow po poznaniu funckji !!!!!!!!!!!!!!!!!!!!

def podziel(a, b):
  try:
   wynik = a/b
  except ZeroDivisionError:
    sys.exit(1)
  return wynik

x = podziel(5, 1)

print(x)


def mnozenie(a, b):

  if b == 0:
    raise ValueError('nie bede mnozyl przez 0')
  else:
    wynik = a*b
    return wynik


try:
  y = mnozenie(5, 0)
except ValueError:
  y = mnozenie(5, 2)


print(y)