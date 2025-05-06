list = ["mayhem", "madam", "Raipur", "bengaluru", "Hyderabad", "mumbai M"]
count = 0
for i in list:
    if i.endswith("m") or i.endswith("M"):
        count += 1

print("Number of strings which ends with M/m:", count)
