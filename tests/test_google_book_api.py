from google_book_api import __version__
from google_book_api.book_finder import create_query, pick_book

def test_version():
    assert __version__ == '0.1.0'

def test_result_amount():
    assert len(create_query('food')) == 5

def test_clean_data():
    assert pick_book('FoOd') == {'food': <__main__.Book object at 0x10a359d80>, 'in defence of food': <__main__.Book object at 0x10a358fa0>, 'the comic book guide to growing food': <__main__.Book object at 0x10a359090>, 'technically food': <__main__.Book object at 0x10a359300>, 'fast food genocide': <__main__.Book object at 0x10a3592d0>}
