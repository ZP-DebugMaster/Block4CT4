"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

"""
Sometimes we want our computer to pick a random number in a given range, pick a random card from a deck, or flip a coin.
The random module will provide access to functions that support these types of operations.
"""
import random
myList = []
unique_list = []


"""
def mainProgram is a function that is the starting point to any python program that you make. 
"""
def mainProgram():
"""
The while True loop means to run forever or runs ss long as an expression evaluates to true.
Thats why you would need a beak statement to stop the loop.
"""
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

            """
            The elif statement is python's way of saying, "if the previous conditions were not true, then try this condition."
            An if statement is basically comparing two values that either have a true of false output. If its true it'll print yes and if its false it'll print no.
            A break statement is used to end a loop, if its used without an argument it will end the function and returns to where the code was executing previously.
            """
            if choice == "1":
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
    
"""
Lists are used to store multiple items in a single variable. In this list we will be adding numbers because we have
input("Please type and integer! "). 
"""
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Please type an integer!   ")
    myList.append(int(newItem))
    #Think about errors!
"""
This command just adds a lot of numbers and I mean a lot of numbers. 
"""
def addABunch():
    print("We're gonna add a bunch of numbersto your list!")
    numToAdd = input("How many intergers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randit(0, int(numRange)))
    print("Your list is now complete!")

"""
The sort method sorts the list ascending by default. 
"""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique values in your list?  Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)
       
    
"""
An index value searches for a given element from the start of the list and returns the lowest index where the element appears.
"""
def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])
"""
Random serach keeps generating a value until the best possible value is found, it will keep generating points until it finds the best one. 
"""
def randomSearch():
    print("Oh I'm so random lul!")
    print(myList[random.randit(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randit(0, len(unique_list)-1)])
"""
The linear search function is an algorithm that will find a target value within a list,
it sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched.
"""
def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your item is at index position {}".format(x))
"""
Recursive binary search searches for a item in a list just like iterative but instead of following instructions step by step in a loop,
it just continues to call itself.
"""
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

"""
Iterative binary search uses loops to repeat a whole set of instructions instead of just calling itself over and over like recursive binary search. 
"""
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

"""
Print is a statement that takes a number of arguments. It prints the arguments with a space in between.
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)


"""
This gives us flexibility to be able to have the script behave differently if it's executed directly vs. called externally.
"""
if __name__== "__main__":
    mainProgram()
