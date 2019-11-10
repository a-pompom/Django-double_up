from .models import Cards
from .hands import Hands
from .cardHandler import CardHandler

class PokerService:
    """
    ポーカーゲームのロジック部分を扱うためのサービス

    Attributes
    ----------
    user_id : int
        ゲームプレイ中のユーザID
    cardHandler : CardHandler    
        トランプのカードを扱うためのハンドラ
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.card_handler = CardHandler(Cards.objects.filter(user_id=self.user_id).order_by('card_id'))

    def init_cards(self):
        return self.card_handler.init_cards()

    def update_unholded_cards(self, hold_list):
        return self.card_handler.update_unholded_cards(hold_list)

    def get_poker_hand(self):
        card_numbers = self.card_handler.get_card_numbers()
        card_marks = self.cardhandler.get_card_marks()

        hands = Hands(card_numbers, card_marks)

        return hands.calc_hands()
