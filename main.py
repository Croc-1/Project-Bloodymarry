
import lms.sql_util
import lms.menu
# import getpass

i = 0

# ------Login-------
# lms.log.log_initiator()
# lms.log.logit("Login Started")


while i < 3:
    ask_name = input("Enter your name ").title().strip()
    ask_pass = input("Enter your password ")
    check_data = (ask_name, ask_pass)
    # ---passwords retrieval
    if lms.sql_util.pass_checker(check_data) is False:
        print(" Invalid user, wrong password or name\nplease try again or register as a new user")
        i += 1
        print(f"you have {3 - i if 3 - i != 0 else exit()} tries")
        # lms.log.logit(message='Login Failed')
    else:
        break


# lms.log.logit(message='Logged in!')

# Body of the program
# noinspection PyUnboundLocalVariable
lms.menu.menu(user=ask_name)
while True:
    ask_option = input(" ==> ").strip().casefold()

    if ask_option in ['browse', '1']:
        # display all the isbn details and the books by them
        lms.sql_util.display(table_name='books')
        # ls.logit('displaying the books')

    elif ask_option in ['search', 'find', '2']:
        search_options = input("""
        SEARCH mode
        search by -- ISBN(isbn), author(author) or name(name)
        -> """).strip().casefold()

        if search_options in ['isbn', '1']:
            # searching the book using the books ISBN
            ask_isbn = input("Enter the ISBN number of the book ")
            # filtering the input
            if ask_isbn.isnumeric():
                lms.sql_util.search_on_isbn(ask_isbn)
            else:
                print("please enter a valid ISBN number")
            # ls.logit('searching for a book by its ISBN')

        elif search_options in ['author', '2']:
            # searching using the author name
            ask_author = input("Enter the author to search ").title().strip()

            lms.sql_util.search_on_author(ask_author)

        elif search_options in ['name', 'book name', '3']:
            # searching using the books name
            ask_title = input("Enter the Title of the book ").strip()

            lms.sql_util.search_on_title(ask_title)

    elif ask_option in ['add', 'contribute', 'add books']:
        # adding the books by the user as a contribution
        print("To Add books you have to verify that it's you!")
        verify_user = input("Please enter your name ").strip().title()
        verify_pass = input("verify your password ")
        # using the add_books function of the  sql_util package to
        lms.sql_util.add_books((verify_user, verify_pass))

    elif ask_option in ['menu', 'options']:
        # menu
        lms.menu.menu()

    elif ask_option in ['help', 'save me']:
        # help regarding options
        lms.menu.helpme()

    elif ask_option in ['explore', '4']:
        # explore for the library books

        lms.sql_util.explore()

    elif ask_option in ['exit', 'quit', '5', 'close']:
        print("Exiting the program")
        exit()

    elif ask_option in ['version']:
        lms.menu.version()

    else:
        print("I don't recognise that need help type help or menu")

#  using the logit function from lms.log  print(ls.logit("resenting by the user"))
