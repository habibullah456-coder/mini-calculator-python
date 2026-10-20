a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

op= input (" + , - , * ,%, **,/, " )

if op=='+':
    print(a+b)
if op=='-':
    print(a-b)
if op=='*':
    print(a*b)
if op=='%':
    print(a%b)
if op=='**':
    print(a**b)
if op=='/':
    print(a/b)

else:
    print("you enter wrong value")