# print(8//3) GIF 
# using #f-string can make cancatinate diffrent data types to a string
# example:


# score=80   #int
# height=1.6 #float
# isWon=True #boolean
# print(f"your score is {score}\nYour height is {height}\nYou are good ? {isWon}")

#How many weeeks left if you live till you are 90 years old
#Assuming all years are non leap

age = float(input("What is your current age?\n"))
year=90-int(age)
month=year*12
week=year*52
day=year*365

#using f-string to concatenate integer with string
print(f"You have {day} days, {week} weeks, and {month} months left.")