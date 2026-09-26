#1. Numbers divisible by 7 and multiple of 5
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number)

#2. Celsius and Fahrenheit Conversion
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(c, "C is", f, "Fahrenheit")

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f, "F is", c, "Celsius")

#3. Guess a Number Between 1 and 9
number = 7

while True:
    guess = int(input("Guess a number between 1 and 9: "))

    if guess == number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess, try again.")

#4. Pattern Using Nested For Loop:
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#5. Reverse a Word:
word = input("Enter a word: ")

reverse = word[::-1]

print("Reverse:", reverse)

#6. Count Even and Odd Numbers:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

#7. Print Each Item and Its Type:
data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": "V", "section": "A"}]

for item in data:
    print(item, type(item))

#8. Print Numbers 0 to 6 Except 3 and 6:
for number in range(7):
    if number == 3 or number == 6:
        continue

    print(number)

#9. Fibonacci Series Between 0 and 50:
a = 0
b = 1

while a <= 50:
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c

#10. Two-Dimensional Array
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

array = []

for i in range(m):
    row = []

    for j in range(n):
        row.append(i * j)

    array.append(row)

print(array)

#11. Input Lines Until Blank Line:
while True:
    line = input("Enter a line: ")

    if line == "":
        break

    print(line.lower())

# 12 Get binary numbers
numbers = input("Enter binary numbers separated by comma: ").split(",")

result = []

# Check each binary number
for num in numbers:
    if int(num, 2) % 5 == 0:
        result.append(num)

# Print result
print(",".join(result))

#13. Count Letters and Digits:
text = input("Enter a string: ")

letters = 0
digits = 0

for character in text:

    if character.isalpha():
        letters = letters + 1

    elif character.isdigit():
        digits = digits + 1

print("Letters:", letters)
print("Digits:", digits)


