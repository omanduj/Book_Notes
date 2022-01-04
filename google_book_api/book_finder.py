from google_book_api.database import base_set_up, insert_book, select_all_books
import requests
import json
import typer

app = typer.Typer()


class Book:
    def __init__(self, name: str, authors: list, publisher: str):
        self.name = name
        self.authors = authors
        self.publisher = publisher


def get_books(query_name: str):
    """Purpose: To create a query with the given subject provided by user, limiting results by 5
    Paramaters: query_name = String of subject to be searched for
    Return Value: data = A list of books matching the query
    """
    if query_name != None:
        response = requests.get(
            "https://books.googleapis.com/books/v1/volumes?q={}&maxResults=5&fields=items(volumeInfo/authors,volumeInfo/title,volumeInfo/publisher)".format(
                query_name
            )
        )

        try:
            data = response.json()["items"]
            return data
        except:
            print("No Books Found")
    else:
        return "Please input valid query string"


def format_info(query_info: dict):
    """Purpose: To clean data for ease of future use
    Paramaters: query_info = A list of dictionaries, each containing information on a book
    Return Value: query_dict = A dictionary containing Book objects
    """
    query_dict = {}
    count = 0
    if query_info != None:
        for book in range(len(query_info)):
            count += 1
            book_info = query_info[book]["volumeInfo"]
            book_title = book_info["title"].lower()
            try:
                query_dict[count] = Book(
                    book_info["title"], book_info["authors"], book_info["publisher"]
                )
            except:
                query_dict[count] = Book(
                    book_info["title"], book_info["authors"], "N/a"
                )
        return query_dict
    return


def parse_info(all_book_info: dict):
    """Purpose: To grammatically fix book information if there are 2+ authors
    Paramaters: all_book_info = A dictionary of book objects
    Return Value: all_book_info = A dictionary of book objects whose author value is grammatically correct
    """
    if all_book_info != None:
        for book_info in all_book_info.values():
            if len(book_info.authors) >= 2:
                authors = ""
                for author in book_info.authors:
                    if author != book_info.authors[-1]:
                        authors += author + " and "
                    if author == book_info.authors[-1]:
                        authors += author
                book_info.authors = [authors]
        return all_book_info
    return None


def print_options(all_book_info: dict):
    """Purpose: To show user all valid books matching a query (limited to 5)
    Paramaters: all_book_info = A dictionary of book objects
    Return Value: N/a
    """
    if all_book_info != None:
        for number, book_info in all_book_info.items():
            author = book_info.authors[0]
            print(
                number,
                ") Name: ",
                book_info.name,
                "|",
                "Author(s):",
                author,
                "|",
                "Publisher:",
                book_info.publisher,
                "\n",
            )


def pick_book(all_book_info: dict):
    """Purpose: User is able to pick a book in a list that will be added to their personal book list
    Paramaters: all_book_info = A dictionary of book objects
    Return Value: wanted_book = If input is valid, it will return the book desired by user
                    -1 = If the input is not valid
    """
    search_book = int(input("Insert desired book title: "))
    if search_book in all_book_info.keys():
        wanted_book = all_book_info[search_book]
        return wanted_book
    else:
        print("Please input valid book")
        return -1


def insert_reading_list(wanted_book: object):
    """Purpose: To insert the desired book to a personal book list
    Paramaters: wanted_book = A book object that contains all relevant information
    Return Value: N/a
    """
    base_set_up()
    my_collection = select_all_books()
    book_names = []

    if my_collection == []:
        wanted_book.authors = wanted_book.authors[0]
        insert_book(wanted_book.name, wanted_book.authors, wanted_book.publisher)
        print("Book inserted!")
    else:
        for book in my_collection:
            book_names.append(book[0])
        if wanted_book.name in book_names:
            print("Book already in collection!")
        if wanted_book.name not in book_names:
            wanted_book.authors = wanted_book.authors[0]
            insert_book(wanted_book.name, wanted_book.authors, wanted_book.publisher)
            print("Book inserted!")


def get_reading_list():
    """Purpose: To show all books in the users book list
    Paramaters: N/a
    Return Value: my_books = A list of all books in the users book list
    """
    my_books = select_all_books()
    print()
    print("Here is your reading list: ")
    for book in my_books:
        print(
            "Book Name:",
            book[0],
            "|",
            "Author(s):",
            book[1],
            "|",
            "Publisher:",
            book[2],
        )

    return my_books


@app.command()
def main(query: str):
    """Purpose: To execute the program as a Command Line Interface (CLI), allowing users to perform queries
                on Google Book API and create a personal list of desired books.
    Paramaters: query = A string that user inputs as query
    Return Value: N/a
    """
    val = 0
    while val <= 2:
        val = int(
            input(
                "Press 1 to add a book | 2 to read current book list | Any other button to exit: "
            )
        )
        if val == 1:
            query_info = get_books(query)
            all_book_info = format_info(query_info)
            all_book_info = parse_info(all_book_info)
            books = print_options(all_book_info)
            if all_book_info != None:
                wanted_book = pick_book(all_book_info)
                if wanted_book != -1:
                    insert_reading_list(wanted_book)
                my_books = get_reading_list()
        if val == 2:
            try:
                get_reading_list()
            except:
                print("No Books Found")
                


if __name__ == "__main__":
    app()
