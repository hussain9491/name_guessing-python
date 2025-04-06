

import random
attempt = 0
real_values  = ["ESHAL", "FATIMA", "AREEBA","AISHA"]
print("hey! We play a game of guessing my naa mehram friend name,\n ")
print(" but you have only 5 attempts")


while attempt <5:
    guess = input("Guess my friend name: ").upper()
    attempt += 1
    if guess == random.choice(real_values) == "ESHAL":
        print("very closed but, why i am telling you my naa mehram friend name?😂😂 you have to",str(5 - attempt), "attempts left")
        continue
    elif guess not in real_values:
        print("wrong name brother you don't know my naa mehram friend name😗, you have to ", str(5 - attempt), "attempts")
        continue
    elif guess == random.choice(real_values) == "FATIMA":
      print("Astagfirullah", guess, "is not my friend😂, try again😉 you have to", str(5 - attempt), "attempts left")
      continue
    elif guess == random.choice(real_values) == "AREEBA":
        print("No wayy!", guess, "is my enemy🙂, try again😂 you have to",str(5 - attempt), "attempts left")
        continue
    else:
        print("wrong guess! try again😁you have to", str(5 - attempt), "attempts left")
        continue
    
        