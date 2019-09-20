#cylinder.py finds the surface area and volume of a cylinder
#Alec Harmeling

length = input("Input a length)
length = float(length)
radius = input("Input a radius")
radius = float(radius)
volume = float(radius * radius * 3.14159 * length)
a1 = float(2 * 3.14159 * radius * length)
a2 = float(radius * radius * 2 * 3.14159)
area = float(a1 + a2)
print("The volume is" , volume)
print("The area is" , area)

input("\n\nPress enter to exit")
