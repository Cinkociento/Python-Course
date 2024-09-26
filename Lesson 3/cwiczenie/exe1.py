a = int(input("Podaj dlugosc 1 boku trojkata: "))
b = int(input("Podaj dlugosc 2 boku trojkata: "))
c = int(input("Podaj dlugosc 3 boku trojkata: "))

if a+b>c and a+c>b and b+c>a:
  print("mozesz stworzyc trojkat")
else:
  print("Nie mozesz stworzyc trojkata")