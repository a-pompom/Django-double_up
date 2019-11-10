from .models import Cards
from .hands import Hands
from .cardHandler import CardHandler

class PokerService:

    def __init__(self, user_id):
        self.user_id = user_id
        self.cardHandler = CardHandler(Cards.objects.filter(user_id=self.user_id).order_by('card_id'))

    def init_cards(self):
        return self.cardHandler.init_cards()

    def update_unholded_cards(self, hold_list):
        return self.cardHandler.update_unholded_cards(hold_list)

    def exists_poker_hand(self):
        card_numbers = self.cardHandler.get_card_numbers()
        card_marks = self.cardHandler.get_card_marks()

        hands = Hands(card_numbers, card_marks)

        return hands.calc_hands()
