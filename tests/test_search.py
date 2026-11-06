import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

        self.cart.add_dvd(
            DigitalVideoDisc("The Lion King", "Animation", cost=20)
        )
        self.cart.add_dvd(
            DigitalVideoDisc("Star Wars", "Science Fiction", cost=25)
        )
        self.cart.add_dvd(
            DigitalVideoDisc("Aladdin", "Animation", cost=15)
        )

    def test_search_by_category(self):
        results = search_by_category(self.cart, "Animation")

        self.assertEqual(
            [dvd.title for dvd in results],
            ["The Lion King", "Aladdin"]
        )

    def test_search_by_category_case_insensitive(self):
        results = search_by_category(self.cart, "animation")

        self.assertEqual(len(results), 2)

    def test_search_by_category_not_found(self):
        results = search_by_category(self.cart, "Comedy")

        self.assertEqual(len(results), 0)

    def test_search_by_title(self):
        results = search_by_title(self.cart, "lion")

        self.assertEqual(
            [dvd.title for dvd in results],
            ["The Lion King"]
        )


if __name__ == "__main__":
    unittest.main()