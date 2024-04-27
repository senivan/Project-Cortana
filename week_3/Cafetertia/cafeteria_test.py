import unittest
from cafeteria2 import Track, Coffee, CustomCoffee, RECIPE

class TestCafeteria(unittest.TestCase):
    def setUp(self):
        Coffee.set_recipe(RECIPE)
        self.track = Track('07.02.2024')

    def test_track_init(self):
        self.assertEqual(self.track.date, '07.02.2024')
        self.assertEqual(self.track.orders, [])
        self.assertEqual(self.track.safety, True)
        self.assertEqual(self.track.__beans, 5000)
        self.assertEqual(self.track.__milk, 20000)

    def test_track_set_limit_milk(self):
        Track.set_limit_milk(30000)
        self.assertEqual(Track.__milk, 30000)

    def test_track_change_air_state(self):
        Track.change_air_state()
        self.assertEqual(Track.safety, False)
        Track.change_air_state()
        self.assertEqual(Track.safety, True)

    def test_track_place_order_invalid_coffee(self):
        order = 'invalid coffee'
        result = self.track.place_order(order)
        self.assertEqual(result, "We can't create anything that is not a Coffee instance.")

    def test_track_place_order_unknown_coffee(self):
        order = Coffee('macchiato')
        result = self.track.place_order(order)
        self.assertEqual(result, "Unfortunately, we don't have such kind of coffee in the menu.")

    def test_track_place_order_no_recipe(self):
        order = Coffee('mocca')
        result = str(order)
        self.assertEqual(result, "Order cannot be created. We don't have recipe for it.")

    def test_track_place_order_unsafe(self):
        Track.change_air_state()
        order = Coffee('espresso')
        result = self.track.place_order(order)
        self.assertEqual(result, 'Unfortunately, now it is not safe to make coffee.')
        Track.change_air_state()

    def test_track_place_order_no_ingredients(self):
        self.track.beans = 0
        self.track.milk = 0
        order = Coffee('espresso')
        result = self.track.place_order(order)
        self.assertEqual(result, "Unfortunately, we don't have enough ingredients.")

    def test_track_place_order_success(self):
        order = Coffee('espresso')
        result = self.track.place_order(order)
        self.assertEqual(result, 'Done!')
        self.assertEqual(len(self.track.orders), 1)
        self.assertEqual(self.track.orders[0].name, 'espresso')
        self.assertEqual(self.track.orders[0].count, 1)
        self.assertEqual(self.track.orders[0].price, 40)
        self.assertTrue(self.track.orders[0].is_paid)
        self.assertEqual(self.track.beans, 4964)
        self.assertEqual(self.track.milk, 19610)

    def test_track_total_revenue(self):
        self.track.place_order(Coffee('espresso'))
        self.track.place_order(Coffee('latte', 2))
        self.assertEqual(self.track.total_revenue(), 200)

    def test_track_total_milk(self):
        self.track.place_order(Coffee('latte', 2))
        self.assertEqual(self.track.total_milk(), 390)

    def test_track_total_beans(self):
        self.track.place_order(Coffee('latte', 2))
        self.assertEqual(self.track.total_beans(), 36)

    def test_track_milk_spoil(self):
        self.track.milk_spoil(19340)
        self.assertEqual(self.track.milk, 60)

    def test_coffee_init(self):
        order = Coffee('espresso')
        self.assertEqual(order.name, 'espresso')
        self.assertEqual(order.count, 1)
        self.assertEqual(order.espresso, 30)
        self.assertEqual(order.milk, 0)
        self.assertFalse(order.is_paid)

    def test_coffee_price(self):
        order = Coffee('espresso')
        order.price = 50
        self.assertEqual(order.price, 50)
        self.assertTrue(order.is_paid)

    def test_custom_coffee_init(self):
        order = CustomCoffee('espresso')
        self.assertEqual(order.name, 'espresso')
        self.assertEqual(order.count, 1)
        self.assertEqual(order.espresso, 30)
        self.assertEqual(order.milk, 0)
        self.assertFalse(order.is_paid)
        self.assertFalse(order.flavor)

    def test_custom_coffee_add_flavor(self):
        order = CustomCoffee('espresso')
        result = order.add_flavor(2, True, 'vanilla')
        self.assertEqual(result, 'Done!')
        self.assertEqual(order.sugar, 2)
        self.assertTrue(order.cinammon)
        self.assertEqual(order.syrup, 'vanilla')
        self.assertTrue(order.flavor)

    def test_custom_coffee_str(self):
        order = CustomCoffee('espresso')
        result = str(order)
        self.assertEqual(result, 'Order "1 custom espresso" is created.')
        order.add_flavor(2, True, 'vanilla')
        result = str(order)
        self.assertEqual(result, 'Your best espresso is ready! It has: 2 stickers of sugar, cinammon, vanilla syrup.')

    def test_custom_coffee_eq(self):
        order1 = CustomCoffee('espresso', 2)
        order2 = Coffee('espresso', 2)
        self.assertFalse(order1 == order2)
        order1.add_flavor(2, True, 'vanilla')
        self.assertFalse(order1 == order2)
        order2.add_flavor(2, True, 'vanilla')
        self.assertTrue(order1 == order2)

if __name__ == '__main__':
    unittest.main()