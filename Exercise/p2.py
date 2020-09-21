#1
degrees= float(input("enter angle here: "))
radians= degrees*3.14/180
print("Degrees: ",degrees)
print("Radians: ",radians)

#2
student1= float(input("enter score here: "))
student2= float(input("enter score here: "))
student3= float(input("enter score here: "))
average= (student1+student2+student3)/3
print("student 1: ",student1)
print("student 2: ",student2)
print("student 3: ",student3)
print("average: ",average)

#3
class1=32
class2=45
class3=51

print("Number of students in each group: ")
print("Class 1: ",class1//5)
print("Class 2: ",class2//7)
print("Class 3: ",class3//6)

print("Number of students leftover: ")
print("Class 1: ",class1%5 )
print("Class 2: ",class2%5 )
print("Class 3: ",class3%5 )

#4
pi= 3.14
pie_diameter= 55.4
pie_radius= pie_diameter / 2
circumference= 2*pi*pie_radius
circumference_msg= "Jimmy’s pie has a circumference: "
print(circumference_msg, circumference)

#5
velocity=float(input("enter velocity: "))
frequency=float(input("enter frequency: "))
wavelength=velocity/frequency
print("The velocity (m/s): ",velocity)
print("The frequency (Hz): ",frequency)
print("The wavelength (m): ",wavelength)
