import itertools  
  
for i in itertools.count(10,5):  
    if i == 50:  
        break  
    else:  
        print(i,end=" ")