a=int(input())
b=int(input())
c=int(input())
d=int(input())
avg=(a+b+c+d)//4
if avg>=91 and avg<=100:
    print("A Grade")
elif avg>=81 and avg<91:
    print("B Grade")
elif avg>=71 and avg<81:
    print("C Grade")
elif avg>=61 and avg<71:
    print("D Grade")
elif avg>=51 and avg<61:
    print("Fail")
else:
    print("Invalid Input!")
