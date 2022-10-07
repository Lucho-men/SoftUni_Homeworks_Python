# change = float(input())
# stotinki = int(change * 100)
# current_stotinki = stotinki
# coins_count = 0
#
# while current_stotinki - 200 >= 0:
#     current_stotinki -= 200
#     coins_count += 1
#
# while current_stotinki - 100 >= 0:
#     current_stotinki -= 100
#     coins_count += 1
#
# while current_stotinki - 50 >= 0:
#     current_stotinki -= 50
#     coins_count += 1
#
# while current_stotinki - 20 >= 0:
#     current_stotinki -= 20
#     coins_count += 1
#
# while current_stotinki - 5 >= 0:
#     current_stotinki -= 5
#     coins_count += 1
#
# while current_stotinki - 2 >= 0:
#     current_stotinki -= 2
#     coins_count += 1
#
# while current_stotinki - 1 >= 0:
#     current_stotinki -= 1
#     coins_count += 1
#
# print(coins_count)

current_sum = float(input())
current_sum = int(current_sum * 100)
coins_counter = 0
coins_counter += current_sum // 200
current_sum %= 200
coins_counter += current_sum // 100
current_sum %= 100
coins_counter += current_sum // 50
current_sum %= 50
coins_counter += current_sum // 20
current_sum %= 20
coins_counter += current_sum // 10
current_sum %= 10
coins_counter += current_sum // 5
current_sum %= 5
coins_counter += current_sum // 2
current_sum %= 2
coins_counter += current_sum // 1
current_sum %= 1

print(coins_counter)