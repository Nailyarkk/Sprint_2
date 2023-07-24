import pytest
from main import BooksCollector

class TestBooksCollectorAddBooks:

    def test_add_new_book_valid_name(self, books_collector):
        book_name= 'book'
        books_collector.add_new_book(book_name)

        assert book_name in books_collector.get_books_genre()

    def test_add_new_book_empty_name(self, books_collector):
        book_name = " "
        books_collector.add_new_book(book_name)

        assert " " in books_collector.books_genre, 'Нет пустого значения книги'

    def test_add_new_book_invalid_name(self,books_collector):
        book_name = "XYZ" * 100
        books_collector.add_new_book(book_name)

        assert book_name not in books_collector.books_genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика']
        ]
    )
    def test_set_book_genre(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_book_genre(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) is not None

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Душа', 'Мультфильмы'],
            ['Моана', 'Мультфильмы'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_with_specific_genre(self,books_collector,name,genre):
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
    def test_get_books_genre(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert 'Боевик' not in books_collector.get_book_genre(name)


    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert 'Какой-то ужастик' not in books_collector.get_books_for_children(), 'книга "Какой-то ужастик" имеется в списке книг для детей'

    @pytest.mark.parametrize(
        'name, genre', [
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_add_book_in_favorites(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        assert name in books_collector.favorites, 'Книга не добавлена в favorites список'



    def test_delete_book_from_favorites(self,books_collector):
        books_collector.add_new_book("Моана")
        books_collector.set_book_genre("Моана", "Мультфильмы")
        books_collector.add_book_in_favorites("Моана")
        books_collector.delete_book_from_favorites("Моана")

        assert "Моана" not in books_collector.favorites, 'Моана bмеется в списке favorites книг '

    @pytest.mark.parametrize(
        'name, genre', [
            ['Моана', 'Мультфильмы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_list_of_favorites_books(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        assert ' ' not in books_collector.get_list_of_favorites_books(), 'Имеется пустое значение'
