from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialize_strategies = {
        "json": JSONSerialize(),
        "xml": XMLSerialize()
    }

    def display_command(book: Book, method_type: str) -> None:
        strategy = display_strategies.get(method_type)
        if strategy:
            strategy.display(book.content)
        else:
            raise ValueError(f"Unknown display type: {method_type}")

    def print_command(book: Book, method_type: str) -> None:
        strategy = print_strategies.get(method_type)
        if strategy:
            strategy.print_book(book.title, book.content)
        else:
            raise ValueError(f"Unknown print type: {method_type}")

    def serialize_command(book: Book, method_type: str) -> str:
        strategy = serialize_strategies.get(method_type)
        if strategy:
            return strategy.serialize(book.title, book.content)
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")

    for cmd, method_type in commands:
        if cmd == "display":
            display_command(book, method_type)
        elif cmd == "print":
            print_command(book, method_type)
        elif cmd == "serialize":
            return serialize_command(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
