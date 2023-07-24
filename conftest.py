import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
        books_collector = BooksCollector()

        return books_collector
