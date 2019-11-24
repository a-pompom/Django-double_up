import random

class CardHandler:
    """
    トランプのカードそのものを扱うためのハンドラ

    Attributes
    ----------
    cards : List<Card>
        ゲームで利用するトランプの集合を扱うためのリスト 
    uid_list : List<int>
        トランプのカードの重複を防ぐためのユニークIDを格納したもの
    """

    def __init__(self, cards):
        self.uid_list = []
        self.cards = cards

    """
    手札を初期化

    Returns
    -------
    cards : list<model.Card>
        初期化によって生成された手札 
        
    """
    def init_cards(self):
        # cardsはDBから取得した結果であり、結果が空の場合は、新たに手札を生成する
        if not self.cards:
            self.cards = []
            for i in range(1, 6):
                self.cards.append(self.create_card(i))

            return self.cards

        # 更新
        for card in self.cards:
            self.update_card(card)

        return self.cards

    """
    手札を初期化

    Parameters
    ---------- 
    card_index : int
        手札の各カードについて、表示位置を識別するためのインデックス
        
    Returns
    -------
    card : model.Card
    新規生成された一枚のカードモデル
        
    """
    def create_card(self, card_index):
        new_card = Cards(
                card_id=card_index,
                user_id=self.user_id)

        # 各手札について、現実のポーカーにおいては絵札の重複は許されないので、
        # 手札の範囲内においてユニークなものを生成
        generated_card = self.generate_unique_card(new_card)

        return generated_card.save()

    """
    手札を再生成

    Parameters
    ---------- 
    card : model.Card
         既存のカードモデル
    
    """
    def update_card(self, card):
        generated_card = self.generate_unique_card(card)

        generated_card.save()


    """
    ゲーム上でホールドされなかった手札について、再生成を行う

    Parameters
    ---------- 
    hold_list : list<str>
        cardのindexについて、ホールド対象となっているものを格納したリスト

    Returns
    -------
    cards : list<model.Card>
    再生成された手札

    """
    def update_unholded_cards(self, hold_list):

        for card in self.cards:

            if str(card.card_id) in hold_list:
                continue
            self.update_card(card)

        return self.cards


    """
    手札内でユニークなカードを生成

    Parameters
    ---------- 
    card : model.Card
         カードのベースとなるもの 数値・絵柄を更新

    Returns
    -------
    card : model.card
        生成されたユニークなカード

    """
    def generate_unique_card(self, card):
        is_unique = False 

        while not is_unique:
            card.card_number = random.randint(1,13)
            card.card_mark = random.randint(1,4)

            # 52枚の絵札として重複していなければよいので、カードの数字・絵札を数値化したものの積をUIDとして利用
            card_uid = card.card_number * card.card_mark

            is_unique = not card_uid in self.uid_list

        self.uid_list.append(card_uid)

        return card


    """
    役判定に利用するため、カードの数値をリスト化したものを返す

    Returns
    -------
    card_numbers : list<int>
        手札のカードの数値を格納したリスト

    """
    def get_card_numbers(self):
        card_numbers = []
        for card in self.cards:
            card_numbers.append(card.card_number)

        return card_numbers

    """
    役判定に利用するため、カードの絵柄をリスト化したものを返す

    Returns
    -------
    card_numbers : list<int>
        手札のカードの絵柄を格納したリスト

    """
    def get_card_marks(self):
        card_marks = []
        for card in self.cards:
            card_marks.append(card.card_mark)

        return card_marks

