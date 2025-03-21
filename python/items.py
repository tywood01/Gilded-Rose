class Default:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        """Default behavior: decrease quality by 1, stop at 0"""
        self.sell_in -= 1
        if self.quality > 0:
            self.quality -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1


class Food:
    """
    This contains comestibles such as Aged Brie.
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = min(self.quality + 1, 50)


class Weapon:
    """
    This contains weapons such as Sulfuras.
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        pass


class Ticket:
    """
    This contains tickets such as backstage
    passes to a TAFKAL80ETC concert.
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in <= 0:
            self.quality = 0

        elif self.sell_in <= 5:
            self.quality = min(50, self.quality + 3)

        elif self.sell_in <= 10:
            self.quality = min(50, self.quality + 2)

        else:
            self.quality = min(50, self.quality + 1)


class Conjured:
    """
    This class contains conjured items Incendio
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = max(0, self.quality - 2)
