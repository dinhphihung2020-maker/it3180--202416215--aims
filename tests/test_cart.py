import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_cart_limit(self):
        cart = Cart()

        for i in range(21):
            dvd = DigitalVideoDisc(f"DVD {i}", cost=10)
            cart.add_dvd(dvd)

        self.assertEqual(len(cart.items), 20)

    def test_add_one_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD", cost=10)

        cart.add_dvd(dvd)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0], dvd)

    def test_sort_by_title(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Star Wars", cost=20)
        dvd2 = DigitalVideoDisc("Aladdin", cost=15)
        dvd3 = DigitalVideoDisc("The Lion King", cost=25)

        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.add_dvd(dvd3)

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Star Wars", "The Lion King"]
        )

    def test_sort_by_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Star Wars", cost=20)
        dvd2 = DigitalVideoDisc("Aladdin", cost=15)
        dvd3 = DigitalVideoDisc("The Lion King", cost=25)

        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.add_dvd(dvd3)

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [15, 20, 25]
        )

if __name__ == "__main__":
    unittest.main()