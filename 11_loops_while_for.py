# For & while loops

# while loop:
x=0
while (x<=4):
    x=x+1
    print(x)

# for loop:
for x in range(2,10):
    print(x)


# Array (data set)
days=["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    print(d)
days=["mon","tue","wed","thu","fri","sat","sun"]

# Other Examples
for d in days:
    # if (d=="sat"):break   #loop stops
    if(d=="fri"):continue   #skips d
    print(d)


days=["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    print(d)


