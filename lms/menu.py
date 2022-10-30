"""
menu, options and help for the file:main.py
"""


def menu(user=''):
    print(f"""
   +{'-'*60}+
   |            Library Management System                       |
   | Hi {user}
   |    1.Browse books (browse)                                 |
   |    2.Search for the book (find)                            |
   |    3.Add Books (add)                                       |
        4.Explore (explore)
   |    5.exit (exit)                                           |
   +{'-'*60}+
   | For help enter help, for version information enter version |
   +{'-'*60}+
    """)


def helpme():
    print("""
    USER HELP
    
    *browse*
    Browse helps the user to browse the extensive catalog of books from
    the LMS database.
    
    Search
    search comprises of the multiple type of search in the books database
    this options has 3 sub options inside it 
        1.ISBN search
        2.Author search
        3.Search by Title of the Book
        
    *add*
    Add is a option for people who want to add data to the database for making
    new books in the library catalog
    
    *help*
    gets you here
    
    for version information enter version 
    """)


def version():
    print("""
    version information '0.5' 'Bloodymary'
    """)
