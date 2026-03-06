
"""Basic Fucntions"""
def greet_user():
    name = input("enter your name: ")

    print(f"hello, {name}! Welcome to the course!")

greet_user()

"""Parameters vs Arguments"""
def calculate_tool(price, quantity):
    total = price * quantity
    return total

item_price = 19.99
item_quantity = 3
bill_total = calculate_tool(item_price, item_quantity)
print("total bill:", bill_total)

"""Default Parameters"""
def checkout(amount, shipping=5.0):
    final_amount = amount + shipping
    return final_amount
print("Order 1 total:",checkout(50))
print("Order 1 total:", checkout(50, shipping=10))

"""Keyword Arguments"""
def register_student(name_2,program,year):
    print(" -------Student Registration-------")
    print(f"Name   :{name_2}")
    print(f"Program  : {program}")
    print(f"Year.  {year}")
    print("-----------------------")

register_student("Anu", "computer science", 1)
register_student(year=2, name_2="Rahul", program="Data Science")

"""*args (Variable Positional Arguments)"""
def average_score(*scores):
    if not scores:
        print("No scores provided.")
        return None
    
    total = sum(scores)
    avg = total / len(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg}")
    return avg

average_score(80,90,75)
average_score(100,95)
average_score()

"""**Kwargs (Variable Keyword Arguments)"""
def create_profile(**info):
    if not info:
        print("Empty Profile.")
        return
    print("------ User Profile ------")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print("---------------")

create_profile(name="K", role="Professor", department="CS")
create_profile(name="Sam", City="Sacramento",)
create_profile()

"""Combining *args and **kwargs"""
def log_event(event_type, *details, **metadata):
    print("=== Event Log ===")
    print(f"Type {event_type}")

    if details:
        print(f"Details: {details}")
    else:
        print("Details: (none)")

    if metadata:
        print("Metadata:")
        for key, value in metadata.items():
            print(f" {key} = {value}")
    else:
        print("Metadata: (none)")
    print("===============")

log_event("LOGIN","Success", user="K", ip="192.168.0.10")
log_event("FILE_UPLOAD","report.pdf", size="2MB")
log_event("PING")

"""Return Multiple Verses"""
def analyze_sales(sales):
    if not sales:
        return None, None, 0,0

    min_sale = min(sales)
    max_sale = max(sales)
    total = sum(sales)
    average = total / len(sales)
    return min_sale, max_sale, total, average

week_sales = [120,150,90,200,175]
min_s,max_s,total_s,avg_s, = analyze_sales(week_sales)

print(f"Min sale : ${min_s}")
print(f"Max sale : ${max_s}")
print(f"Total sale : ${total_s}")
print(f"min sale : ${avg_s:2f}")

"""Scope: Local vs Global Variables"""

balance = 1000

def deposit_correct(amount):
    global balance
    balance = balance+amount
    print(f"Deposited ${amount}, new balance = ${balance}")
def deposit_wrong(amount):
    balance = balance + amount
    return balance
print("initial balance:", balance)
deposit_correct(200)
print("After deposit:", balance)

"""Higher-Order Functions"""
def ten_percent_discount(amount):
    return amount *.9
def flat_five_discount(amount):
    return amount - 5

def apply_discount(amount,discount_func):
    new_amount = discount_func(amount)
    print(f"Original: ${amount}, After discount: ${new_amount}")
    return new_amount

apply_discount(100, ten_percent_discount)
apply_discount(100, flat_five_discount)

"""Lambda Fucntions"""

square = lambda x: x**2
print(square(5))

products = [
    ("notebook", 4.99),
    ("Pen", 1.49),
    ("Backpack", 29.99),
    ("Bottle", 9.99)
]

sorted_by_price =sorted(products,key=lambda item:item[1])
print("Products")
for name, price in sorted_by_price:
    print(f" {name}: ${price}")

"""Docstrings"""

def celsius_to_fahrenheit(c):
    return (c*9/5+32)

result = celsius_to_fahrenheit(37)
print(f"37•C in fahrenheit = {result}•F")

print("\nDocstring:")
print(celsius_to_fahrenheit.__doc__)
    


