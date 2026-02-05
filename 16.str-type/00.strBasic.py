s = "Hello   How are     you"
print(s.split(" ")) # ['Hello', '', '', 'How', 'are', '', '', '', '', 'you']
print(s.split()) # ['Hello', 'How', 'are', 'you']
print(s.split(",")) # ['Hello   How are     you']

s = "10,20,30"
print(s.split(",")) # ['10', '20', '30']


a=2.3467
print(f"hey, {a:.2f}") # rounding