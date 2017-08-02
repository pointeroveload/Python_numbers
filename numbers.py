#Numbers.py - Tom Weaver
#	Simple application showing Factorial, Fibonacci, Binary Search and Quick Sort algorithms in Python. 
#	Uses Python 3+ so may cause problems with 2.7, license free, do with it as you please. 
#
import os
import sys
import random
import time 

options = ['Exit', 'Fibonacci', 'Factorial', 'Quicksort', 'Binary Search']
selection = 0

#BinarySearch(): This function asks the user for numbers to use in the binary search, populates an array with a number of pseudo-random
#numbers, sorts the list and then uses the Binary Search algorithm to check if the element is present in the array. 
def BinarySearch():
	cls()
	print("* Binary Search *")
	#Ask the user for a series of numbers for use in the function
	start = int(input("Please enter a start number: "))
	end = int(input("Please enter an end number: "))
	st  = int(input("Please enter a number to search for: "))
	#Check that the start is > the end, else the array will be negative in size; useless!
	if start > end:
		print("\tYou can't have the start after the end, lets try again...")
		time.sleep(2)
		BinarySearch()
	#Create a list 
	alist = list()
	#fill the list with random numbers in the range of start->end 
	for i in range(0, end-start):
		alist.append(random.randint(start, end))
	#Sort the list using out QuickSortHelper function
	QuickSortHelper(alist, 0, len(alist)-1)
	#Create a variable,'res' which will be a numerical value if the element is found, or -1 if not
	res = BinarySearchHelper(alist, 0, len(alist)-1, st)
	#check the value of 'res' and print an appropriate message to the user
	if res != -1:
		print("\nFound element at index: %d" %res)
		print(alist)
	else: 
		print("\nElement is not present in the array!")
		print(alist)
	#Check if the user wants to repeat the function of go back to the start	
	if Repeat("Binary Search"):
		BinarySearch()
	else:
			Restart()
		
#BinarySearchHelper(): Helper function for BinarySearch() that takes a number or arguments and then performs the actual search.
#The return value is the place in the array the element resides if it is present, or -1 if not.
def BinarySearchHelper(arr, left, right, search):
	#Check if the value of 'right' is > than that of 'left'
	if right >= left:
		#Set midpoint by adding the value of 'right' - 'left' divided by two to the value of 'left'
		mid = int(left + (right - left) / 2)
		#If the value of 'mid' is the search term then return it
		if arr[mid] == search:
			return mid
		#else-if the element at 'mid' in the array is > the value of 'search' , recursively call BinarySearchHelper() 
		#by processing the left split of the array
		elif arr[mid] > search:
			return BinarySearchHelper(arr, left, mid-1, search)
		#else-if the element at 'mid' in the array is < the value of 'search' , recursively call BinarySearchHelper() 
		#by processing the right split of the array	
		else:
			return BinarySearchHelper(arr, mid+1, right, search);
	else:
		#If we get here then the value is not present in the array
		return -1

#cls(): Simple function to clear the console window
def cls():
	os.system('cls' if os.name=='nt' else 'clear')

#ComputeFactorial(): Helper function for Factorial() that takes an integer as an argument and then computes the factorial of this number. 
def ComputeFactorial(int):
	#create a var to hold initial value of 'int'
	px = int
	#loop from the value of 'int' backward by decrementing the value by -1 on each iteration
	for i in range(int-1, 0, -1):
		#set 'px' to the value of 'px' multiplied by the current value of 'i'
		px = px * i
	#return px
	return px

#Factorial(): Asks the user for a number to calculate the factorial of, calls the helper function ComputeFactorial() and then prints out 
#the result to the user. 	
def Factorial():
	cls()
	print("* Factorial *")
	#ask user to enter a positive integer 
	inp = int(input("Please enter a number > 0 and press enter: "))
	print("Computing...")
	#print out the series of integers used in the factorial
	for i in range(inp, 0, -1):
		if i == 1:
			sys.stdout.write(str(i))
		else:
			sys.stdout.write(str(i)+" * ")
	#finally print out the calculated Factorial. 
	else:
		print(" = "+str(ComputeFactorial(inp)))
	if Repeat("Factorial"):
		Factorial()
	else:
		Restart()

#ComputeFibonacci(): Helper function for Fibonacci() that takes an integer as an argument and then computes the fibonacci sequence up to the 
#entered value.		
def ComputeFibonacci(int):
	#vars
	f = 0
	s = 1
	out = ""
	#for loop, loop between 0 and the value of 'int'
	for i in range(0, int):
		#if i <=1 then 'n' is equal to i (useful in first few cases)
		if i <= 1:
			n = i
		#else 'n' is equal to 'f' plus 's', then set the value of 'f' to 's' and 's' to 'n'
		else:
			n = f + s
			f = s
			s = n
		#escape clause to print a '.' instead of a ',' for the final case
		if i  == int-1:
			out = out + str(n) + "."
		else:
			out = out + str(n) + ", "
	print("\n"+out)	

