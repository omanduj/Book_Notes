How to Run
-----------

In order to properly run this project you must first install Poetry, a tool used for dependency management and
packaging in Python. A link to the installation documents can be found here:
>https://python-poetry.org/docs/

Following installation run the command "poetry install" (within the goole_book_api directory), this will install
all the project's dependencies.

In order to run the application you must simply migrate to the correct parent directory (google_book_api/
google_book_api), then execute the following command replacing XXXX with the desired input:
>python book_finder.py XXXX

ex) python book_finder.py food

 This will cause the program to run, executing queries with the topic passed in as a parameter

Design Decisions
-----------

The design decisions taken were used to increase scalability, reliability and maintainability of the program.

In regards to scalability, if the user has a desire to find search for other subjects they must simply alter
their input of the CLI. This will display 5 results that match what they are searching for. If the problem
statement were to switch to include other information (increase in results, search by author, etc), this
could be achieved simply by modifying the google api url to fit the desired scenario. The code also lends
itself to be easily added to, utilizing predefined functions to output more complex outputs. For example,
using the output of the functions lends itself to a creation of a UI if the project is to expland from a command
line application to a larger project.

Reliability was designed via precautionary steps. The usage of checking mutating the input to be all lower case
and converting causes all user input (as long as spelling is correct) to be valid when searched for in the
defined dictionary. Poetry was also used in order to track what versions of software are required to this
program function correctly.

Maintainability was emphasized via the simple coding logic and doc strings. The usage of the dictionary allows
for very quick look up times to identify the books required to complete the task. By using poetry as a
dependency manager it also shows what technologies are required for the program to run correctly.
