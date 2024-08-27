import random

for i in range (2):
    print(random.random())
    
print(random.randint(10,20)) # Between two interval


members=["Ankita","Bella","Austin"]
leader=random.choice(members)
print(leader)