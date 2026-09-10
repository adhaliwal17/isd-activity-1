import unittest
from library_item.genre import Genre

__author__ = "Amarveer Singh Dhaliwal"
__version__ = "1.0"

class TestGenre(unittest.TestCase):

    def test_enumeration_values_initialization(self):

        self.assertEqual(100, Genre.FICTION.value)
        self.assertEqual(200, Genre.NON_FICTION.value)
        self.assertEqual(300, Genre.FANTASY.value)
        self.assertEqual(400, Genre.TRUE_CRIME.value)

if __name__ == "__main__":
    unittest.main()
