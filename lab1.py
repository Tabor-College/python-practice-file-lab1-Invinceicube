temp_celsius = int(input("enter temperature in celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32 

# conversion formula
print(f"The temperature in Fahrenheit is {temp_fahrenheit}")
if temp_celsius > 25: # 
    print("Go on beach")
elif temp_celsius > 15: # cold weather
    print("go hiking")
else:
    print("stay inside")

    