class Card:
    """
    絵札を格納するためのクラス

    Attributes
    ----------
    number : int
        カードの数値
    mark : int
        カードの絵柄を数値で表したもの
    uid : int
        カードの数値と絵柄を数値で表したものの積 一意なカードとするため利用
        
    """

    def __init__(self, number, mark):
        self._number = number
        self._mark = mark
        self._uid = number * mark

    @property
    def number(self):
        return self._number

    @property
    def mark(self):
        return self._mark

    @property
    def uid(self):
        return self._uid
