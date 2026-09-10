text = "Python"

for i in range(len(text)):
    print(i + 1, text[i])

for num in range(3, 31, 3):   # start=3, stop=31 (exclusive), step=3
    print("Multiple of 3:", num)

# Using while loop to print multiples of 3
num = 3
while num <= 30:             # condition keeps loop running
    print("Multiple of 3:", num)
    num += 3                 # prevents infinite loop
