from django import template

register = template.Library()

MARKS = ['?', '♢', '♣︎', '♠︎', '♡']

@register.filter
def get_mark(mark_index):
    """
    数値からトランプの絵柄を取得ｓ 

    Parameters
    ----------
    mark_index : int
        絵柄を格納している配列を参照するためのインデックス

    Returns
    -------
    絵柄 不明なときは、「?」を返す
    """
    return MARKS[mark_index]

@register.filter
def get_count(count):
    """
    表示用にプレイ回数をincrementして渡す

    Parameters
    ----------
    count : int
        プレイ回数

    Returns
    -------
    回数 + 1
    """
    return count + 1
