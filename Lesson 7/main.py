#SLOWNIK DICTIONARY - zbior ktopry zawiera pary elementow KLUCZ:WARTOSC, moga to byc dowlne typy danych,
#z tym ze klucze nie moga sie powtarzac.
#JEST MUTOWALNY. JEST NIEUPORZADKOWANY, zamiast indexow, zeby dostac sie do wartosci uzywamy kluczy.

slownik = {'apple':'jablko', 'cat':'kot', 'wiek':25, 'czy_stary_wrocil_z_mlekiem':False}

print(slownik['apple'])

x = slownik.get('purple', 'fioletowy')
"""print(x)

print(slownik.keys())
print(slownik.values())

print(slownik.items())"""

for k, w in slownik.items():
  print(f'{k} : {w}')


x = 5.9865
print(f'hej {x}')
