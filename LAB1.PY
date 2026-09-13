# Input / output
txt = input("Type something to test this out: ") 
print(txt)

# multiple print statements
print("helo");print("world")

#for indentation purpose
age=20
if age>18:
    print("eligible")
else:
    print("not eligible")

#different type checkings including imaginery part:
x="python"
print(type(x))

y=-234
print(type(y))

x=1+2j
print(type(x))

#Boolean (bool)
x=True
print(type(x))

x=False
print(type(x))

#Escape Characters Example
print("Line 1\nLine 2")        #\n (Newline) - Moves cursor to the next line
print("Column 1\tColumn 2")    # \t (Horizontal Tab) - Inserts a tab space
print("Literal Backslash: \\")  # \\ (Backslash) - Prints a single \
print("Single Quote: \'")     # \' (Single Quote) - Prints '
print("Double Quote: \"")      # \" (Double Quote) - Prints "


#String indices and accessing string elements
string="noor fatima"
print(string[-2])

#list:
my_list=["noor","fatima",19]
print(my_list[-1])

#access indexes:
my_list=["noor","fatima",19]
print(my_list[1:2])
print(my_list[:])
print(my_list[:2])

