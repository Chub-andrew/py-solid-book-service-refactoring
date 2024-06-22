from abc import ABC, abstractmethod
import json
import dicttoxml


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        book_data = {"title": title, "content": content}
        return dicttoxml.dicttoxml(
            book_data,
            custom_root="book",
            attr_type=False).decode("utf-8")
