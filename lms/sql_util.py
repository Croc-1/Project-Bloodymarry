"""
mysql user credentials
"""
import os
import yaml
import mysql.connector

USER_TABLE = 'lms_users'
BOOKS_TABLE = 'books'
DEBUG_TABLE = 'test_books'


def main_cnx(user_id='user'):
    """
    function that returns the login connection using the
    cnx_data.yml file
    """
    # changing to the data directory
    if os.path.exists('cnx_data.yml') is False:
        # os.chdir('..')
        os.chdir('data')
    with open('cnx_data.yml') as data_file:
        data = yaml.load(data_file, yaml.SafeLoader)

    cnx = mysql.connector.connect(**data[user_id])
    return cnx


def pass_checker(user_data):
    """
    checking the user input to the registered users
    in the database
    :return: boolean value
    """
    # starting the defined connection using the main_cnx() function
    cnx = main_cnx()

    cursor = cnx.cursor()
    # executing the command using execute statement

    cursor.execute(f'select * from {USER_TABLE}')
    # getting the data in the desired form
    database_data = cursor.fetchall()

    # checking the database from the file data
    if user_data in database_data:
        return True
    else:
        return False


def display(table_name='books'):
    """
    show the books, isbn author from the database
    :param table_name:
    :return:
    """
    # initiating the connection
    cnx = main_cnx()
    cursor = cnx.cursor()

    # executing the sql statement for the data
    cursor.execute(f"select * from {table_name}")

    # printing the data form stored in the cursor
    for lines in cursor:
        print(f'{lines[0]:14} {lines[1]:45}by {lines[2]}')
    # ##############tmp##########################
    '''fix this out of index is done in following function search_isbn'''


def search_on_isbn(isbn_number: str):
    """
    searching using the isbn of the book
    :return:
    """
    cnx = main_cnx()
    cursor = cnx.cursor()
    if isbn_number.isnumeric():
        cursor.execute(f"select * from {BOOKS_TABLE} where isbn = {isbn_number!r}")
        # fetching the data from the database
        data = cursor.fetchall()
        # checking for empty data
        if not data:
            print(f"Sorry no book is found having ISBN {isbn_number}")
        else:
            print('Found')
            print(data)
    else:
        print("Please enter a number to search")


def search_on_author(author_name: str):
    """
    searching function using the author name
    :return:
    """

    cnx = main_cnx()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT book_name, published from {BOOKS_TABLE} where author = {author_name!r}")
    data = cursor.fetchall()
    # printing the data retrieved from database
    # listing of the all the books from the author
    if data:
        print(f"Books by {author_name}")
        print(f"Title {'-'*35}Publishing date")
        for books in data:
            print(f"{books[0]:40} {books[1]:5}")
    else:
        print(f"Author {author_name!r} not found\nPlease check for any typos in the author name and try again")


def search_on_title(book_name: str):
    """
    searching the books in the database using the
    :param book_name:
    :return:
    """

    cnx = main_cnx()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT book_name, published, author from {BOOKS_TABLE} where book_name = {book_name!r}")
    data = cursor.fetchall()
    if data:
        print("Found")
        for books in data:
            print(f"{books[0]:40} {books[1]}, by {books[2]}")
    else:
        print(f"Not Found with title {book_name!r}")


def add_books(verify_user):
    """
    Adding the books by the user as a contribution to the project database
    helping it to grow to a more vast book library
    :param verify_user:
    :return:
    """
    if pass_checker(verify_user) is False:
        print("Sorry the credentials are wrong")
    else:
        cnx = main_cnx()
        # making the cursor
        cursor = cnx.cursor()
        # asking the details of the books by the valid user
        while True:
            try:
                print("Enter the following details of the book exit to leave \n")
                ask_isbn = input("Enter the isbn number ").strip().casefold()
                if ask_isbn in ['exit', 'quit']:
                    break
                ask_book_name = input("Enter the book name ").strip()
                ask_author = input(f"Enter the Author of the book {ask_book_name!r} ").title().strip()
                ask_year = input("Enter the year of publishing ")
                # if no exception occurs break the loop
                # ------tmp-----##
                cursor.execute(f"insert into {DEBUG_TABLE} values ({ask_isbn!r}, {ask_book_name!r}, {ask_author!r},"
                               f" {ask_year})")
                # executing the changes to the table
                cnx.commit()
                print("*Successfully* added the book to the library thanks for the contribution \n"
                      "help this project to grow.\n")

            except (mysql.connector.errors.DatabaseError, mysql.connector.errors.InterfaceError):
                print(f" {'*'*9}SORRY! there was an error, sorry for the inconvenience {'*'*9}")
                print(f"{'*'*9}Please enter a number value for the publishing year{'*'*9}")
