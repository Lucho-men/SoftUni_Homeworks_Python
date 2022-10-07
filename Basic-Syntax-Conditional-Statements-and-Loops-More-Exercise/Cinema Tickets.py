# total_current_tickets = 0
# total_tickets = 0
# total_standard_tickets = 0
# total_student_tickets = 0
# total_kid_tickets = 0
# command = input()
#
# while command != "Finish":
#     movie_name = command
#     free_seats = int(input())
#     second_command = input()
#     total_current_tickets = 0
#     standard_tickets = 0
#     student_tickets = 0
#     kid_tickets = 0
#     while second_command != "End":
#         if second_command == "Finish":
#             break
#         type_of_ticket = second_command
#
#         if type_of_ticket == "standard":
#             standard_tickets += 1
#             total_standard_tickets += 1
#         elif type_of_ticket == "student":
#             student_tickets += 1
#             total_student_tickets += 1
#         elif type_of_ticket == "kid":
#             kid_tickets += 1
#             total_kid_tickets += 1
#         total_current_tickets += 1
#         total_tickets += 1
#         second_command = input()
#
#     print(f"{movie_name} - {((total_current_tickets/free_seats)*100):.2f}% full.")
#     command = input()
#
# print(f"Total tickets: {total_tickets}")
# print(f"{((total_student_tickets/total_tickets) * 100):.2f}% student tickets.")
# print(f"{((total_standard_tickets/total_tickets) * 100):.2f}% standard tickets.")
# print(f"{((total_kid_tickets/total_tickets) * 100):.2f}% kids tickets.")


student_tickets_counter = 0
kid_tickets_counter = 0
standard_ticket_counter = 0
total_tickets_counter = 0
command = input()
while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_ticket_counter += 1
        elif ticket_type == "kid":
            kid_tickets_counter += 1
        free_places -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    precent_full_hall = sold_tickets / total_places * 100
    print(f"{movie_name} - {precent_full_hall:.2f}% full.")
    command = input()
students_percent = student_tickets_counter / total_tickets_counter * 100
kids_percent = kid_tickets_counter / total_tickets_counter * 100
standard_percent = standard_ticket_counter / total_tickets_counter * 100
print(f"Total tickets: {total_tickets_counter}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")