# #Odd Even Number
# number=int(input("Enter number"))
# if number % 2 ==0:
#     print("Even Number:",number)
# else:
#     print("Odd Number:",number)

# #odd Even List 
# number=[88,66,77,88]
# for i in number:
#     if num%2 ==0:
#         print("Even Number:",number)
#     else:
#         print("Odd Number:",number)

# #positive negative number
# Check whether a number is positive, negative, or zero
num=int(input("enter num"))
if num<0:
    print("Positive")
elif num>0:
    print("negative")
else:
    print("zero")
#count how to many odd even number range 1 to 20
Even_num=int(input("enter num"))
Odd_num=int(input("enter num"))
for i in range(1,20):
    if i%2 ==0:
        Even_num +=1
    else:
        Odd_num +=1
print("even Number is:",Even_num)
print("odd number is:",Odd_num)