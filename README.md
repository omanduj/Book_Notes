Google Book API
=======

What you'll see
-----------
This project creates a command line tool that allows users to create query books located on the google API. They are
then able to select the returned books and create a personal reading list. The reading list is returned at the end of
every book being added.


How to Run
-----------

In order to properly run this project you must first install Poetry, a tool used for dependency management and
packaging in Python. A link to the installation documents can be found here:
>https://python-poetry.org/docs/

Following installation run the command "poetry shell" to create a virtual environment and "poetry install", this will
install all the project's dependencies.

In order to run the application, you must execute the following command in the appropriate directory on the command line
(google_book_api/google_book_api):
>python book_finder.py xxx

 Replace 'xxx' with the subject or title of book being searched for.

This will display 5 books that are found in the google API book service, allowing the user to add books with the given
name to their personal book list. After adding a book to the book list, all books are shown to the user that are on
their list.

In order to run the tests simply enter the appropriate directory (google_book_api) and run pytest while within the
virtual environment.
