# petla while
n = 1

while n < 10: # nie wyswitla sie 10 bo jest warunek to mniejsze od 10 jak chcesz wyswietlic 10 to trzeba dac <= 10
  print(n)
  n+= 1

# petla for

for i in range(9): # nie wyswitli nam sie 9 bo idziemy od 0 do 8 jest to 9 liczb czyli 9 wykonan
  print(i)

for i in range(2, 9): # teraz wykonujemy od 2 do 8
  print(i)

for i in range(2, 9, 2): # teraz wykonujemy od 2 do 8 idac co 2 czyli 2, 4, 6, 8
  print(i)

# break i continue

for i in range(2, 10, 2):
  if i == 6:
    break # zatrzymuje program przed 6
  print(i)

for i in range(2, 10, 2):
  print(i)
  if i == 6:
    break # zatrzymuje program i wypisuje 6, bo najpierw wyprintuje sie 6 a pozniej wykona sie warunek i zatrzyma petle

for i in range(2, 10, 2):
  if i ==6:
    continue # ominie 6 i jej nie wypisze
  print(i)