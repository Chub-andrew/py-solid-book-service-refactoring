from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    def print_book(self, title: str, content: str) -> None:
        print(f"{title}")
        print(content)


class ReversePrint(Print):
    def print_book(self, title: str, content: str) -> None:
        print(f"{title}")
        print(content[::-1])
