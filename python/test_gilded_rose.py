# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_food(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(1, gilded_rose.items[0].quality)

    def test_weapon(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", gilded_rose.items[0].name)
        self.assertEqual(80, gilded_rose.items[0].quality)

    def test_ticket(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)]
        gilded_rose = GildedRose(items)

        for _ in range(3):
            gilded_rose.update_quality()

        self.assertEqual(
            "Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name
        )
        self.assertEqual(11, gilded_rose.items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(3):
            gilded_rose.update_quality()
        self.assertEqual("Conjured", gilded_rose.items[0].name)
        self.assertEqual(4, gilded_rose.items[0].quality)


if __name__ == "__main__":
    unittest.main()
