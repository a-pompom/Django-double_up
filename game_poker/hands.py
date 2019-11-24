class Hands:
    """
    ポーカーの役を扱うためのクラス

    Attributes
    ----------
    sorted_card_numbers : List<int>
        ソート済みのカードの数値を格納したリスト
    card_marks : List<int>
        カードの絵柄を表す数値を格納したリスト
    pair_count: int
        ペアが何個存在するか
    card_same_count: int
        同じ数値のカードが何枚存在するか
    has_straight : bool
        ストレートが成り立つか
    has_flash : bool
        フラッシュが成り立つか
    """
    
    def __init__(self, card_numbers, card_marks):
        self.sorted_card_numbers = sorted(card_numbers)
        self.card_marks = card_marks

        self.pair_count = 0
        self.card_same_count = 0
        self.has_straight = False
        self.has_flash = False

    """
    役の判定を行う

    Returns
    -------
    hands : str
        役を表す文字列
        
    """
    def calc_hands(self):
        # 役判定処理
        self.calc_straight() \
        .calc_flash() \
        .calc_pair_and_same()

        # 成立した役を返す
        if self.has_flash and self.has_straight:
            return 'STRAIGHT FLASH!!!'

        if self.has_straight:
            return 'STRAIGHT!!'

        if self.has_flash:
            return 'FLASH!!'

        if self.pair_count == 4 and self.card_same_count == 3:
            return 'FULL HOUSE!!'

        if self.card_same_count == 3:
            return '3 CARD!'

        if self.pair_count == 2:
            return '2 PAIR!'

        return 'NO HAND...'

    """
    ストレートが成り立つか判定
    ストレート: カードの数値が連番となる
    (ex: 1,2,3,4,5)

    """
    def calc_straight(self):
        head = self.sorted_card_numbers[0]

        # 任意の手札のカードcard_nについて、card_n+1 = card_n + 1が成り立つか
        for card_number in self.sorted_card_numbers:
            if card_number != head:
                self.has_straight = False
                return self

            head += 1

        self.has_straight = True

        return self

    """
    フラッシュが成り立つか判定
    フラッシュ: 手札のカードの絵柄が全て同じ
        
    """
    def calc_flash(self):
        head = self.card_marks[0]

        for mark in self.card_marks:
            if mark != head:
                self.has_flash = False
                return self

        self.has_flash = True

        return self

    """
    手札のカードの数値について、連続している数・ペアの数を判定
    今回はロジックを単純化するため、1,1,1という並びであっても2つのペアであるというように判定している

    """
    def calc_pair_and_same(self):
        # ペアの数 1ペア、2ペアが存在
        pair_count = 0
        # 同じ数値のカードが何回続いたか 3カード・4カードを判定する際のスタックとして利用
        same_number_count = 1
        # 手札内の同じ数値のカードの数 3カード・4カードが成り立つか判定する際に利用
        max_same_number_count = 0
        # ペア・同じ数値のカードを集計する際の開始位置 手札のカード1枚々を走査するために利用
        head_index = 0

        # 1,1,2,2,2という手札があった場合、
        # [1],1,2,2,2 -> 1,[1],2,2,2 -> 1,1,[2],2,2...
        # というように走査し、数値の連続数・ペアの数を判定する
        for current_card_number in self.sorted_card_numbers:

            for card_pointer in range(head_index,len(self.sorted_card_numbers)):
                # 自身との比較は不要なのでスキップ
                if card_pointer == head_index:
                    continue

                if current_card_number != self.sorted_card_numbers[card_pointer]:
                    same_number_count = 1
                    continue

                # 同じ数値のカードが連続した場合、役判定に利用できるよう、連続数を更新し、
                # 連続がペアとなる場合、ペア数もあわせて増やす
                same_number_count+= 1
                if same_number_count == 2:
                    pair_count+= 1

                # 最大連続数の更新判定
                if same_number_count > max_same_number_count:  
                    max_same_number_count = same_number_count
                
            head_index+= 1

        self.pair_count = pair_count
        self.card_same_count = max_same_number_count

        return self
