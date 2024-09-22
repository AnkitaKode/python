def generate_2d_array(m, n):
    array = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(i * j)  
        array.append(row)
    return array

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

result_array = generate_2d_array(m, n)

print("Generated 2D Array:")
for row in result_array:
    print(row)