for i in range(0,101):
 
    if i % 2 == 0 and i % 5 == 0:
        print(str(i)+" buzz"+" bazz")
        continue
    if i % 2 == 0:
        print(str(i)+" buzz")
        continue
    if i % 5 == 0:
        print(str(i)+" bazz")
        continue
    
    print(i)