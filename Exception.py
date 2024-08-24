try:
    age=int(input("Age: "))
    print(f'Your age is {age}')

except ValueError:
    print("Invalid age.")