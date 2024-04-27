"""Cafeteria"""
RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }

class Track:
    """
    Track class
    """
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    safety = True
    __beans = 5000
    __milk = 20000
    orders = []
    def __init__(self, date: str) -> None:
        self.date = date
    @classmethod
    def set_limit_milk(cls, value: int) -> None:
        """
        The method that sets the limit of milk
        """
        cls._Track__milk = value
    @classmethod
    def change_air_state(cls) -> None:
        """
        The method that changes the air state
        """
        cls.safety = not cls.safety
    # @classmethod
    # def milk_spoil(cls, value: int) -> None:
    #     """
    #     Milk spoil
    #     """
    #     cls._Track__milk -= value
    @property
    def beans(self) -> int:
        """
        Beans
        """
        total_beans_needed = self.total_beans()
        return max(self.__beans - total_beans_needed, 0)
    # @beans.setter
    # def beans(self, value: int) -> None:
    #     self.__beans = value
    # @beans.getter
    # def beans(self) -> int:
    #     """
    #     Beans
    #     """
    #     total_beans_needed = self.total_beans()
    #     return max(self.__beans - total_beans_needed, 0)
    @property
    def milk(self) -> int:
        """
        Milk
        """
        total_milk_needed = self.total_milk()
        return max(self.__milk - total_milk_needed, 0)
    def place_order(self, order) -> str:
        """
        Place order
        """
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        if order.name not in self.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        if not Track.safety:
            return "Unfortunately, now it is not safe to make coffee."
        if self.milk < order.milk or self.beans < order.count * 6:
            return "Unfortunately, we don't have enough ingredients."
        self.orders += [order]
        order.price = self.MENU[order.name]*order.count
        order.is_paid = True
        return 'Done!'
    def total_revenue(self) -> int:
        """
        Total revenue
        """
        return sum(order.price for order in self.orders)
    def total_milk(self) -> int:
        """
        Total milk
        """
        return sum(order.milk for order in self.orders)
    def total_beans(self) -> int:
        """
        Total beans
        """
        return sum(order.espresso/30 for order in self.orders)*6
    def milk_spoil(self, value: int) -> None:
        """
        Milk spoil
        """
        self.__milk -= value
        self.__milk = max(self.__milk, 0)

class Coffee:
    """
    The Coffee class
    """
    __recipe = {}

    def __init__(self, name, count=1) -> None:
        self.name = name
        self.count = count
        if self.name in self.__recipe:
            self.is_paid = False
    @property
    def espresso(self):
        '''The espresso'''
        if self.__recipe is not None and self.name in self.__recipe:
            return self.__recipe[self.name]['espresso'] * self.count
        return 0
    @property
    def milk(self):
        '''The milk'''
        if self.__recipe is not None and self.name in self.__recipe:
            return (self.__recipe[self.name].get('steamed_milk', 0)
                    + self.__recipe[self.name].get('foamed_milk', 0)) * self.count
        return 0
    # @property
    # def price(self):
    #     """
    #     The price
    #     """
    #     return self.__price
    # @price.setter
    # def price(self, value):
    #     self.__price = value
    #     self.is_paid = True
    @classmethod
    def set_recipe(cls, recipe: dict) -> None:
        """
        This method sets the recipe for the coffee
        """
        cls.__recipe = recipe

    def __str__(self) -> str:
        if not self.__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self.__recipe:
            return "Order cannot be created. We don\'t have recipe for it."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        if isinstance(self, CustomCoffee):
            return f'Order "{self.count} custom {self.name}" is created.'
        return f'Order "{self.count} {self.name}" is created.'

    # @property
    # def __dict__(self):
    #     if self.__recipe is None or self.name not in self.__recipe:
    #         return {'name': self.name, 'count': self.count}
        # return {'name': self.name, 'count': self.count, 'is_paid': self.is_paid}
    def __repr__(self) -> str:
        return f'{self.count} {self.name}'
    def __eq__(self, other) -> bool:
        if not isinstance(other, CustomCoffee) or not other.flavor:
            return (self.name, self.count) == (other.name, other.count)
        return False

class FlavorMixin():
    """
    The FlavorMixin class
    """
    def add_flavor(self, sugar: int, cinammon: bool, syrup: str) -> None:
        """
        The method that adds flavor to the coffee
        """
        if self.is_paid:
            self.sugar = sugar * self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return 'Done!'
        return 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """
    The CustomCoffee class
    """
    def __init__(self, name, count=1) -> None:
        Coffee.__init__(self, name, count)
        # self.is_paid = False
        self.flavor = False

    # def add_flavor(self, sugar, cinammon, syrup):
    #     self.sugar = sugar
    #     self.cinammon = cinammon
    #     self.syrup = syrup
    #     return 'Done!'

    # def add_flavor(self, sugar: int, cinammon: bool, syrup: str) -> None:
    #     """
    #     The method that adds flavor to the coffee
    #     """
    #     self.sugar = sugar * self.count
    #     self.cinammon = cinammon
    #     self.syrup = syrup
    #     self.flavor = True
    #     if self.is_paid:
    #         return 'Done!'
    #     return 'Please, pay for it.'
    def __str__(self) -> str:
        if not self.flavor:
            return Coffee.__str__(self)
        flavor_description = ''
        if self.sugar:
            flavor_description += f'{self.sugar} stickers of sugar, '
        if self.cinammon:
            flavor_description += 'cinammon, '
        if self.syrup:
            flavor_description += f'{self.syrup} syrup, '
        if flavor_description:
            return f'Your best {self.name} is ready! It has: {flavor_description[:-2]}.'

    def __repr__(self) -> str:
        return f'{self.count} custom {self.name}'
    def __eq__(self, other) -> bool:
        if not isinstance(other, CustomCoffee):
            if self.flavor:
                return False
            return (self.name, self.count) == (other.name, other.count)
        return (self.name == other.name and self.count == other.count and
                    self.sugar == other.sugar and self.cinammon == other.cinammon
                    and self.syrup == other.syrup)
