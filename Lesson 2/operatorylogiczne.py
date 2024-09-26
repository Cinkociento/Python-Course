x = 3
y = 2
print(x > y and y == 2) # -> True jezeli po obu stronach jest prawda otrzymamy True a jezeli jedna z stron jest zla otrzymamy False
print(x > y and y != 2) # -> False

print(x > y or y != 2) # -> True jezeli po jednej z stron jest prawda to i tak utrzymamy True a False otrzymamy tylko wtedy gdy po obu stronach bedzie falsz
print(x > y or y == 2) # -> True