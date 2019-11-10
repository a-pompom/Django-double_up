class Hands:
    
    def __init__(self, card_numbers, card_marks):
        self.sorted_card_numbers = sorted(card_numbers)
        self.card_marks = card_marks

        self.pair_count = 0
        self.card_same_count = 0
        self.has_straight = False
        self.has_flash = False

    def calc_hands(self):
        self.calc_straight() \
        .calc_flash() \
        .calc_pair_and_same()

        if self.has_flash and self.has_straight:
            return 'straight flash'

        if self.has_straight:
            return 'straight'

        if self.has_flash:
            return 'flash'

        if self.pair_count == 4 and self.card_same_count == 3:
            return 'full house'

        if self.card_same_count == 3:
            return '3 card'

        if self.pair_count == 2:
            return '2 pair'

        return 'no hand...'


    def calc_straight(self):
        # 5枚のカードの数値の和 = (head + tail) * 3を満たすとき、ストレートが成り立つ
        head = self.sorted_card_numbers[0]
        tail = self.sorted_card_numbers[len(self.sorted_card_numbers)-1]

        card_number_sum = 0
        for card_number in self.sorted_card_numbers:
            card_number_sum += card_number

        sequential_sum = (head + tail) * 3 - ((head + tail) / 2)

        if card_number_sum == sequential_sum:
            self.has_straight = True

        return self

    def calc_flash(self):
        head = self.card_marks[0]

        card_mark_sum = 0
        for mark in self.card_marks:
            card_mark_sum += mark

        if card_mark_sum == head * len(self.card_marks):
            self.has_flash = True

        return self

    def calc_pair_and_same(self):
        pair_count = 0
        same_number_count = 1
        max_same_number_count = 0
        head_index = 0

        for current_card_number in self.sorted_card_numbers:

            for card_pointer in range(head_index,len(self.sorted_card_numbers)):
                if card_pointer == head_index:
                    continue

                if current_card_number == self.sorted_card_numbers[card_pointer]:
                    pair_count+= 1
                    same_number_count+= 1
                    continue

                if same_number_count > max_same_number_count:
                    max_same_number_count = same_number_count
                
                same_number_count = 1

            head_index+= 1
            if same_number_count > max_same_number_count:
                max_same_number_count = same_number_count

            same_number_count = 1

        self.pair_count = pair_count
        self.card_same_count = max_same_number_count

        return self
