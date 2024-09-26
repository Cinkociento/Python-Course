wiek = int(input("Podaj wiek: "))
if wiek >= 18: # if to takie gdy warunek jest spelniony print mozesz kupic piwo a gdy nie jest spelniony czyli else print jeszcze zawczesnie
  print("Mozesz kupic piwo!")
else:
  print("Jeszcze zawczesnie!")


wiek = int(input("Podaj wiek: "))
if wiek >= 21:
  print("Mozesz kupic piwo w Stanach i w Polsce")
elif wiek >= 18: # elif to taki 2 if, bo gdy if sie nie wykona(nie bedziesz miec 21 lat) to wykonuje sie 2 czyli elif dopiero jezeli on sie nie spleni wykonuje sie else
  print("mozesz kupic piwo tylko w Polsce")
else:
  print("Jeszcze zawczesnie!")