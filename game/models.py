from django.db import models
from user.models import CustomUser

# Create your models here.

class GameStatus(models.Model):

    # 対象のユーザ
    user = models.ForeignKey (
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
    )

    # 画面に初期値として表示される数値
    current = models.IntegerField()

    # ユーザが選択したHighまたはLowについて、currentと比較する対象
    target = models.IntegerField()
    
