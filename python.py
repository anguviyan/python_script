#! /usr/bin/python
############################## sample program #################################
print("Hello world")
one = 1
print(one)
############################## Variable address #################################
print(id(one))
############################## if_else_ program #################################
if True:
    print("True")
else:
    print("False")
############################## Delete_variable #################################
#del(one)
#print(one)
############################## Variable_type #################################
two = str('sriram')
print(two)
print(type(two))

three = int(10)
print(three)
print(type(three))

four = float(10.1)
print(four)
print(type(four)) 
############################## Assignment_operator #################################
a=b=c=10
print(a)
print(b)
print(c)
############################## Boolean_example #################################
print(a is b)
############################## sample program #################################
d,e,f = 1,2,"sriram"
print(d)
print(e)
print(f)
############################## sample program #################################
apple = 10
orange = 20
total = apple * orange
print(total)
############################## variable_type #################################
var1 = 1
print(type(var1))

var2 = 'sriram'
print(type(var2))

var3 = 10.1
print(type(var3))

var4 = 3 + 4j
print(type(var4))

############################## String_Program #################################
str = 'Hello World'

print(str)
print(str[0])
############################## List Example ################################# Mutable means add/del/update #########################
p = ['a',1,10.1]
print(p[0])
print(p[1])
print(p[2])
p[0] = 'b'
print(p[0])
############################## Tuple Example #################################
q = ('a',1,10.1)
print(q[0])
print(q[1])
print(q[2])
#q[0] = 'b'
#print(q[0])-------->Error
#q[3] = 11---------->Error
#print(q[3])-------->Error

############################## List with Tuple Example #################################
r = [(1,2),('a','b')]
print(type(r))
print(r)

############################## For loop Example #################################
for i in range(5):
    print(i)
for i in range(1,3):
    print(i)
for i in range(1,5,2):
    print(i)
############################## Zip Example #################################
r = [1,2]
s = [3,4]
print(list(zip(r,s)))

############################## Dictnory Example #################################
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is Two'

tinydict = {'one': 1,'Two':2,'Three':3}

#tinydict['Four':4]----->Error
#tinydict['Three':4]----->Error

print(tinydict)
print(tinydict.keys())
print(tinydict.values())

tinydict.update({'Four':4})
#tinydict.add({'Five':5})----->Error
print(tinydict)

tinydict['Five'] = 5
print(tinydict)

print(tinydict['one'])

tut = {1:'sri',2:'ram',3:'dhivakar',4:{4:'Angu',5:'samy'}}
print(tut)

############################## Set Example ################################# Duplicat will be removed ###############
muki = {'beer',1,1.0}
print(type(muki))
print(muki)

myset = set(['a','b','c','c'])
print(myset)

myset.add('d')
print(myset)

myset.remove('d')
print(myset)

############################## Format Example #################################
k=1
l=2
m=0

m = l*k

print(k,l,m)
print("k:{} l:{} k*l:{}".format(k,l,m))
############################## Literal Example #################################
x = 0x1c
y = 0O34

print("x",x)
print("y",y)
############################## Arithmatic Example #################################
t=1
s=2
v = s*t
print("t:{} s:{} v:{}".format(t,s,v))
############################## Comparision Example #################################
e = 4
f = 5

if(e == f):
    print("Line1- e is equal to f")
else:
    print("Line2- e is not equal to f") 
############################## Assignment Example #################################
g = e + f
print("e:{} f:{} e+f:{}".format(e,f,g))

g += e
print("g:{} g+=e:{}".format(g,e))
############################## Input Example #################################
#name = input()
#city = input()

#print("Hello my name is",name)
#print("I am from",city)

#subject = input("Enter your subject: ")
#teacher = input("Enter your teacher: ")

#print("Name of the subject",subject)
#print("Name of your teacher",teacher)

#Number = raw_input("Enter your number. ")
#print("Number of yours",Number)

amount = str(input("Enter your weight: "))
print("My weight is: ",amount)
############################## Match Example #################################

u = input()

match u:
    case 'a': return "a is return"
    case _: return "Nothing"
