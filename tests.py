from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_default_rating_of_the_new_book_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_each_book_can_be_added_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Как захватить мир с помощью вилки')
        collector.add_new_book('Как захватить мир с помощью вилки')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_cant_set_rating_to_book_not_in_books_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Методика оказания первой помощи при скуке', 1)
        assert collector.get_book_rating('Методика оказания первой помощи при скуке') != 1

    def test_set_book_rating_cant_set_rating_less_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Актуальные проблемы натягивания совы на глобус')
        collector.set_book_rating('Актуальные проблемы натягивания совы на глобус', 0)
        assert collector.books_rating['Актуальные проблемы натягивания совы на глобус'] != 0

    def test_set_book_rating_cant_set_rating_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book('Что страшнее: 1 пожар или 2 переезда? Делимся опытом')
        collector.set_book_rating('Что страшнее: 1 пожар или 2 переезда? Делимся опытом', 15)
        assert collector.books_rating['Что страшнее: 1 пожар или 2 переезда? Делимся опытом'] != 15

    def test_get_book_rating_the_book_not_in_books_rating_have_no_rating(self):
        collector = BooksCollector()
        collector.get_book_rating('Переворот в мозгах')
        assert collector.get_book_rating('Переворот в мозгах') == None

    def test_add_book_in_favorites_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ахр рахр. Рыынн. (Чубакка. Автобиография)')
        collector.add_book_in_favorites('Ахр рахр. Рыынн. (Чубакка. Автобиография)')
        a = 'Ахр рахр. Рыынн. (Чубакка. Автобиография)' in collector.favorites
        assert a == True

    def test_add_book_in_favorites_cant_add_book_if_it_is_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Космос в стакане')
        a = 'Космос в стакане' in collector.favorites
        assert a == False

    def test_delete_book_from_favorites_del_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пляжи в Антарктиде. Краткий путеводитель туриста')
        collector.add_book_in_favorites('Пляжи в Антарктиде. Краткий путеводитель туриста')
        collector.favorites.remove('Пляжи в Антарктиде. Краткий путеводитель туриста')
        a = 'Пляжи в Антарктиде. Краткий путеводитель туриста' in collector.favorites
        assert a == False












