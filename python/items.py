"""
items.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Provide wrapper classes for different types of items
    that handle specific behavior for updating quality.
"""


class Default:
    """Represents the default behavior for items."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in >= 0:
            self.quality = max(0, self.quality - 1)

        else:
            self.quality = max(0, self.quality - 2)


class Food:
    """Represents comestibles that appreciate over time."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = min(self.quality + 1, 50)


class Weapon:
    """Represents weapons such as Sulfuras that never fluctuate in value."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        pass


class Ticket:
    """Represents tickets that appreciate until the event."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0

        elif self.sell_in <= 5:
            self.quality = min(50, self.quality + 3)

        elif self.sell_in <= 10:
            self.quality = min(50, self.quality + 2)

        else:
            self.quality = min(50, self.quality + 1)


class Conjured:
    """Represents conjured items that depreciate twice as fast as default items."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = max(0, self.quality - 2)
