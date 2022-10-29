x=12               #integer
y=12.5             #float
z="hi"             #string

# Implicit type conversion
x=x+y
print(x,type(x))
print(x,"type of x is:", type(x) )

# Explicit type conversion
age=input("what is your age") 
age=int(age)
print(type(age))

age=input("what is your age")
age=int(age)
print(age,type(age))
print(age,type(int(age)))
print(age,type(str(age)))