from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

from .models import GameStatus
import random

# Create your views here.

class GameView(View):
    model = GameStatus
    template_name = 'home.html'

    def get(self, request):
        game_status = GameStatus(current=random.randint(1, 13), target=0)
        game_status.save()

        return render(request, 'home.html', {'status': game_status})
