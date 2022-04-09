from random import randint

digit = 0
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-[]:;,./<>?_+*}`{=~|"
ID = ""

while True:
    try:
        digit = input("digit:")
        digit = int(digit)
    except:
        print("Please enter an integer.")
        continue
    finally:
        break

for _ in range(10):
    for __ in range(digit):
        ID += letter[randint(1, 82)];
    print(ID)
    ID = ""