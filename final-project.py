username=None #String
password=None
i = 0 #Integer
check = False #Boolean

username = input("Enter username ") #Login system
password = input("Enter password ") #Input command

while i < 2: #While loop
    if username == "DanielD" and password == "MisterGunnisthebest":  #If else statement
        check = True
        break
    else:
        i += 1
        print("Wrong input, you have {} more try (tries)".format(3-i))
        username = input("Enter username ")
        password = input("Enter password ")
if check ==  False:
    print("Too many failed attempts, quiting program")

# Initializing variables
rock    = 0
sand    = 0
pebbles = 0
gravel  = 0

# Read the file and take out the base values
def filer():
    global rock,sand,pebbles,gravel
    k  = [0,0,0,0]
    i  = 0
    fr = open("dailysales.txt", "r")
    for line in fr:
        contents = line.split()
        k[i] = int(contents[0]) #In order to make it easier, I chose one format for all 4 products: the ammount first then the type of product.
        i += 1
    rock    = k[0]
    sand    = k[1]
    pebbles = k[2]
    gravel  = k[3]
    fr.close()

# Add the daily sales into the values
def sort(x):  #Function
    global rock, sand, pebbles, gravel, y
    while True:
        if x in ["Rock","rock"]:
            y = int(input("Please enter the amount "))
            rock += y
            break
        elif x in ["Sand","sand"]:
            y = int(input("Please enter the amount "))
            sand += y
            break
        elif x in ["Pebbles","pebbles"]:
            y = int(input("Please enter the amount "))
            pebbles += y
            break
        elif x in ["Gravel","gravel"]:
            y = int(input("Please enter the amount "))
            gravel += y
            break
        else:
            print("Wrong type entered")
            x = input("Enter the type ")

# Write the daily sales in to the file after finishing the adding
def filew(): #Function
    global rock, sand, pebbles, gravel
    fw = open("dailysales.txt", "w+")
    fw.write("{} rock".format(rock))
    fw.write("\n")
    fw.write("{} sand".format(sand))
    fw.write("\n")
    fw.write("{} pebbles".format(pebbles))
    fw.write("\n")
    fw.write("{} gravel".format(gravel))
    fw.write("\n")
    fw.close()

# Take the average and total of the 4 types of variables
def opt2(): #Function
    aver  = (rock + sand + pebbles + gravel)/4 #Calculations
    total = rock + sand + pebbles + gravel
    print(aver, "is the average")
    print("{} is the total".format(total))

# Workers
def opt3(x): #Function
    fw = open("workers.txt", "a+")
    global w
    w = []
    for i in range(0,x):
        w.append([]) #2D array
        name = input("Enter the name of the worker: ") #In order to make it easier, I put the names of the workers before their roles
        w[i].append(name) #2D array append
        fw.write(name)
        fw.write(' ')
        role = input("Enter the role of the worker: ")
        w[i].append(role)
        fw.write(role)
        fw.write('\n')
    fw.close()

# Workers Sort
def sort_workers(k): #Function
    fr = open("workers.txt", "r")
    w = []
    t = 0
    for line in fr:
        contents = line.split()
        w.append([])  #2D array append
        for i in range (0,2):
            w[t].insert(1,contents[i]) #2D array insert
        t+=1
    if k == 'n':
        w.sort() #2D array sort
        print("The list is sorted by name") #Sort by the first element of each "row"
        print(w)
    if k == 'r':
        w.sort(key = lambda x : x[1]) #Sort by the second elemement of each "row"
        print("The list is sorted by role")
        print(w)
    fr.close()

# Main Loop
while check == True:
    print("Welcome to the program")
    print("1. Option 1: Enter the sale")
    print("2. Option 2: Find average and total")
    print("3. Option 3: Add new worker and salary")
    print("4. Option 4: Sort the worker list")
    print("5. Option 5: Exit the program")
    opt = int(input("Choose one of the options "))
    if opt == 1:
        filer()
        num =  int(input("How many sales do you want to enter "))
        for i in range (0,num):  #For loop
            type = input("Please enter the type of building materials ")
            sort(type)
        filew()
    if opt == 2:
        filer()
        opt2()
    if opt == 3:
        ind = int(input("How many workers do you want to enter? "))
        opt3(ind)
    if opt == 4:
        method = input("Type 'n' to sort by names and 'r' to sort by roles ")
        sort_workers(method)
    if opt == 5:
        print("Exiting the program...")
        break