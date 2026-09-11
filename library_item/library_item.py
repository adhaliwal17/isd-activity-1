from  library_item.genre import Genre

class LibraryItem:
    def __init__(self, item_id: int, title: str, author: str, genre: Genre,
                 is_borrowed: bool):
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed

        #item_id error check
        
        digits = []
        for digit in str(item_id):
            digits.append(digit)
        if len(digits) < 4 or item_id < 0:
            raise ValueError("Item ID must be a positive value with a minimum" \
            " of four digits.")

        #title error check
        if title == "":
            raise ValueError("Title cannot be an empty string.")

        #author error check
        if author == "":
            raise ValueError("Author cannot be an empty string.")

    @property
    def item_id(self) -> int:
        return self.__item_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def genre(self) -> Genre:
        return self.__genre

    @property
    def is_borrowed(self) -> bool:
        return self.__is_borrowed

    def __str__(self):
        if self.__is_borrowed is True:
            availability = "Borrowed"
        else:
            availability = "Available"
        return(f"Item ID: {self.__item_id}\n"
               f"STATUS: {availability}")

    

    
    

