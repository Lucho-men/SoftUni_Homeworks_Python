# n = int(input())
# salary = int(input())
#
# for i in range(n):
#     site = input()
#     if salary <= 0:
#         print("You have lost your salary.")
#         break
#     else:
#         if site == "Facebook":
#             salary -= 150
#         elif site == "Instagram":
#             salary -= 100
#         elif site == "Reddit":
#             salary -= 50
# print(f"{salary}")

open_tabs = int(input())
salary = int(input())

fine = 0

for site in range(open_tabs):
    site_name = input()

    if site_name == "Facebook":
        fine = 150
    elif site_name == "Instagram":
        fine = 100
    elif site_name == "Reddit":
        fine = 50
    else:
        fine = 0

    salary -= fine

    if salary <= 0:
        print("You have lost your salary.")
        break
    # else: # not needed actually
    # continue

if salary > 0:
    print(salary)
