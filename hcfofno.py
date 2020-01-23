def shcf(a,b):
    if a>b:
       smaller=b
    else:
        smaller=a
    hcf=1
    for i in range(1,smaller+1):
        if (a%i == 0) and (b%i == 0):
            hcf=i
    return hcf
print("the hcf of{} and {} is {}".format(50,60,shcf(50,60)))
           