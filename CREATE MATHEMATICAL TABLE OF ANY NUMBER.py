def generate_table(number):
    for i in range(1, 11):
        result = i * number
        print(f"{i} x {number} = {result}")

try:
    num = int(input("Enter an integer: "))
    generate_table(num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
