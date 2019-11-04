from django.db import models
from user.models import CustomUser


class Cards(models.Model):

    class Meta:
        unique_together = (('user', 'card_id'),)

    # 対象のユーザ
    user = models.ForeignKey (
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
    )

    # 何枚目のカードかを表す識別子 ユーザごとに5枚保持
    card_id = models.IntegerField(default=0)

    # 各カードの数値
    card_number = models.IntegerField(default=0)

    # 各カードの絵柄
    card_mark = models.IntegerField(default=0)
    
