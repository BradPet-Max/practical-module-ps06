#Q1-Create an array called students with 5 student names.
students = ["Peter", "Ntokozo", "Andre", "Sanele", "Hlogi"]

print(students)

#Q2-Create an empty array called vehicles.
vehicles = []

vehicles.append("Toyota")
vehicles.append("Ford")
vehicles.append("BMW")

print(vehicles)

#Q3-Create an array called marks with 4 subject marks.
marks = [75, 80, 65, 90]
print(marks[2]) #Print the 3rd subject mark

marks[0] = 85 #Change the 1st subject mark to 85
print(marks)

#Q4 -(Debugging)
cities = ["Polokwane", "Pretoria", "Cape Town"]
#print(cities[3]) #This will give an error because the index 3 is out of range. The valid indices are 0, 1, and 2.
print(cities[2]) # corrected to print the 3rd city, which is at index 2.