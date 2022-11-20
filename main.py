"""
main program file
"""

import lms.sql_util    # main functions for the program and utilities
import lms.menu    # menu and help displaying functions
# import getpass    # password receiving function can be used in future

login_variable = 0

# ------Login-------
ask_name = None

while login_variable < 3:
    ask_name = input("Enter your name ").title().strip()
    ask_pass = input("Enter your password ")
    check_data = (ask_name, ask_pass)
    # ---passwords retrieval
    if lms.sql_util.pass_checker(check_data) is False:
        print(" Invalid user, wrong password or name\nplease try again or register as a new user")
        login_variable += 1
        print(f"you have {3 - login_variable if 3 - login_variable != 0 else exit()} tries")
        lms.sql_util.logit(message='Login Failed')
    else:
        # if the user is found in the database of the users
        break


lms.sql_util.logit(message='Logged in!')

lms.sql_util.clear()    # for clearing the screen
# Body of the program
lms.menu.menu(user=ask_name)
while True:
    ask_option = input(" ==> ").strip().casefold()

    if ask_option in ['browse', '1']:
        # display all the isbn details and the books by them
        lms.sql_util.display(table_name='books')
        lms.sql_util.logit('displaying the books')

    elif ask_option in ['search', 'find', '2']:
        # search options for more exact searching of the books in
        # the books cataloging
        search_options = input("""
        SEARCH mode
        search by -- ISBN(isbn), author(author) or name(name)
        -> """).strip().casefold()

        if search_options in ['isbn', '1']:
            # searching the book using the books ISBN
            ask_isbn = input("Enter the ISBN number of the book ")
            # filtering the input so that only numbers get into the
            # sql input query
            if ask_isbn.isnumeric():
                lms.sql_util.search_on_isbn(ask_isbn)
            else:
                print("please enter a valid ISBN number")
            lms.sql_util.logit('searching for a book by its ISBN')

        elif search_options in ['author', '2']:
            # searching using the author name
            ask_author = input("Enter the author to search ").title().strip()

            lms.sql_util.search_on_author(ask_author)
            lms.sql_util.logit("Searching on the basis of author ")

        elif search_options in ['name', 'book name', 'title', '3']:
            # searching using the books name
            ask_title = input("Enter the Title of the book ").strip()

            lms.sql_util.search_on_title(ask_title)
            lms.sql_util.logit("searching for a book by title")

    elif ask_option in ['add', 'contribute', 'add books']:
        # adding the books by the user as a contribution
        print("To Add books you have to verify that it's you!")
        verify_user = input("Please enter your name ").strip().title()
        verify_pass = input("verify your password ")
        # using the add_books function of the  sql_util package to
        lms.sql_util.add_books((verify_user, verify_pass))
        lms.sql_util.logit('Adding to the database')

    elif ask_option in ['menu', 'options']:
        # main menu
        lms.menu.menu()

    elif ask_option in ['help', 'save me']:
        # help regarding options
        lms.menu.helpme()

    elif ask_option in ['explore', '4']:
        # explore for the library books
        lms.sql_util.explore()

    elif ask_option in ['exit', 'quit', '5', 'close']:
        # exiting the program
        print("Exiting the program")
        lms.sql_util.logit("Exiting the program ")
        exit()

    elif ask_option in ['version']:
        # program version information
        lms.menu.version()

    elif ask_option in ['clear screen', 'cls', 'clear']:
        # clearing the screen
        lms.sql_util.clear()

    else:
        # for unknown commands
        print("I don't recognize that need help type help or menu")

#  using the logit function from lms.log
#  for loging the functions happened in the program
