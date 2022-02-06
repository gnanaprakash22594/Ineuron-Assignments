#1a
list = [i for i in range(2000, 3201) if (i%7 == 0 and i%5 != 0)]
print(list)

#1b
fname = input("Input your first name:")[::-1]
lname = input("Input your last name:")[::-1]

print(fname +' '+lname)

#1c
pi = 3.14159265
d = 12
r = d/2

V = 4/3*pi*r**3

print("Volume of the sphere with diameter 12:", V)
