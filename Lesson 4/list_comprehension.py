lista = [1,2,3,4,5,6,7]

#len() zwraca dlugosdc elementu, w tym prypadku ilosc elementow listy
for i in range(len(lista)):
  print(lista[i])

lista1 = []
#1 sposob wypelnienia listy od 1 do 100
for i in range(1, 101):
  lista1.append(i)

#2 sposob list comprehension
list1 = [i for i in range(1, 101)]


