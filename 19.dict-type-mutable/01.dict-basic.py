d = {}
print(d) # {}
print(type(d)) # <class 'dict'>

d = {100:"Ram",101: "Ramesh"}
print(d) # {100: 'Ram', 101: 'Ramesh'}
print(d[100]) # Ram
# print only keys
for key in d:
    print(key) # 100 101

# print values
for key in d:
    print(d[key]) # Ram Ramesh

d[102]="Ramu"
print(d) # {100: 'Ram', 101: 'Ramesh', 102: 'Ramu'}
del d[100]
print(d) # {101: 'Ramesh', 102: 'Ramu'}
d[102]="Sita"
print(d) # {101: 'Ramesh', 102: 'Sita'}

# other improtant dict methods
for key in d.keys():
    print(key) # 101 102

for value in d.values():
    print(value) # Ramesh Sita

for t in d.items():
    print(t) # (101, 'Ramesh') (102, 'Sita') => returns tuple

for key, value in d.items():
    print(key, value) # 101 Ramesh   102 Sita => unpacking tuple