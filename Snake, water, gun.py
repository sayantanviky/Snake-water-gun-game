import  random
def gameWin(Sayantan, you):
    if Sayantan == you:
        return None
    elif Sayantan == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Sayantan == 'w':
        if you == 'g':
            return False
        elif you  == 's':
            return True
    elif Sayantan == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Sayantan Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    Sayantan = 's'
elif randNo == 2:
    Sayantan = 'w'
elif randNo == 3:
    Sayantan = 'g'

you = input("Your Turn: Snake(s) Water(w) Gun(g)?")
a = gameWin(Sayantan, you)

print(f"Sayantan chose {Sayantan}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("Congrats! you Win!")
else:
    print("HaHa! you can't defeat Sayantan, you Lose!")