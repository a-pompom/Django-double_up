from django import forms
from .models import GameStatus

class GameForm(forms.ModelForm):
    models = GameStatus
