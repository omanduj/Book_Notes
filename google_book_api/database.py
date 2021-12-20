import sqlite3


def base_set_up():
    """Purpose: To set up sqlite3 database
    Paramaters: N/a
    Return Value: N/a
    """
    conn = sqlite3.connect("my_book_list.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS my_book_list (
                id integer primary key autoincrement,
                book_name text,
                author text,
                publisher text
            ) """
    )

    conn.commit()
    conn.close()


def insert_book(book_name, author, publisher):
    """Purpose: Insert book information to database
    Paramaters: book_name = Name of a given book,
                author = Name of a given author,
                publisher = Name of a given publisher
    Return Value: N/a
    """
    conn = sqlite3.connect("my_book_list.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO my_book_list (book_name, author, publisher) VALUES (:book_name, :author, :publisher)",
        {"book_name": book_name, "author": author, "publisher": publisher},
    )

    conn.commit()
    conn.close()


def select_all_books():
    """Purpose: Insert book information to database
    Paramaters: N/a
    Return Value: N/a
    """
    conn = sqlite3.connect("my_book_list.db")
    c = conn.cursor()

    books = c.execute("SELECT book_name, author, publisher FROM my_book_list")
    books = books.fetchall()

    conn.commit()
    conn.close()
    return books
