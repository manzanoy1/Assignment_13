#Yanira Manzano
#04/30/2020
#Assignment 13 DB:

# -creates new customers and books infomation
# -modify tables
# -print the contents of the table
# -delete from that table
# The Menu will offer those options
import sqlite3
from sqlite3 import Error
#Connection script
def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        
    return conn

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#The table is being created in the customers menu option
print("Connect to SQLite database:")
connection = create_connection("Assignment13")

create_customers_table = """
CREATE TABLE IF NOT EXISTS customers (
  customer_id       INT  NOT NULL   UNIQUE ,
  first_name        TEXT NOT NULL,
  last_name         TEXT NOT NULL,
  street_adress     VARCHAR(100),
  city              VARCHAR(85),
  state             VARCHAR(30),
  zip               INT
  
  age INTEGER
);
"""
#The table is being created in the books menu option
create_books_table = """
CREATE TABLE IF NOT EXISTS books (
  book_id           INT NOT NULL UNIQUE,
  title             VARCHAR(30),
  author            VARCHAR(50),
  ISBN              INT,
  edition           INT,
  price             DECIMAL(2),
  publisher         VARCHAR(25)
);
"""
#Connection for both tables
execute_query(connection, create_customers_table)
execute_query(connection, create_books_table)

#This is where the program will being with the tables that are created: Customers and Books
while True:
    menu = int(input("Main menu:\n\t1. Customers \n\t2. Books \n\t3. Exit Program\n>>>"))

    if menu == 1:
        while True:
            customers_menu = int(input("Customers menu:\n\t1. Add a new customer"
                                       "\n\t2. Modify an existing customer"
                                       "\n\t3. Print a list of all customers"
                                       "\n\t4. Delete a customer"
                                       "\n\t5. Return to main menu\n>>>"))



            if customers_menu == 1:
                new_customer = input("Enter all information about a new customer!\nUse the following format:"
                                     "\ncustomer_id, first_name, last_name, street_adress, city, state, zip\n>>>")
                add_new_customer = f"""
                INSERT INTO customers 
                VALUES ({new_customer})
                """
                execute_query(connection, add_new_customer)

            elif customers_menu == 2:
                customer_updated = int(input("Enter the customer_id that you want to update!\n>>>"))
                info_updated = input("Now enter the information you want to update!\nUse the following format:"
                                     "\n customer_id = 7, first_name = 'Tom' ...\n>>>")

                modify_customer = f"""
                UPDATE customers 
                SET {info_updated}
                WHERE customer_id = {customer_updated}
                """
                execute_query(connection, modify_customer)

            elif customers_menu == 3:
                list_of_customers = """
                SELECT customer_id, first_name, last_name
                FROM customers
                """

                lists = execute_read_query(connection, list_of_customers)
                for list in lists:
                    print(list)

            elif customers_menu == 4:
                farewell = int(input("Enter the customer's customer_id that you want to delete\n>>>"))
                delete_customers = f"""
                DELETE FROM customers
                WHERE customer_id = {farewell}"""

                execute_query(connection, delete_customers)

            elif customers_menu == 5:
                break



    elif menu == 2:

        while True:

            books_menu = int(input("Customers menu:\n\t1. Add a new book"
                                       "\n\t2. Modify an existing book"
                                       "\n\t3. Print a list of all books"
                                       "\n\t4. Delete a book"
                                   "\n\t5. Return to main menu\n>>>"))

            if books_menu == 1:
                new_book = input("Enter all information about a new book in the following sequence:"
                                     "\nbook_id, title, author, ISBN, edition, price, publisher\n>>>")
                add_new_book = f"""
                INSERT INTO books
                VALUES ({new_book})
                """
                execute_query(connection, add_new_book)

            elif books_menu == 2:
                book_updated = int(input("Enter the book_id that you want to update!\n>>>"))
                info_updated = input("Now enter the information you want to update!\nUse the following format:"
                                     "\n book_id = 3, author = 'Hemingway' ...\n>>>")

                modify_book = f"""
                UPDATE books
                SET {info_updated}
                WHERE book_id = {book_updated}
                """
                execute_query(connection, modify_book)

            elif books_menu == 3:
                list_of_books = """
                SELECT book_id, title, author2
                FROM books
                """

                lists = execute_read_query(connection, list_of_books)
                for list in lists:
                    print(list)

            elif books_menu == 4:
                farewell = int(input("Enter the book's book_id that you want to delete\n>>>"))
                delete_books = f"""
                DELETE FROM books
                WHERE book_id = {farewell}"""

                execute_query(connection, delete_books)

            elif books_menu == 5:
                break


    elif menu == 3:
        print("Bye")
        break
    else:
        print("Invalid option:>>>")
