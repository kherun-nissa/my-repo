num = int(input("enter a no.to check its primr or not :"))
if num <=num:
    print("not prime")
else:
    i=1
    count=0
    while i <= num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("no.is prime")
    else:
        print("no.is composite")