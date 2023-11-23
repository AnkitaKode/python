students="Radha","Ankita","Annie","Bella","Rumi"

for student in students:
    if student=="Annie":
        break;
    print(student)

print("For continue statement")
for student in students:
    if student=="Annie":
        continue
    print(student)    