#Fibonacci(): Asks the user for a number to use as a limit, calls the helper function ComputeFibonacci() and then prints out the fibonacci
#sequence from 0 up to the limit. 
def Fibonacci():
	cls()
	print("* Fibonacci *")
	#Ask user to enter an integer for the number of steps they wish to calculate
	inp = int(input("Please enter the number of Fibonacci steps to compute and press enter: "))
	print("Computing...")
	#Call the helper function and pass the user entered value as an argument
	ComputeFibonacci(inp)
	if Repeat("Fibonacci"):
		Fibonacci()
	else:
		Restart()
	
#Main(): Main function for the application which calls the necessary functions at the beginning of running. 
def Main():
	cls()
	PrintOptions()
	Selection()
	
#PrintOptions(): Print out the options to the user so they can select which function they want to use
def PrintOptions():
	print("Welcome to Numbers.py, please make a selection.")
	print("\t1, Fibonacci")
	print("\t2, Factorial")
	print("\t3, QuickSort")
	print("\t4, Binary Search")
	print("\t0, Exit")
	print("(You can press Ctrl+C at any time to immediately exit the program)")
	print("Please enter the number of your selection and press enter.")

#QuickSort(): Asks the user to enter a whitespace separated list of numbers which is then passed to the QuickSortHelper() helper function.
#The sorted list is then printed out to the user. 
def QuickSort():
	cls()
	print("* Quicksort *")
	#Ask user for a list to sort
	s = input("Please enter a list of numbers separated by spaces and press enter: ")
	alist = list(map(int, s.split()))
	#Pass the list to the QuickSortHelper() function to sort it!
	QuickSortHelper(alist, 0, len(alist)-1)
	print("\n")
	print(alist)
	if Repeat("Quicksort"):
		QuickSort()
	else:
		Restart()	
	
#QuickSortHelper(): Helper function for QuickSort() that takes a list and two integers as arguments and then proceeds to sort the array.
def QuickSortHelper(alist, first, last):
	#First check that first is < last
	if first < last:
		#Create a new split point to halve the array
		splitpoint = Partition(alist, first, last)
		#Recursively call the QuickSortHelper() function on the left half of the array
		QuickSortHelper(alist, first, splitpoint-1)
		#Recursively call the QuickSortHelper() function on the right half of the array
		QuickSortHelper(alist, splitpoint+1, last)

#Partition(): A second helper function for QuickSort(), but which is called via QuickSortHelper() taking an array and two integers as arguments. 
#The function works out the next partition for the array and returns this to QuickSortHelper().
def Partition(alist, first, last):
	#set the pivot value
	pivotval = alist[first]
	#set the left as the second value in the array
	leftmark = first+1
	#set the right mark as the last value 
	rightmark = last
	#set the 'done' flag to false
	done = False
	#whilst 'done' is equal to false, continue
	while not done:
		#whilst 'leftmark' is less than or equal to 'rightmark' and the element at the value of 'leftmark' (e.g. the 4th element) in the array is less
		#than or equal to the pivot value 
		while leftmark <= rightmark and alist[leftmark] <= pivotval:
			#increment the value of 'leftmark' by 1
			leftmark = leftmark+1
		#Whilst element at the value of 'rightmark' in the array (e.g. the 12th element) is greater or equal to the pivot value, and 'rightmark' is 
		#greater or equal to 'leftmark'
		while alist[rightmark] >= pivotval and rightmark >= leftmark:
			#decrement the value of 'rightmark' by 1
			rightmark = rightmark - 1
		#If the value of 'rightmark' is less than that of 'leftmark' set done to True
		if rightmark < leftmark:
			done = True
		#else set temp to the element at the value of 'leftmark' in the array, set the element in the array at the value of 'leftmark' to the element
		#at the value of 'rightmark' in the array, and set the element in the array at the value of 'rightmark' to the value of temp
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
	#Set temp to the element in the array at the value of 'first'
	temp = alist[first]
	#Set the element at the value of 'first' in the array to the element at the value of 'rightmark' in the array
	alist[first] = alist[rightmark]
	#Set the element at the value of 'rightmark' in the array to the value of temp
	alist[rightmark] = temp
	#return the value of 'rightmark'
	return rightmark;

#Repeat(): This function takes a string argument and asks the user if they would like to repeat the function they have just used and returns
#true if so or false if not
def Repeat(str):
	print("\nWould you like to repeat the "+str+" function?" )
	sel = input("Please enter 'y' or 'n' and press enter: ")
	if sel.lower() in ['y', 'yes']:
		return True
	elif sel.lower() in ['n', 'no']:
		return False

#Restart(): This function is called when the program should restart, clears the console and then prints the options to the user. 
def Restart():
	cls()
	PrintOptions()
	Selection()
		
#Selection(): This function asks the user to enter an integer to select which function they would like to choose, then executes
#that function.		
def Selection():
	global selection
	selection = int(input("Selection: "))
	print("You selected: %s" %options[selection])
	if selection == 1:
		Fibonacci()
	elif selection == 2:
		Factorial()
	elif selection == 3:
		QuickSort()
	elif selection == 4:
		BinarySearch()
	
#Call Main() to begin the program. 	
Main()

	