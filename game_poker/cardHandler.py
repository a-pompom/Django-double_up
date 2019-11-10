import random

class CardHandler:
    """
    トランプのカードそのものを扱うためのハンドラ

    Attributes
    ----------
    cards : List<Card>
        ゲームで利用するトランプの集合を扱うためのリスト 
    """

    def __init__(self, cards):
        self.uid_list = []
        self.cards = cards

    def init_cards(self):
        if not self.cards:
            self.cards = []
            for i in range(1, 6):
                self.cards.append(self.create_card(i))

            return self.cards

        for card in self.cards:
            self.update_card(card)

        return self.cards

    def create_card(self, card_index):
        new_card = Cards(
                card_id=card_index,
                user_id=self.user_id)

        generated_card = self.generate_unique_card(card)

        return new_card.save()

    def update_card(self, card):
        generated_card = self.generate_unique_card(card)

        card.save()

    def update_unholded_cards(self, hold_list):

        for card in self.cards:
            if str(card.card_id) in hold_list:
                continue
            self.update_card(card)

        return self.cards

    def generate_unique_card(self, card):
        is_unique = False 

        while not is_unique:
            card.card_number = random.randint(1,13)
            card.card_mark = random.randint(1,4)

            card_uid = card.card_number * card.card_mark

            is_unique = not card_uid in self.uid_list

        self.uid_list.append(card_uid)

        return card

    def get_card_numbers(self):
        card_numbers = []
        for card in self.cards:
            card_numbers.append(card.card_number)

        return card_numbers

    def get_card_marks(self):
        card_marks = []
        for card in self.cards:
            card_marks.append(card.card_mark)

        return card_marks

