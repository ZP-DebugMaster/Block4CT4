"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will preform those actions above
import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY")
            choice = input("""  1. Add to list,
2. Add a bunch o' numbers
3. Return the value at an index position
4. Print contents of list
5. Random Choice
6. Linear Search
7. End Program  """)
            if choice == "!":
                addToList()
            elif choice == "2":
                addBunch()
            elif choice == "3":
                indexValues
            elif choice == "4":
                print(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            else:
                break
        except:
            print("An error occured")

def addToList():
    newItem = input("Please type an integer!   ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add bunch of numbers!")
    numToAdd = input("How many intergers do you want to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randit(0, int(numRange)))
    print("Your list is now complete!")
    

def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randit(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for?   Number-wise?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))

if __name__== "__main__":
    mainProgram()
