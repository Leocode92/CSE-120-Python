# Leo Williams

# Python program to list numbers from 1 to 20 and label them odd or even.
# A number is even if division by 2 gives a remainder of 0., and if the remainder is 1, it is an odd number.

print("This program can count from 1 to 20 and identify the numbers if they are Even or Odd.")
# To change the range, just replace 21 with any number you want.


count = 0
for number in range(0, 21):
   if (number % 2) == 0:
      print(f"{number} is Even number")
   else:
      print(f"{number} is Odd number")