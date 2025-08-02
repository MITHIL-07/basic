import random

target = random.randint(1,100)

while True:
    i = int(input("Guss the number="))
    if(i == target):
        print("susccesfully..")
        break
    elif(i < target):
        print("take a bigger number..")
    elif(i > target):
        print("take a small number..")    

print()
print("-------GAME OVER-------")                                                     


