# ------------- LESSON 9, EXERCISE 1 -------------------
# Create classes Card, CardCreate
from random import randint


class ValueDiscountError(Exception):
    pass


class Card:
    def __init__(self):
        self.__card_number = None
        self._discount = 5

    @property
    def discount(self):
        return self._discount

    @property
    def card_number(self):
        return self.__card_number

    @discount.setter
    def discount(self, val: int) -> None:
        if isinstance(val, int) and val >= 1:
            self._discount = val
        else:
            raise ValueDiscountError('Check your discount value')


class CardCreated:
    card: list = []

    @classmethod
    def create(cls, amount: int, discount: int = None) -> None:

        card_numbers = [int(card.card_number) for card in cls.card]

        new_card_numb = '0000000000000000'
        if card_numbers:
            new_card_numb = max(card_numbers)

        for i in range(amount):
            new_card = Card()

            if discount is not None:
                new_card.discount = discount

            new_card_numb = str(int(new_card_numb) + 1)
            new_card_numb = '0' * (16 - len(new_card_numb)) + new_card_numb

            new_card._Card__card_number = new_card_numb

            cls.card.append(new_card)


CardCreated.create(10, 3)
card_dict = [{'card_number': i.card_number, 'discount': i.discount} for i in CardCreated.card]
print(*card_dict)










