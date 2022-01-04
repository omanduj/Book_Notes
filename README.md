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

 Replace 'xxx' with the subject or title of the book being searched for.

This will display 5 books that are found in the google API book service, allowing the user to add books with the given
name to their personal book list. After adding a book to the book list, all books are shown to the user that are on
their list.

In order to run the tests simply enter the appropriate directory (google_book_api) and run pytest while within the
virtual environment.

Notes
-------

A few edge cases are handled by simply notifying the user that inputs are invalid, for example if '' is used the
function will run but when told to add a book the program will print 'No Books Found'. When working on numbers and
emojis as edge cases, I found that the google api was able to handle these queries and respond with books.

In order to improve user experience when selecting books, I altered the program to allow users to input a number
corresponding to a book in order to add it to their reading list as opposed to typing the entire name of the book.

In order to view the reading list of the user you must first run the program and then will be prompted with a menu
that has options to add a book, see current book list or to exit. If you add a book, by default it will print an up to
date book list. This new edit also allows the program to run until the user is finished adding books with a given
subject.

I used parameters to run the program in order to allow for scalability. I view a possible expansion for the project
is to have a file full of book titles to search for. Altering the code to take in said file and parse the titles into
the current code would be quick and easy.
