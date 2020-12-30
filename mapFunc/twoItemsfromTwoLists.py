#Make new Fruits by sending two iterable objects into the function:
def myFanc(a , b):
    return a + b

frt1 = ['Apple' , 'Banana' , 'cherry']
frt2 = ['Orange' , 'lemon' , 'Apricots']
x = map(myFanc , frt1 , frt2 )
print(list(x))