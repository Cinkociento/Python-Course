# lista = [1, 0.5] # tworzy liste z wybrana zawartoscia w srodku
lista = [] # tworzy pusta liste o nazwie lista
lista.append(1) # dodaje liczbe 1 do listy
lista.insert(2, 1.5) # dodaje liczbe 1.5 na index 2, bo pierwsza liczba to index na ktory dodajemy cos. A rzeczy po przecinku to zawartosc ktora dodajemy
print(lista)
print(lista[2])# wyswietla index 2

my_list = [True, 1, 'siema']


#przypisujemy zawartosc my_list do my_list1
my_list1 = my_list
my_list1.clear()
#w takim przypadku my_list tez sie wyczysci bo my_list1 ma taki sam adres w pamieci
#doslownie są tym samym

#w takim przypadku tworzy nam sie kopia my_list, dzieki czemu zmieniajac my_list1 elementy w my_list sie nie zmieniaja
my_list1 = my_list.copy()
my_list1.clear()

#mozna robic incepcje list xd, albo inaczej stackowanie, jesli chcemy odwolac sie do elementu zagniezdzonego to dajemy taki podwojny index jak ponizej
kulki = [[1,2], [3,4]]

print(kulki[0][0])


#wycinki list
osoby = [ 'a', 'b', 'c', 'd', 'e', 'f']

print(osoby)#wszytkie oosby
print(osoby[3])#b
print(osoby[-1])#f, zawsze ostani element listy
print(osoby[-2])#e

# [start, stop, przeskok]
print(osoby[0:3])#a, b, c, d
print(osoby[0:3:2])#a, c
print(osoby[2:-2])#c, d