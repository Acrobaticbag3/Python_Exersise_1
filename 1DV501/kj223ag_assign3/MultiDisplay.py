from dataclasses import dataclass


@dataclass
class MultiDisplay:
    word: str = ''
    count: int = 0

    def set_message(self, message):
        self.message = message

    def set_count(self, count):
        self.count = count

    def set_display(self, message, count):
        self.message = message
        self.count = count

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def display(self):
        for _ in range(self.count):
            print(self.message)

    def get_message(self):
        return self.message
