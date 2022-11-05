"""
mysql user credentials
"""
import os
import yaml
import mysql.connector
import random

USER_TABLE = 'lms_users'
BOOKS_TABLE = 'books'
DEBUG_TABLE = 'test_books'
ISSUE_TABLE = 'issue_list'


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
    cursor.execute(f"SELECT book_name, published, author from {BOOKS_TABLE} where book_name like {book_name+'%'!r}")
    data = cursor.fetchall()
    if data:
        print("Found")
        for books in data:
            print(f"{books[0]:40} {books[1]}, by {books[2]}")

        return True
    else:
        print(f"Not Found with title {book_name!r}")
        return False


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


def book_issue_updater():
    """
    function for making updates to the issue database
    :return:
    """

    # cnx = main_cnx()
    # cursor = cnx.cursor()

    ask_book = input("Enter the book to update its issue record ")
    var = search_on_title(ask_book)

    if var:
        pass
    # update the database using suitable details


def book_issue_maker():
    """
    making the book issue entry into the database
    :return:
    """
    cnx = main_cnx()
    cursor = cnx.cursor()

    ask_issue_book = input("Enter the issue book ")
    value = search_on_title(ask_issue_book)
    ask_add = input(f"Add {ask_issue_book!r} to issue list")
    if value and ask_add in ['yes', 'y', 'yep']:
        cursor.execute("")
    else:
        print(f'issue addition aborted for the book {ask_issue_book}')


def explore():
    """
    exploring the data
    :return:
    """

    cnx = main_cnx()

    cursor = cnx.cursor()

    # getting data for the author
    cursor.execute(f"select author from {BOOKS_TABLE}")
    author = cursor.fetchall()

    # getting the number of books in the database
    cursor.execute(f'select count(*) from {BOOKS_TABLE}')
    times = cursor.fetchall()

    # getting the old books in database
    cursor.execute(f'select book_name, author from {BOOKS_TABLE} where published < 2000 ')
    old = cursor.fetchall()

    # processing the retried values
    classic_time = random.randint(0, len(old) - 1)
    random_author = author[random.randint(0, len(author) - 1)][0]
    classic_book = old[classic_time][0]
    classic_author = old[classic_time][1]
    total_books = times[0][0]

    print(fr"""
    +{'-' * 30}LIBRARY MANAGEMENT SYSTEM{'-' * 30}+
    |{" "*85}|
    |   Read `By Authors like{" "*61}|    
    |   {random_author}{" "*(91 - (8 + 1 + len(random_author)))}|                          
    |   ```````  Total books in library {total_books} ```````{" "*(91- (49+len(str(total_books))))}|
    |   ~Time less classics{" "*63}|
    |   {classic_book}     by' {classic_author}{" "*(91 - (17+1+len(classic_author)+len(classic_book)))}|
    |{" "*85}|
    +{'-' * 30}{'*' * 25}{'-' * 30}+
        """)
