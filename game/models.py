from django.db import models

# Create your models here.

class GameStatus(models.Model):
    # 画面に初期値として表示される数値
    current = models.IntegerField()

    # ユーザが選択したHighまたはLowについて、currentと比較する対象
    target = models.IntegerField()
