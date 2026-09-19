#While Loop
count=0
while(count<3):
    count+=1
    print("noor")

# Single statement while block 
count = 0
while (count == 0): print("Hello Geek") #this will gave infnite loop because no condition to terminate    

#for in Loop:
#Syntax:
#or iterator_var in sequence: 
#tatements(s)

#Example 1
# Python program to illustrate 
# Iterating over a list 
print("List Iteration")
l = ["geeks", "for", "geeks"] 
for i in l:
        print(i)

 #example 2:
print("\nTuple Iteration")
t = ("geeks", "for", "geeks") 
for i in t:
      print(i)

 # Iterating by index
list = ["geeks", "for", "geeks"] 
for index in range(len(list)):
                    print (list[index])

 #Loop Control Statements:
#1:Continue Statement

for letters in 'greeforgrek':
            if letters == 'e' or letters == 's':
               continue
            print ('Current Letter :', letters)

 #Break Statement: 
for letters in 'greeforgrek':
            if letters == 'e' or letters == 's':
               break
            print ('Current Letter :', letters)

#Calling a Function
#To call a function, use the function name followed by parenthesis:
#Example
def my_function():
                print("Hello from a function")
my_function()

#Parameters:
def fun(fname):
    print(fname+"is 19")
fun("noor")    

#Default Parameter Value:
def fun(country='pak'):
    print(country+" is my land")
fun("janah")
fun()

#Passing a List as a Parameter:
def fun(food):
    for x in food:
        print(x)
fruits=["apple","mango" ,"grapes"]
fun(fruits)

#return values:
def fun(a):
    return a*5
print(fun(2))    

#class:
class Person:
     def __init__ (self, name, age): 
         self.name = name
         self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
