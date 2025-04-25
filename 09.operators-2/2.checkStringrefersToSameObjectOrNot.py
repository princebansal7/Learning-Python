# when we take input from user: whether string is
# same or not they will be created as different object

print("Enter 2 strings: ")
str1, str2 = input(), input()

print(str1 is str2)

# -------------------------------------------------------
# But we assign by ourself: then
# if same string => same object
# if different string => different object

val1 = "prince"
val2 = "prince"
print(val1 is val2)  # True


val1 = "prince"
val2 = "princ"
print(val1 is val2)  # False
