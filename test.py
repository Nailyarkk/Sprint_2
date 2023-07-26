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
        assert books_collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre', [
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_book_genre_not_none(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) is not None, 'жанры пусты'

    @pytest.mark.parametrize(
            'name, genre', [
                ['Дюна', 'Фантастика'],
                ['Душа', 'Мультфильмы'],
                ['Моана', 'Мультфильмы'],
                ['Какой-то ужастик', 'Ужасы'],
                ['Русалочка', 'Мультфильмы']
            ]
        )
    def test_get_book_genre_positive_case(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert 'Моана' or 'Русалочка' in books_collector.get_book_genre(name)


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
    def test_get_books_for_children_positive_case(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert 'Русалочка' or 'Моана' in books_collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name, genre', [
            ['Дюна', 'Фантастика'],
            ['Какой-то ужастик', 'Ужасы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_negative_case(self, books_collector, name, genre):
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

        assert name in books_collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'name, genre', [
            ['Моана', 'Мультфильмы']
        ]
    )
    def test_add_book_in_favorites_сount_1(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        count = len(books_collector.get_list_of_favorites_books())

        assert count == 1, 'В favorites списке больше 1 книги'

    @pytest.mark.parametrize(
        'name, genre', [
            ['Моана', 'Мультфильмы'],
            ['Русалочка', 'Мультфильмы']
        ]
    )
    def test_delete_book_from_favorites(self,books_collector,name,genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)

        assert name not in books_collector.get_list_of_favorites_books(), 'Моана имеется в списке favorites книг '

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

        assert 'Моана' or 'Русалочка' in books_collector.get_list_of_favorites_books(), 'Имеется пустое значение'