from django.urls import path
from .views import PokerView

urlpatterns = [
        path('', PokerView.as_view(), name='poker'),
]
