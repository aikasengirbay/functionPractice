# def get_command():
#     """Show menu and calls commands. Returns commands"""
#     print "------------------"
#     print "You can add / view / check / exit"
#     command = raw_input("Action > ")
#     command = command.lower()
    
#     return command

# def add_book(books):
#     """Add new book. Returns new title"""

#     new_book = raw_input("Title > ")
#     new_book = new_book.title()
#     books.append(new_book)
    
#     return new_book

# def view_books(books):
#     """View all books"""

#     for book_list in books:
#         print book_list

# def check_books(books):
#     """Search for a book. If found return title if not None"""
    
#     book_check = raw_input("Title > ")
#     book_check = book_check.title()
#     if book_check in books:
        
#         return book_check    


# def library():
#     """Main loop"""
    
#     books = ["Dune", "Pride and Prejudice"]
#     print "Brighticorn's Books"
#     print "*** *** ***"

#     while True:
        
#         command = get_command()
#         print "Action:", command
        
#         if command == "exit":
#             print "Goodbye"
#             break
        
#         elif command == "add":
#             print "***   Add Book   ***"
#             book = add_book(books)
#             print "Added Book: ", book
        
#         elif command == "view":
#             print "*** View Books ***"
#             view_books(books)
#             print "*** End of listing ***"
        
#         elif command == "check":
#             print "*** Check for a Book ***"
#             found = check_books(books)
#             print "Found:", found

#         else:
#             return "The input is not an option"


# # print add_book([])

# # viewing_books = library(), check_books(books)
# # print viewing_books
# # print check_books(books)
# # print get_command()
# library()






ask_user = raw_input("whould you like to count, yes or no? > ")
ask_user = str(ask_user.lower())

count=0

while True:
	if ask_user == "yes":
		print "Enter number"
		user_number = raw_input("> ")
		user_number = int(user_number)
		while user_number >= count:
			print count
			count = count + 1


		



