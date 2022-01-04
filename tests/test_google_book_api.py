from google_book_api import __version__
from google_book_api.book_finder import pick_book, get_books

def test_version():
    assert __version__ == '0.1.0'

def test_result_amount():
    assert len(get_books('food')) == 5
    assert len(get_books(1)) == 5

def test_get_books():
    assert get_books('saddasdwsaddasdw') == None
    assert get_books('') == None
