from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstractUserを継承することで、ユーザの基本属性(ユーザ名、メールアドレス、パスワード、苗字など...)に加え、
# 権限関連の情報もまとめてプロパティとして持つことができる
# また、カスタムユーザを設定しておくと、後からの拡張に柔軟に対応できるようになるため、
# Djangoのアプリ開発では基本的には認証・認可処理にCustomUserを利用していく
class CustomUser(AbstractUser):
    pass

    
