
def numpor5():
 n = int(input('Ingrese el numero: '))
 var = 0
 count = 0 

 while var < n:
    var += 1
    print(var)
    if var % 5 == 0:
        count += 1 
 print(count)

numpor5()