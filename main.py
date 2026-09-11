"""A program to demonstrate the concepts covered in this activity.
"""
from library_item.library_item import LibraryItem
from library_item.genre import Genre

__author__ = "Amarveer Singh Dhaliwal"
__version__ = "1.0"

def main() -> None:
    """The main entry point to the program."""
    #class instance
    book = LibraryItem(34535, "The Origin of Species", "Charles Darwin",
                               Genre.NON_FICTION, True)
    #accessors
    print(book.item_id)
    print(book.title)
    print(book.author)
    print(book.genre)
    print(book.is_borrowed)
    

    #class instance with invalid inputs
    try:
        book_2 = LibraryItem(347, "1984", "", Genre.FICTION, True)
    except ValueError as exception: 
        print(exception)

if __name__ == "__main__":
    main()
