# Make sure to use python2

from Tkinter import *
import ttk
import timeit
import random

def gcd(firstNum,secondNum):
	"""
	Return the greatest common factor of any two given numbers
	"""

	a = firstNum
	b = secondNum

	if b==0:
		return a
	else:
		return gcd(b, a % b)

def gcdEntry():
	firstNum = int(raw_input('What is your first number? '))
	a = firstNum
	secondNum = int(raw_input('What is your second number? '))
	b = secondNum
	print gcd(a,b)

def numberEntry():
	#I want to use this function to call it through a button press
	#allowing the prime test algorithm to run in the terminal when
	#the button is pressed
	number = int(raw_input("What number would you like me to check? "))

	#return the parameter number in the button Line: 214
	return number

def prime_check(number):

	# print number
	
	#Ask for user input and store it in 'number'
	number = number() # int(raw_input("What number would you like me to check? "))
	
	# Refuse a very long execution time
	if number > 2 ** 30: # # 2**30 is about 7.2e16, which means 72,000,000,000,000,000
		return "That number is too big to run this algorithm quickly."

	# Refuse anything but positive integers
	if type(number) not in (int, long) or number < 1:
		return "That number is not a positive integer."

	# Check is number is even

	if number%2 == 0 and number != 2:
		return "The number " + str(number) + " is not a prime number."
		
	# If there are divisor pairs, 
	# one divisor is <= number's square root
	max_divisor = int(number ** 0.5)
	max_divisor += 1 # So range() includes it
		
	# Check all possible divisors
	# from the odd numbers

	for possible_divisor in range(3, max_divisor, 2):
		if number % possible_divisor == 0: 
			# No remainder, so it's a factor
			return "The number " + str(number) + " is not a prime number."
	return "The number " + str(number) + " is a prime number."

	#print the results
	# print prime_check(number)
def do_prime():
	print prime_check(numberEntry)


class Calculator:

	# Stores the current value to display in the entry
	calc_value = 0.0

	# Will define if this was the last math button clicked
	div_trigger = False
	mult_trigger = False
	add_trigger = False
	sub_trigger = False

	#def prime_check

	# Called anytime a number button is pressed
	def button_press(self, value):

		# Get the current value in the entry
		entry_val = self.number_entry.get()

		# Put the new value to the right of it
		# If it was 1 and 2 is pressed it is now 12
		# Otherwise the new number goes on the left
		entry_val += value

		# Clear the entry box
		self.number_entry.delete(0, "end")

		# Insert the new value going from left to right
		self.number_entry.insert(0, entry_val)

	# Returns True or False if the string is a float
	def isfloat(self, str_val):
		try:

			# If the string isn't a float float() will throw a
			# ValueError
			float(str_val)

			# If there is a value you want to return use return
			return True
		except ValueError:
			return False

	def clear_text(self):
		self.number_entry.delete(0, 'end')

	# Handles logic when math buttons are pressed
	def math_button_press(self, value):

		# Only do anything if entry currently contains a number
		if self.isfloat(str(self.number_entry.get())):

			# make false to cancel out previous math button click
			self.add_trigger = False
			self.sub_trigger = False
			self.mult_trigger = False
			self.div_trigger = False

			# Get the value out of the entry box for the calculation
			self.calc_value = float(self.entry_value.get())

			# Set the math button click so when equals is clicked
			# that function knows what calculation to use
			if value == "/":
				print("/ Pressed")
				self.div_trigger = True
			elif value == "*":
				print("* Pressed")
				self.mult_trigger = True
			elif value == "+":
				print("+ Pressed")
				self.add_trigger = True
			else:
				print("- Pressed")
				self.sub_trigger = True

			# Clear the entry box
			self.number_entry.delete(0, "end")
			
	#def prime_check_press(self):
		#if do_prime:
			
			
		
		
		
		
		
		
		
		
		
		
	# Performs a mathematical operation by taking the value before
	# the math button is clicked and the current value. Then perform
	# the right calculation by checking what math button was clicked
	# last
	def equal_button_press(self):

		# Make sure a math button was clicked
		if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

			if self.add_trigger:
				solution = self.calc_value + float(self.entry_value.get())
			elif self.sub_trigger:
				solution = self.calc_value - float(self.entry_value.get())
			elif self.mult_trigger:
				solution = self.calc_value * float(self.entry_value.get())
			else:
				solution = self.calc_value / float(self.entry_value.get())

			print(self.calc_value, " ", float(self.entry_value.get()),
											" ", solution)
											
			# Turning off all triggers
			self.div_trigger = False
			self.mult_trigger = False
			self.add_trigger = False
			self.sub_trigger = False
			
			# Clear the entry box
			self.number_entry.delete(0, "end")

			self.number_entry.insert(0, solution)


	def __init__(self, root):
		# Will hold the changing value stored in the entry
		self.entry_value = StringVar(root, value="")

		# Define title for the app
		root.title("Calculator")
		# Defines the width and height of the window
		root.geometry("530x285")

		# Block resizing of Window
		root.resizable(width=False, height=False)

		# Customize the styling for the buttons and entry
		style = ttk.Style()
		style.configure("TButton",
						font="Serif 15",
						padding=10)

		style.configure("TEntry",
						font="Serif 18",
						padding=10)

		# Create the text entry box
		self.number_entry = ttk.Entry(root,
						textvariable=self.entry_value, width=50)
		self.number_entry.grid(row=0, columnspan=4)

		# ----- 1st Row -----

		self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

		self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

		self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

		self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

		# ----- 2nd Row -----

		self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

		self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

		self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

		self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

		# ----- 3rd Row -----

		self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

		self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

		self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

		self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

		# ----- 4th Row -----

		self.button_clear = ttk.Button(root, text="AC", command=self.clear_text).grid(row=4, column=0)

		self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)

		self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)

		self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

		self.prime_check = ttk.Button(root, text="Prime Check", command=lambda: do_prime()).grid(row=5, column=0)

		self.gcd = ttk.Button(root, text="GCD Check", command=lambda: gcdEntry()).grid(row=5, column=1)

		self.dotButton = ttk.Button(root, text=".", command=lambda: self.button_press('.')).grid(row=5, column=2)


# Get the root window object
root = Tk()

# Create Drop Down Menu
menu = Menu(root)
root.config(menu=menu)

#----------- Status Bar -------#
#status = Label(root, text='Preparing to do nothing...', bd=1, relief=SUNKEN)
#status.pack(side=BOTTOM, fill=X)

# Features Menu
subMenu = Menu(menu)
menu.add_cascade(label='About', menu=subMenu)
#subMenu.add_command(label='Prime Number Check', command = prime_check(number))

# Menu includes various editing tools
editMenu= Menu(menu)

# Current date and time
menu.add_cascade(label='Date and Time', menu=editMenu)


# Create the calculator
calc = Calculator(root)

# Run the app until exited
root.mainloop()