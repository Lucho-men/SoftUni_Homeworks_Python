# print("Type a number:", end="")
# n = int(input())
# is_odd = True
# for i in range(0,n):
#     print(f"Number{i+1}=",end="")
#     number = int(input())
#     if number % 2 != 0:
#         print(f"{number} is odd!")
#         is_odd == False
#         break
#     else:
#         continue
# if is_odd == True:
#     print(f"All numbers are even.")

#print("Type a number:", end="")
n = int(input())
is_odd = True
for i in range(n):
    #print(f"Number{i+1}=",end="")
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        is_odd == False
        break
else:
    print(f"All numbers are even.")