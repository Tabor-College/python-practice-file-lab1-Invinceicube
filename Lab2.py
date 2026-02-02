print(str("Hello! Please enter each class grade and credit hours in the following formats"))
print(str("Grade Example: 93-100% = 4.0, 90-92.99% = 3.7"))
print(str("Credit Hours Example: 3 = 3, (enter 0.95)"))
print(str("please refer to the Tabor College Academic Catalog for your grades"))

Class_1_Grade = float(input("Class 1 Grade " ))
Class_1_Hours = float(input("Class 1 Credit Hours " ))
Class_2_Grade = float(input("Class 2 Grade " ))
Class_2_Hours = float(input("Class 2 Credit Hours " ))
Class_3_Grade = float(input("Class 3 Grade " ))
Class_3_Hours = float(input("Class 3 Credit Hours " ))
Class_4_Grade = float(input("Class 4 Grade " ))
Class_4_Hours = float(input("Class 4 Credit Hours " ))
Class_5_Grade = float(input("Class 5 Grade " ))
Class_5_Hours = float(input("Class 5 Credit Hours " ))
Class_6_Grade = float(input("Class 6 Grade " ))
Class_6_Hours = float(input("Class 6 Credit Hours " ))

Class_Hours_Sum = Class_1_Hours + Class_2_Hours + Class_3_Hours + Class_4_Hours + Class_5_Hours +Class_6_Hours
print(Class_Hours_Sum)

Class_1_Weighted = Class_1_Hours * Class_1_Grade
Class_2_Weighted = Class_2_Hours * Class_2_Grade
Class_3_Weighted = Class_3_Hours * Class_3_Grade
Class_4_Weighted = Class_4_Hours * Class_4_Grade
Class_5_Weighted = Class_5_Hours * Class_5_Grade
Class_6_weighted = Class_6_Hours * Class_6_Grade

Weighted_Sum = Class_1_Weighted + Class_2_Weighted + Class_3_Weighted + Class_4_Weighted + Class_5_Weighted + Class_6_weighted
print(float(Weighted_Sum))
Gpa = Weighted_Sum/Class_Hours_Sum
print (f" Your current GPA is {Gpa:.2f}")


# Elif Statements

if Gpa > 3.7:
    grade = "A"
elif Gpa > 3.5:
    grade = "B"
elif Gpa > 3.2:
    grade = "C"
elif Gpa > 2.6:
    grade = "D"
else:
    grade = "F"
print(grade)

# Radius Calculater
import math

A_circle = int(input("input area" ))
A_Pi = math.sqrt(A_circle/math.pi)n
print(A_Pi)

# Executing a Statement
for EachPress in range(7):
        print("live", end ="")

# Count Controlled Loops
for count in range(6):
    print(count, end = "")

# Loop Errors: Off-by-one Error
for count in range (1,4)
        print(count, end = "")

# Traverse through a sequence of data
list(range(6))
list(range(1,5))

# Steps in Range
list(range(1,6,2))


