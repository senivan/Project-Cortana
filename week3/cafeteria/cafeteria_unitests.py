'''Cafeteria testing'''

# After creating the tests, the number of tests covering
# the task was 95. Next, copylot tried to determine which
# parts of the problem it did not cover. ("What corner cases
# are not covered by the tests in the class...?").
# He added additional checks to the __str__ and __eq__ functions,
# but until the last moment he did not realize that some arguments
# should be defined in separate clauses, not in the initial.
# He also failed to cover one case in __eq__ in the Coffee class (when flavor is False).
# In the end, the copylot managed to cover the task with 99% of the tests,
# but with hints about specific cases in individual functions.
# The code now works 100% correctly.

import unittest
from cafeteria import Coffee, CustomCoffee, FlavorMixin, Track, RECIPE

class TestCafeteriaClass(unittest.TestCase):
    def test_cafeteria_class(self):
        day_track = Track('07.02.2024')
        day_track.date = '07.02.2024'
        order1 = Coffee('latte')
        self.assertEqual(str(order1), 'Order cannot be created. Recipe has not been set.')
        self.assertEqual(order1.__dict__, {'name': 'latte', 'count': 1})
        Coffee.set_recipe(RECIPE)
        order1 = Coffee('latte', 2)
        self.assertEqual(order1.name, 'latte')
        self.assertEqual(order1.count, 2)
        self.assertFalse(order1.is_paid)
        self.assertEqual(order1.espresso, 120)
        self.assertEqual(order1.milk, 270)
        self.assertEqual(Coffee._Coffee__recipe[order1.name], {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15})
        self.assertEqual(str(order1), 'Order "2 latte" is created.')
        self.assertEqual(Track.MENU, {
            "espresso":  40,
            "latte": 70,
            "flat white": 70,
            "dopio":  50,
            "cappuccino":  60,
            "lungo": 50,
            "cortado": 55,
            "mocca": 60})
        self.assertEqual(day_track.place_order(order1), 'Done!')
        self.assertEqual(order1.price, 140)
        self.assertTrue(order1.is_paid)
        self.assertEqual(str(order1), 'Preparing 2 latte...')
        self.assertEqual(len(day_track.orders), 1)
        order2 = Coffee("macchiato")
        self.assertNotEqual(order1, order2)
        self.assertEqual(str(order2), 'Order "1 macchiato" is created.')
        self.assertEqual(order2.__dict__, {'name': 'macchiato', 'count': 1, 'is_paid': False})
        self.assertEqual(day_track.place_order(order2), "Unfortunately, we don't have such kind of coffee in the menu.")
        self.assertEqual(len(day_track.orders), 1)
        order2 = Coffee("mocca")
        self.assertEqual(str(order2), "Order cannot be created. We don't have recipe for it.")
        self.assertEqual(order2.__dict__, {'name': 'mocca', 'count': 1})
        order2 = CustomCoffee('cappuccino')
        self.assertNotEqual(order1, order2)
        self.assertIsInstance(order2, CustomCoffee)
        self.assertIsInstance(order2, Coffee)
        self.assertIsInstance(order2, FlavorMixin)
        self.assertNotIsInstance(order1, CustomCoffee)
        self.assertNotIsInstance(order1, FlavorMixin)
        self.assertEqual(order2.name, 'cappuccino')
        self.assertEqual(order2.count, 1)
        self.assertEqual(order2.espresso, 60)
        self.assertEqual(order2.milk, 120)
        self.assertFalse(order2.flavor)
        self.assertEqual(day_track.place_order(order2), 'Done!')
        self.assertEqual(len(day_track.orders), 2)
        self.assertEqual(str(order2), 'Preparing 1 cappuccino...')
        self.assertEqual(order2.price, 60)
        self.assertEqual(order2.add_flavor(2, True, 'almond'), 'Done!')
        self.assertEqual(order2.sugar, 2)
        self.assertTrue(order2.cinammon)
        self.assertEqual(order2.syrup, 'almond')
        self.assertEqual(str(order2), 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.')
        self.assertEqual(str(day_track.orders), '[2 latte, 1 custom cappuccino]')
        self.assertEqual(day_track.total_revenue(), 200)
        self.assertEqual(day_track.total_milk(), 390)
        self.assertEqual(day_track.total_beans(), 36)
        self.assertNotIsInstance(order2, Track)
        self.assertEqual(Track._Track__beans, 5000)
        self.assertEqual(Track._Track__milk, 20000)
        self.assertEqual(day_track.beans, 4964)
        self.assertEqual(day_track.milk, 19610)
        order3 = Coffee('Irish Coffee', 3)
        self.assertEqual(day_track.orders, [order1, order2])
        order3 = CustomCoffee('latte', 2)
        self.assertEqual(order3, order1)
        self.assertEqual(order3.add_flavor(3, False, 'green banana'), 'Please, pay for it.')
        self.assertEqual(order1, order3)
        self.assertEqual(day_track.place_order(order3), 'Done!')
        self.assertEqual(str(order3), 'Preparing 2 latte...')
        self.assertEqual(order3.add_flavor(3, False, 'green banana'), 'Done!')
        self.assertEqual(order3.sugar, 6)
        self.assertEqual(str(order3), 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.')
        self.assertNotEqual(order3, order1)
        day_track.milk_spoil(19340)
        self.assertEqual(day_track.milk, 0)
        order4 = Coffee('latte', 2)
        self.assertEqual(day_track.place_order(order4), "Unfortunately, we don't have enough ingredients.")
        self.assertEqual(len(day_track.orders), 3)
        Track.set_limit_milk(30000)
        self.assertEqual(Track._Track__milk, 30000)
        order5 = "Coffee"
        self.assertNotIsInstance(order5, CustomCoffee)
        self.assertEqual(day_track.place_order(order5), "We can't create anything that is not a Coffee instance.")
        Track.change_air_state()
        self.assertFalse(Track.safety)
        order6 = CustomCoffee('lungo', 2)
        self.assertEqual(day_track.place_order(order6), 'Unfortunately, now it is not safe to make coffee.')
        Track.change_air_state()
        self.assertTrue(Track.safety)
        order6 = CustomCoffee('lungo')
        self.assertEqual(str(order6), 'Order "1 custom lungo" is created.')
        self.assertEqual(day_track.place_order(order6), 'Done!')
        self.assertEqual(day_track.total_revenue(),  390)
        self.assertEqual(day_track.total_milk(), 660)
        self.assertEqual(day_track.total_beans(), 78)

        Track.set_limit_milk(15000)
        self.assertEqual(Track._Track__milk, 15000)

        day_track.milk_spoil(5000)
        self.assertEqual(day_track._Track__milk, 0)

        Coffee.set_recipe(RECIPE)
        order7 = Coffee('espresso')
        self.assertEqual(order7.espresso, 30)

        order8 = CustomCoffee('latte')
        self.assertEqual(order8.add_flavor(2, True, 'vanilla'), 'Please, pay for it.')

        order = Coffee('unknown_coffee')
        self.assertEqual(order.espresso, 0)
        self.assertEqual(order.milk, 0)
        self.assertNotEqual(order, order8)
        self.assertNotEqual(order8, order3)

if __name__ == '__main__':
    unittest.main()

# python -m coverage run cafeteria_unitests.py
# python -m coverage report -m
