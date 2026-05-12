#Random programs in Python
'''
def outer_function():
    global a  # This will refer to the global variable 'a' defined outside the function
    a=50
    def innerfunction():
        global a
        a=25
        print(a)
    innerfunction()
    print(a)
a=15
outer_function()
print(a)
'''
'''
for i in range(5):
    print(i)
else:
    print("Loop is over")
'''
'''
i=0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop is over")    
'''
'''
from operator import index


a=(1,2,3,4,5)
for i in a:
    print(i)
print(a.index(3))    
print(a[::-1]) 

a=list(a)

a.sort()
#a=tuple(a)
a.reverse()
print(a)   

b=a.copy()
print(b)
'''
'''
my_tuple=(1,2,3,4,5,6,7,8,9) #Tuples are immutable, so we cannot change their elements directly. However, we can convert the tuple to a list, modify the list, and then convert it back to a tuple if needed.
my_tuple=list(my_tuple)
my_tuple.clear()
print(my_tuple)
'''
'''
my_set={1,2,3,4,5}
my_set.add(6)
my_set.discard(20) #discard() method is used to remove an element from a set if it is present. If the element is not present, it does nothing and does not raise an error.
my_set.remove(20)  #remove() method is used to remove an element from a set. If the element is not present, it raises a KeyError.
print(my_set)
'''
'''
my_set1={1,2,3,4,5}
my_set2={4,5,6,7,8}
print(my_set1.union(my_set2)) #union() method is used to combine two sets and return a new set that contains all the unique elements from both sets.
print(my_set1.intersection(my_set2)) #intersection() method is used to find the common elements between two sets and return a new set that contains only those common elements.
print(my_set1.difference(my_set2)) #difference() method is used to find the elements that are present in one set but not in the other set and return a new set that contains those unique elements.
print(my_set1.symmetric_difference(my_set2)) #symmetric_difference() method is used to find the elements that are present in either of the sets but not in both sets and return a new set that contains those unique elements.
print(my_set1.issubset(my_set2)) #issubset() method is used to check if all the elements of one set are present in another set. It returns True if the first set is a subset of the second set, and False otherwise.
print(my_set1.issuperset(my_set2)) #issuperset() method is used to check if all the elements of one set are present in another set. It returns True if the first set is a superset of the second set, and False otherwise.
'''
'''
tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.List is a collection which is ordered and changeable. In Python, lists are written with square brackets.
Set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.Set has no duplicate elements.
Dictionary is a collection which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.
'''
'''
my_dict={"name":"John","age":30,"city":"New York"}
print(my_dict["name"])
my_dict["address"]="123 Main St"
print(my_dict)
my_dict["age"]=31
print(my_dict)
my_dict.pop("city")
print(my_dict)
#dictionary is mutable,but the keys must be immutable (like strings, numbers, or tuples). Values can be of any data type and can be duplicated, but keys must be unique within a dictionary.
print(my_dict.keys())
print(my_dict.values())
print(my_dict.popitem()) #popitem() method is used to remove and return the last key-value pair from a dictionary. It returns a tuple containing the key and value of the removed item. If the dictionary is empty, it raises a KeyError.
print(my_dict)
my_dict.clear() #clear() method is used to remove all items from a dictionary. After calling this method, the dictionary will be empty.
print(my_dict)
del my_dict #del statement is used to delete a variable, list, or dictionary from memory. After using del on a variable, it will no longer exist and will raise a NameError if you try to access it.
#print(my_dict) #This will raise a NameError because my_dict has been deleted from memory.
'''
'''
squares={x: x**2 for x in range(10)} #This is a dictionary comprehension that creates a dictionary called 'squares'. The keys of the dictionary are the numbers from 0 to 9, and the values are the squares of those numbers. The syntax {key: value for item in iterable} is used to create a new dictionary by iterating over an iterable and applying an expression to each item.
print(squares)
print(1 in squares)  #This checks if the key '1' is present in the 'squares' dictionary. It returns True if the key is found, and False otherwise.
'''
'''
import sys

randomList=['a',0,2]
for entry in randomList:
    try:
        print("The Entry is ",entry)
        r=1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[1],"occured.")
        print("Next Entry.")
        print()
print("The reciprocal of",entry,"is",r)   

'''
'''
try:
    num=int(input("Enter a number :"))
    assert num % 2 ==0 #assert is used to check if a condition is TRUE.✅ If condition is True → nothing happens.❌ If condition is False → Python raises an exception (AssertionError)
except:
    print("Not an even number!")
else:
    reciprocal=1/num
    print(reciprocal)  
'''

'''
Procedure-oriented programming (POP) focuses on functions and follows a top-down approach,
 where a program is broken into smaller procedures that operate on data, which is usually shared and less protected. 
 In contrast, object-oriented programming (OOP) focuses on objects, combining data and functions into a single unit (encapsulation), and follows a bottom-up approach.
POP is generally simpler and suitable for small programs but offers less security and reusability, whereas OOP provides better data protection, modularity, and code reuse, making it more suitable for large, complex applications.
'''
'''
class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
blu=Parrot("Blu",10)
print(blu.sing("Happy"))
print(blu.dance())  
'''
'''
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim fast")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("run faster")
peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()        
            

'''
'''
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price : {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(1000)
c.sell()
'''
'''
class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")
def flying_test(bird):
    bird.fly()
blu=Parrot()
peggy=Penguin()
flying_test(blu)
flying_test(peggy)
'''
'''
for i in range(5):
    stack.append(i)
print(stack)
'''
'''
expression="1+2"
stack=[]
for ch in expression:
    if stack:
        if ch.isdigit():
            stack.append(ch)
        else:
            op=ch
            a=stack.pop()
            b=stack.pop()
            if op =='+':
                stack.append(a+b)
            elif op =='-':
                stack.append(a-b)
            elif op =='*':
                stack.append(a*b)
            else:
                stack.append(a/b)
print(stack[-1])

'''
'''
count=0
l=[]
for i in range(11,20):
    for j in range(1,10):
        if i%j==0:
            count+=1
    if count==1:
        l.append(i)
print(l)
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
Second=Node(20)
Third=Node(30)
first.next=Second
Second.next=Third
Third.next=None
temp=first
while temp is not None:
    print(temp.data)    
    temp=temp.next
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    print("Where to insert the new node ?")
    print("1. At the beginning")
    print("2. At the end")
    print("3. After a node")
    choice=int(input())
    if choice==1:
        insert_at_beginning()
    elif choice==2:
        insert_at_end()
    elif choice==3:
        insert_after_node()
    def insert_at_beginning(self):
        print("Enter the data to insert at the beginning :")
        data=int(input())
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


'''
stones= [1, 2, 3, 4, 5]

while len(stones)>1:
    





                    

    
   
  
 