import unittest
from library_item.library_item import LibraryItem
from library_item.genre import Genre

__author__ = "Amarveer Singh Dhaliwal"
__version__ = "1.0"

class TestInit(unittest.TestCase):

    def test_item_id_less_than_four_digits(self) -> None:
        #Act
        with self.assertRaises(ValueError) as context:
            LibraryItem(87, "Lord of the Rings", "Tolkien", Genre.FANTASY, True)

        #Assert
        excepted = "Item ID must be a positive value with a minimum" \
            " of four digits."
        actual = str(context.exception)
        self.assertEqual(excepted, actual)


    def test_title_empty_string(self) -> None:
        #Act
        with self.assertRaises(ValueError) as context:
            LibraryItem(1200, "", "Mark", Genre.FANTASY, False)

        #Assert
        excepted = "Title cannot be an empty string."
        actual = str(context.exception)
        self.assertEqual(excepted, actual)

    def test_author_empty_string(self) -> None:
        #Act
        with self.assertRaises(ValueError) as context:
            LibraryItem(4509, "The Alchemsit", "", Genre.FICTION, False)

        #Assert
        excepted = "Author cannot be an empty string."
        actual = str(context.exception)
        self.assertEqual(excepted, actual)

    def test_initialize_new_instance(self) -> None:
        #Arrange
        item_id = 1250
        title = "The Story of My Life"
        author = "Hellen Keller"
        genre = Genre.NON_FICTION
        is_borrowed = False

        #Act
        library_item = LibraryItem(1250, "The Story of My Life", "Hellen Keller",
                                    Genre.NON_FICTION, False)

        #Assert
        self.assertEqual(1250, library_item._LibraryItem__item_id)
        self.assertEqual("The Story of My Life", library_item._LibraryItem__title)
        self.assertEqual("Hellen Keller", library_item._LibraryItem__author)
        self.assertEqual(Genre.NON_FICTION, library_item._LibraryItem__genre)
        self.assertEqual(False, library_item._LibraryItem__is_borrowed)

class TestItemIdProperty(unittest.TestCase):
    
    def test_returns_current_state(self) -> None:
        #Arrange
        item_id = 12452
        title = "A Game of Thrones"
        author = "George Martin"
        genre = Genre.FANTASY
        is_borrowed = True

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        #Act
        actual = library_item.item_id

        #Assert
        expected = item_id
        self.assertEqual(expected, actual)

class TestTitleProperty(unittest.TestCase):
    
    def test_returns_current_state(self) -> None:
        #Arrange
        item_id = 99238
        title = "The Hobbit"
        author = "Tolkien"
        genre = Genre.FANTASY
        is_borrowed = False

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        #Act
        actual = library_item.title

        #Assert
        expected = title
        self.assertEqual(expected, actual)

class TestAuthorProperty(unittest.TestCase):
    
    def test_returns_current_state(self) -> None:
        #Arrange
        item_id = 8345
        title = "1984"
        author = "George Orwell"
        genre = Genre.FICTION
        is_borrowed = True

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        #Act
        actual = library_item.author

        #Assert
        expected = author
        self.assertEqual(expected, actual)

class TestGenreProperty(unittest.TestCase):
    
    def test_returns_current_state(self) -> None:
        #Arrange
        item_id = 7689
        title = "The Diary of a Young Girl"
        author = "Anne Frank"
        genre = Genre.NON_FICTION
        is_borrowed = True

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        #Act
        actual = library_item.genre

        #Assert
        expected = genre
        self.assertEqual(expected, actual)

class TestIsBorrowedProperty(unittest.TestCase):
    
    def test_returns_current_state(self) -> None:
        #Arrange
        item_id = 6354
        title = "Harry Potter"
        author = "Rowling"
        genre = Genre.FANTASY
        is_borrowed = True

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        #Act
        actual = library_item.is_borrowed

        #Assert
        expected = is_borrowed
        self.assertEqual(expected, actual)

class TestStrMethod(unittest.TestCase):

    def test_string_representation_item_borrowed(self):
        #Arrange
        library_item = LibraryItem(6872, "To Kill a Mocking Bird", "Harper Lee",
                                   Genre.FANTASY, True)

        #Act
        actual = str(library_item)

        #Assert
        expected = "Item ID: 6872\n" \
        "STATUS: Borrowed"
        self.assertEqual(actual, expected)

    def test_string_representation_item_available(self):
        #Arrange
        library_item = LibraryItem(6872, "To Kill a Mocking Bird", "Harper Lee",
                                    Genre.FANTASY, False)

        #Act
        actual = str(library_item)

        #Assert
        expected = "Item ID: 6872\n" \
        "STATUS: Available"
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
