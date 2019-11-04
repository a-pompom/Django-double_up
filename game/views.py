from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

from .models import GameStatus
from .service import DoubleUpService
import random


class GameView(View):
    """
    ダブルアップの状態を管理するためのViewクラス

    Attributes
    ----------
    template_name : str
        レンダリング対象のテンプレート名
    """

    template_name = 'home.html'
    
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

        service = DoubleUpService(request.user.id)
        game_status = service.init_game_state()

        return render(request, 'home.html', {'status': game_status})


    def post(self, request, selected):
        """
        postメソッドで呼び出される処理 ダブルアップの結果を導出し、勝敗判定を行う

        Parameters
        ----------
        self : object
            GameView
        request : HttpRequest
            home.htmlでのpostリクエスト
        selected : str
            ユーザの画面上での選択値 High あるいは Lowをとる

        Returns
        -------
        rendered_value : HttpResponse
            home画面へ遷移し、結果を表示するためのコンテキストを保持
        """

        service = DoubleUpService(request.user.id)
        game_status = service.update_target()

        result_message = service.compare_user_selected(selected)

        return render(request, 'home.html', {'status': game_status, 'result_message': result_message})

