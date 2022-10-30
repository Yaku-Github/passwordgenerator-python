import random

while (1==1):
    a = 1
    numbers = input("Type count of numbers you want (or q to quit): ")
    if (numbers == "q"):
        quit()
    nint = int(numbers)
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    caplets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    symbols = ["1","2","3","4","5","6","7","8","9","0","/","|","*","-","_","+","@"]
    output = []


    while (a <= nint ):
        random.seed()
        array = random.randint(1, 3)
        if (array == 1):
            random.seed()
            c = random.randint(0, 25)
            output.append(letters[c])
        if (array == 2):
            random.seed()
            c = random.randint(0, 25)
            output.append(caplets[c])
        if (array == 3):
            random.seed()
            c = random.randint(0, 16)
            output.append(symbols[c])
        a = a+1
    print (''.join(output))