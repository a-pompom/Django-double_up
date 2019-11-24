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

    """
    手札を初期化

    Returns
    -------
    cards : list<model.Card>
    初期化された手札
        
    """
    def init_cards(self):
        return self.card_handler.init_cards()

    """
    ホールドされなかったカードを更新

    Returns
    -------
    cards : list<model.Card>
    更新された手札
        
    """
    def update_unholded_cards(self, hold_list):
        return self.card_handler.update_unholded_cards(hold_list)

    """
    役判定処理を行う

    Returns
    -------
    hands : str
        役を表す文字列
        
    """
    def get_poker_hand(self):
        card_numbers = self.card_handler.get_card_numbers()
        card_marks = self.card_handler.get_card_marks()

        hands = Hands(card_numbers, card_marks)

        return hands.calc_hands()
