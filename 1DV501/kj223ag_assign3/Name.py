from dataclasses import dataclass  # import dataclass from dataclasses


# initialize a class
@dataclass
class Name:
    # set default (empty) variables
    first_name: str = ''
    last_name: str = ''

    # return first and last name
    def to_string(self):
        return f"{self.first_name} {self.last_name}"

    # return first name as a string
    def get_first(self):
        return (f"{self.first_name}")

    # return last name as a string
    def get_last(self):
        return (f"{self.last_name}")

    # set first name by passing a new value
    def set_first(self, first_name):
        self.first_name = first_name

    # set last name by passing a new value
    def set_last(self, last_name):
        self.last_name = last_name

    # return the shortend version of the name
    def get_short_name(self):
        return f"{self.first_name[0]}. {''.join([self.last_name[i] for i in range(4)])}"
