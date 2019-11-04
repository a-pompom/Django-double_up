from .models import Cards
import random

class PokerService:

    def __init__(self, user_id):
        self.user_id = user_id

    def init_cards(self):
        # カードを初期化してDBへ格納
        cards= Cards.objects.filter(user_id=self.user_id).order_by('card_id')

        if not cards:
            for i in range(1, 6):
                new_card = Cards(
                        card_id=i,
                        card_number=random.randint(1,13),
                        card_mark=random.randint(1,4),
                        user_id=self.user_id)
                new_card.save()

            cards= Cards.objects.filter(user_id=self.user_id).order_by('card_id')
            return cards

        for card in cards:
            
            card.card_number=random.randint(1,13)
            card.card_mark=random.randint(1,4)
            card.save()

        return cards

    def exists_poker_hand(self):
        # まずはHOLDされなかったものを再生成してみるか
        cards= Cards.objects.filter(user_id=self.user_id).order_by('card_id')

        # 役判定
        # まずはツーペア、スリーカードを判定してみる
        card_numbers = []
        card_marks = []
        for card in cards:
            card_numbers.append(card.card_number)
            card_marks.append(card.card_mark)

        judge_list = sorted(card_numbers)

        a = judge_list[0]
        count = 0

        for num in judge_list :
            print('loop')
            print(a)
            print(num)
            if a == num :
                count += 1

            a = num

        if count > 1:
            print('hand!!')
            print(count)


    def update_cards(self, hold_list):
        cards= Cards.objects.filter(user_id=self.user_id).order_by('card_id')

        for card in cards:
            if str(card.card_id) in hold_list:
                continue

            card.card_number=random.randint(1,13)
            card.card_mark=random.randint(1,4)

        return cards


