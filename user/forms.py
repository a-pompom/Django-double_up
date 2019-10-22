from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

"""
CustomUserを利用して新規ユーザレコードを生成するためのモデル
デフォルトフィールドとして、パスワードのみを保持しており、その他認証等で利用する情報を定義していく
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
