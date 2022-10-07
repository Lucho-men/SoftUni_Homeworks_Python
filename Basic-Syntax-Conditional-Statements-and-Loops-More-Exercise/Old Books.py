favourite_book = input()
checked_books = 0
current_book = input()

while current_book != "No More Books" and current_book != favourite_book:
    checked_books += 1
    current_book = input()

if current_book == favourite_book:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")


