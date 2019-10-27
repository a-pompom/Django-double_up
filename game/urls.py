from django.urls import path
from .views import GameView

urlpatterns = [
        path('<str:selected>', GameView.as_view(), name='home'),
        path('', GameView.as_view(), name='home'),
]
