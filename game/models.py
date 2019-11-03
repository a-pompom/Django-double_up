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

    # 初期値の絵柄
    current_mark = models.IntegerField(default=0)

    # ユーザが選択したHighまたはLowについて、currentと比較する対象
    target = models.IntegerField(default = 0)

    # 比較対象の絵柄
    target_mark = models.IntegerField(default=0)

    # ダブルアップが何回連続で成功したか
    double_up_count = models.IntegerField(default = 0)

    # ユーザが保持しているコイン
    coin = models.IntegerField(default = 1000)

    # ゲーム単位で獲得したコイン
    gained_coin = models.IntegerField(default = 0)
    
