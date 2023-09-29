# Module 5 & 6
#Question 1: lls all the dice once and prints out the sum of the numbers.
# Use a for loopWrite a program that asks the user how many dice to roll.
# # The program ro

# import random
# dice = int(input("How many dice do you want to roll? "))
#
#
# def roll_dice(num_dice):
#     rolls = 0
#     for i in range(1, num_dice + 1):
#         print(f"Roll #{i} = {(roll := random.randint(1, 6))}")
#         rolls += roll
#     return rolls
#
#
# result = roll_dice(dice)
# print(f"The total for {dice} rolls is {result}.")





#Question 2: Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

# numbers=[]
# while numbers !="":
#     number=input("Enter your numbers:  or press Enter to quit: ")
#     numbers.append(number)
#     numbers.sort(reverse=True)
#     if number =="":
#         break
# print(numbers[:5])


# Question 3: Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

# number = int(input("Enter a number: "))
#
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(f"{number} is not a prime number")
#             break
#     else:
#         print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# Question no 4: Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.


# city_list = []
# for i in range(5):
#     city=input("Enter your city :  ")
#     city_list.append(city)
# print("Cities entered: ")
# for city in city_list:
#     print (city)

#Module 6

#Question 1
#Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
#
# import random
# import math
# number_of_dice = []
# def roll():
#     dice = random.randint(1, 6)
#     while dice != 6:
#         dice = random.randint(1, 6)
#         number_of_dice.append(dice)
#         if dice == 6:
#             break
#     for i in number_of_dice:
#         print(i)
#     return
# roll()

#Question no. 2
# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.


# import math
# import random
# number_of_dice = []
# side = int(input("Input the sides of dice: "))
# def roll(side):
#     dice = random.randint(1, side)
#     while dice != side:
#         dice = random.randint(1, side)
#         number_of_dice.append(dice)
#         if dice == side:
#             break
#     for i in number_of_dice:
#         print(i)
#     return
#
#
# roll(side)
#

# Question 3: Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
#Write a main program that asks for a volume in gallons from the user and converts the value to liters.
#The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
#
#
# def convert(gallon):
#     liter = gallon*3.78
#     return print(f"The amount in liters is {liter}")
#
# amount = float(input("Input the amount in gallons: "))
# while amount >= 0:
#     convert(amount)
#     amount=float(input("Input the amount in gallons: "))
#
# else:
#     print("Cannot convert negative value. Bye")

#Quetion 4
#Write a function that gets a list of integers as a parameter.
#The function returns the sum of all the numbers in the list.
#For testing, write a main program where you create a list, call the function, and print out the value it returned.
# def cal(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#
#     return print(total)
#
# list = [7,8,9,11,13]
# cal(list)

#Question 5: Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list,
# call the function,
# and then print out both the original as well as the cut-down list.
# def cal(numbers):
#     even_list =[]
#     for x in numbers:
#         if x%2 == 0:
#             even_list.append(x)
#     return print(list2), print(even_list)
#
# list2 = [5,6,7,9,10,23,56,21]
# cal(list2)

#Question 6 Write a function that receives two parameters: the diameter of a round pizza in centimeters
# and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

# import math
# def cal_pizza(diameter, price):
#     area = math.pi*(diameter/2*0.01)**2
#     price_per_meter_square = round(price/area,2)
#     return price_per_meter_square
#
#
# diameter1 = float(input("Input the diameter of pizza 1(cm): "))
# price1 = float(input("Input the price of pizza 1 (euro): "))
# a = cal_pizza(diameter1,price1)
#
#
# diameter2 = float(input("Input the diameter of pizza 2(cm): "))
# price2 = float(input("Input the price of pizza 2 (euro): "))
# b = cal_pizza(diameter2,price2)
#
# if a > b:
#     print("Pizza 2 is cheaper than pizza 1")
# elif a < b:
#     print("Pizza 1 is cheaper than pizza 2")
# else:
#     print("The price is even")
#




