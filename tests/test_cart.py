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


if __name__ == "__main__":
    unittest.main()