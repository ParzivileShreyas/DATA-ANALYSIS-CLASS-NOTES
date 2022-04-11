'''
# 1st lab question

def future(day):
    if day == 0:
        print("future is Sunday")
    elif day == 1:
        print("future is Monday")
    elif day == 2:
        print("future is Tuesday")
    elif day == 3:
        print("future is Wednesday")
    elif day == 4:
        print("future is Thursday")
    elif day == 5:
        print("future is Friday")
    elif day == 6:
        print("future is Saturday")

todaysDate = int(input("Enter an interger for today's day of the week from 0 - 6, Sunday is 0 and Saturday is 6."))


if todaysDate == 0:    
    print("Today is Sunday")
elif todaysDate == 1:
    print("Today is Monday")
elif todaysDate == 2:
    print("Today is Tuesday")
elif todaysDate == 3:
    print("Today is Wednesday")
elif todaysDate == 4:
    print("Today is Thursday")
elif todaysDate == 5:
    print("Today is Friday")
elif todaysDate == 6:
    print("Today is Saturday")


daysElapsed = int(input("Enter the number of days elapsed since today:"))
future((daysElapsed+todaysDate) % 7)


#2nd lab question
l=float(input("enter the length in METER="))
b=float(input("enter the width in METER="))
area=l*b
print("the area is",area,"m")


#3rd lab question
l=int(input("enter the length in feet="))
b=int(input("enter the width in feet="))
area=l*b
acre = area/43560
print("size of field",acre,"acres")


#4th lab question
n=int(input("enter positive number="))
s=(n*(n+1))/2
print("the sum of all numbers till n is =",s)


#5th lab question
def duplicate(li):
    n=len(li)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if li[i] == li[j] and li[i] not in dup:
                dup.append(li[i])
    return dup
n = int(input("Enter number of elements in the list : "))
ListA=[]
for i in range(0, n):
   print("Enter element No-{}: ".format(i+1))
   elm = int(input())
   ListA.append(elm) 
print("The entered list is: \n",ListA)
print("The duplicates in the given list is:",duplicate(ListA))


#6th lab question
a=int(input("enter thr 1st number="))
b=int(input("enter the 2nd number="))
c=int(input("enter the 3rd number="))
if a>=b and b>=c:
    print(c,"<=",b,"<-",a)
elif b>=a and a>=c:
    print(c,"<=",a,"<=",b)
elif c>=a and a>=b:
    print(b,"<=",a,"<=",c)
elif a>=c and c>=b:
    print(b,"<=",c,"<=",a)
elif b>=c and c>=a:
    print(a,"<=",c,"<=",b)
elif c>=a and a>=b:
    print(b,"<=",a,"<=",c)
elif c>=b and b>=a:
    print(a,"<=",b,"<=",c)


#7th lab question
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)

''' 

#8th lab question
s=input("Enter a string:")  #abcdef

#print(s[:]) #abcde
#print(s[0:5]) #abcde
#print(s[0:5:1]) #abcde
#print(s[::]) #abcde

revstr=(s[::-1])  #edcba reverse string

if revstr==s:
    print("palindrome")
else:
    print("Not palindrome")


