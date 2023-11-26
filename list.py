#list[] #tuple() #set{}
marks=[23,45,28]

for score in marks:
    print(score)


print(marks)
print(marks[0])
print(marks[-1])
print(marks[0:2])
print(marks[1:3])

marks.append(89)
print(marks)

marks.insert(1,90)
print(marks)

print(89 in marks)

print(len(marks))


i=0
while i < len(marks):
    print(marks[i])
    i=i+1  

#to clear list
marks.clear()
print(marks)