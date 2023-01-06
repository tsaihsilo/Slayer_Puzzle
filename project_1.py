print('Solve: SLAYER + SLAYER + SLAYER = LAYERS')

user_guess = input("What is your guess? ")
slayer = int(user_guess)
x = slayer % 100000
y = slayer // 100000
z = str(x) + str(y)
result = slayer + slayer + slayer

if result == int(z):
   print(str(z) + " == " + str(result) + " -> True")
else:
   print(str(z) + " == " + str(result) + " -> False")