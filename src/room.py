# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.contents = []

    def remove_item(self, item):
        self.contents.remove(item)

    def add_item(self, item):
        self.contents.append(item)