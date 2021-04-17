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
unique_list = []

def mainProgram():
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose one of the following options. Type a number ONLY")
        choice = input("""1. Add to list,
2. Add a bunch o' numbers
3. Get an item at an index
4. Sort list
5. Random Choice
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Quit   """)
            if choice == "!":
                addToList()
            elif choice == "2":
                addBunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for?  ")
                reursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySeatch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            else:
                break
    

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Please type an integer!   ")
    myList.append(int(newItem))
    #Think about errors!

def addABunch():
    print("We're gonna add a bunch of numbersto your list!")
    numToAdd = input("How many intergers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randit(0, int(numRange)))
    print("Your list is now complete!")


def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique values in your list?  Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)
       
    

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Oh I'm so random lul!")
    print(myList[random.randit(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randit(0, len(unique_list)-1)])

def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
        
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)

        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)

    else:
        print("Your number isn't here!")


def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)

if __name__== "__main__":
    mainProgram()
