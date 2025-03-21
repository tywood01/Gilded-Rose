"""
gilded_rose.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Gilded Rose Exersise for practicing refactoring code.
"""

# -*- coding: utf-8 -*-
from items import Default, Food, Weapon, Ticket, Conjured


class GildedRose(object):
    """
    This represents our small inn where we maintain a
    registry of available items to sell and update our
    prices on a daily basis.
    """

    item_registry = {
        "Aged Brie": Food,
        "Backstage passes to a TAFKAL80ETC concert": Ticket,
        "Sulfuras, Hand of Ragnaros": Weapon,
        "Conjured": Conjured,
    }

    def __init__(self, items):
        self.items = [self.wrap_item(item) for item in items]

    def wrap_item(self, item):
        """This adapts our regular item object using a specified class."""

        item_class = self.item_registry.get(item.name, Default)
        return item_class(item.name, item.sell_in, item.quality)

    def update_quality(self):
        """Update the quality of all the inn's items."""

        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
