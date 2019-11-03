import random
from .models import GameStatus
from django.db.models import F

class DoubleUpService:
    """
    DoubleUpのロジック部分を処理するためのService

    Attributes
    ----------
    target : int
        currentに対してHigh/Lowを比較する値
    current : int
        画面に初期値として表示される値       
    """

    def __init__(self, user_id):
        """
        コンストラクタ
        current : int
            画面に表示される初期値 DBのレコードで保持されているので、ここでは初期化はしない
        target : int
            比較対象となる値 各メソッドで参照するので、インスタンスの属性値として保持しておく
        user_id: int
            処理対象のユーザID
        """
        self.target = random.randint(1,13)
        self.current = 0
        self.user_id = user_id

    def init_game_state(self):
        """
        画面初期表示の段階で呼ばれる処理 DBのレコードを初期化

        Parameters
        ----------
        self : Object

        Returns
        -------
        game_status : GameStatus 
            初期値が設定されたGameStatusModel
        """
        
        game_status = GameStatus.objects.filter(user_id=self.user_id)

        # get_or_createでは、ランダム生成されるcurrent,targetで既存レコードを紐付け・新規作成することが
        # できないので、取得処理の結果で分岐して、新規作成・既存レコードの初期化を分岐させる
        if not game_status:
            new_game_status = GameStatus(current=random.randint(1,13), target=0,doubleUpCount=0, user_id=self.user_id)
            new_game_status.save()
            return new_game_status.first()

        # 既存レコードを再生成した値及び初期値で初期化
        game_status.update(current=random.randint(1,13), target=0)
        return game_status.first()


    def update_target(self):
        """
        判定処理を行えるようにするため、ゲームの状態を更新

        Parameters
        ----------
        self : Object

        Returns
        -------
        game_status : GameStatus
            更新後のゲーム状態Model
        """

        game_status = GameStatus.objects.filter(user_id=self.user_id)

        game_status.update(target=self.target)
        self.current = game_status.first().current

        # ユーザIDでレコードは一意になるが、QuerySetオブジェクトはSequenceなので、先頭要素を返す
        return game_status.first()


    def compare_user_selected(self, selected):
        """
        ユーザの選択値(High/Low)が結果と合致しているか比較

        Parameters
        ----------
        self : DoubleUpService
        selected : str
            High or Low

        Returns
        -------
        result_message : str
            target == current => draw
            target > current and selected = High => win
            target < current and selected = Low => win
            else => lose
        """

        if self.target == self.current:
            self.update_user_game_status('draw')
            return 'draw...'

        if selected == 'High' and self.target > self.current:
            self.update_user_game_status('win')
            return 'you win!!'

        if selected == 'Low' and self.target < self.current:
            self.update_user_game_status('win')
            return 'you win!!'

        return 'you lose...'


    def update_user_game_status(self, result):
        """
        ゲーム状態として、ダブルアップ回数を更新

        Parameters
        ----------
        self : DoubleUpService
        result: str
            win/lose/draw

        Returns
        -------
        """
        
        game_status = GameStatus.objects.filter(user_id=self.user_id)

        if result == 'win':
            game_status.update(doubleUpCount=F('doubleUpCount') + 1)
            return

        if result == 'draw':
            game_status.update(doubleUpCount=F('doubleUpCount') + 1)
            return

        game_status.update(doubleUpCount=0)
