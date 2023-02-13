
# def dog_year_conv(years):
#     years = int(years)
#     if years < 0:
#         return "value must be larger than 0"
#     return years * 7
# human_years = input("Enter your dogs age:")
# print(dog_year_conv(human_years))

#1
def find_circumference(radius):
    pi = float(3.142)
    return radius * pi * 2
radius = int(input ("Enter radius for circ:"))
print("The circumference is: ")
print(find_circumference(radius))

def find_area(radius):
    pi = float(3.142)
return radius **2 * pi
radius = int(input ("Enter radius for area: "))
print("The area is: ")
print(find_area(radius))

# r = int(input("Enter radius: "))
# area = round(3.14 * r ** 2,2)
# circ = round(2 * 3.142 * r, 2)
# print(f"Area is {area} - Circumference is {circ}")

#2
here = int(input("Enter number 1 - 100: "))
for i in range(0,here+1,2):
        print(i)

#3
names = []
for i in range(3):
        name = input ("Enter a name: ")
        names.append(name)
print(names)


#4
num = int(input ("Enter num: "))
if num % 2 == 0:
        print("Even")
else:
        print("Odd")

#5
name = input("Enter your name: ")
(len(name))
print(len(name))

