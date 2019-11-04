from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

from .models import Cards
from .service import PokerService



class PokerView(View):
    """
    ポーカーの状態を管理するためのクラス

    Attributes
    ----------
    template_name : str
        レンダリング対象のテンプレート名
    """

    template_name = 'poker.html'
    
    def get(self, request):
        """
        getリクエストで呼び出される処理 ゲームの状態を初期化

        Parameters
        ----------
        self : Object
            GameView
        request : HttpRequest
            home画面へのHttpRequest

        Returns
        -------
        renderedValue : HttpResponse
            home画面へ遷移し、ゲームの状態を保持するオブジェクトをコンテキストとして保持
        """

        print('poker get called:')

        # service呼び出し 5枚のカードをランダムに生成
        # 実体は、Cardsモデルのリストとして、コンテキストに格納
        service = PokerService(request.user.id)
        cards = service.init_cards()

        context = {'cards': cards}

        return render(request, 'poker.html', context)

    def post(self, request):
        print(request.POST.getlist('holds'))
        service = PokerService(request.user.id)

        cards = service.update_cards(request.POST.getlist('holds'))
        service.exists_poker_hand()

        context = {'cards': cards}

        return render(request, 'poker.html', context)




