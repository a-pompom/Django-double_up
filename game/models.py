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
    current = models.IntegerField(default = 0)

    # ユーザが選択したHighまたはLowについて、currentと比較する対象
    target = models.IntegerField(default = 0)

    # ダブルアップが何回連続で成功したか
    doubleUpCount = models.IntegerField(default = 0)

    # ユーザが保持しているコイン
    coin = models.IntegerField(default = 1000)

    # ゲーム単位で獲得したコイン
    gainedCoin = models.IntegerField(default = 0)
    
