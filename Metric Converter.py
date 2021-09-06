# This is a Homework 1 – CSE 120 – Introduction to Python (Leo Williams).

print("Problem 2: Miles to Kilometers Program")


#Ask and save miles input from the user
miles = float(input("Enter value of miles: "))

#conversion factor
conv_fac =  1.6093

#calculate miles (Formula for an approximate result, multiply the length value by 1.6093)
kilometers =  miles * conv_fac

#output the result.
#To simplify the answer i convert it to only one decimal (%0.1f).
print("%0.1f miles is equal to %0.1f kilometers" %(miles, kilometers))

print("Thank You!")