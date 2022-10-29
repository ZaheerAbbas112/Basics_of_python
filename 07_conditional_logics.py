#logical operators are either "true or false" or "yes or no" or "0 or 1"

# equal to                                  ==
# not equal to                              !=
# greater than                              >
# less than                                 <
# greater than and equal to                 >=
# less than and equal to                    <=

print(8==8)
print(3!=3)
print(3>2)
print(6<9)
print(4>2)
print(5>=8)
print(6<=9)
print(2>=5)

# Application of logical operators
nazar_age=5
school_age_requirement=4
print(nazar_age==school_age_requirement)

# Input function & logical operator
age_at_school=5
nazar_age=input("how old nazar is?  ")  
nazar_age=int(nazar_age)
print(type(nazar_age))    
print(nazar_age==age_at_school)             #logical operator

# Logical operator without input function
five=5
age_at_school=five
nazar_age= five
print(type(nazar_age))
print(nazar_age==age_at_school)
