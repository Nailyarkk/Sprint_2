import pytest
from main import BooksCollector

class TestBooksCollectorAddBooks:
    def test_add_new_book_valid_name(self):
        books_collector = BooksCollector()
        book_name= 'book'
        books_collector.add_new_book(book_name)

        assert book_name in books_collector.books_genre

    def test_add_new_book_empty_name(self):
        books_collector = BooksCollector()
        book_name = ""
        books_collector.add_new_book(book_name)

        assert "" not in books_collector.books_genre

    def test_add_new_book_invalid_name(self):
        books_collector = BooksCollector()
        book_name = "XYZ" * 100
        books_collector.add_new_book(book_name)

        assert book_name not in books_collector.books_genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка','Мультфильмы']
        ]
    )
    def test_set_book_genre(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_book_genre(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_with_specific_genre(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name,genre)
        assert books_collector.get_books_with_specific_genre("Мультфильмы") == ["Душа"] or ["Моана"]

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_genre(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre


    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert 'Duna' or 'Душа' in books_collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_add_book_in_favorites(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        assert name in books_collector.favorites



    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Моана")
        books_collector.set_book_genre("Моана", "Мультфильмы")
        books_collector.add_book_in_favorites("Моана")
        books_collector.delete_book_from_favorites("Моана")

        assert "Моана" not in books_collector.favorites

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_list_of_favorites_books(self,name,genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        assert "Душа" or "Моана" in books_collector.get_list_of_favorites_books()
