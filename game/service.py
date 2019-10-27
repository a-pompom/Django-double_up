import random
from .models import GameStatus

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

    def __init__(self):
        """
        コンストラクタ
        current : int
            画面に表示される初期値 DBのレコードで保持されているので、ここでは初期化はしない
        target : int
            比較対象となる値 各メソッドで参照するので、インスタンスの属性値として保持しておく
        """
        self.target = random.randint(1,13)
        self.current = 0

    def init_game_state(self, user_id):
        """
        画面初期表示の段階で呼ばれる処理 DBのレコードを初期化

        Parameters
        ----------
        self : Object
        user_id : int
            ゲームを現在プレイしているユーザのID

        Returns
        -------
        game_status : GameStatus 
            初期値が設定されたGameStatusModel
        """
        
        game_status = GameStatus.objects.filter(user_id=user_id)

        # get_or_createでは、ランダム生成されるcurrent,targetで既存レコードを紐付け・新規作成することが
        # できないので、取得処理の結果で分岐して、新規作成・既存レコードの初期化を分岐させる
        if not game_status:
            new_game_status = GameStatus(current=random.randint(1,13), target=0, user_id=user_id)
            new_game_status.save()
            return new_game_status.first()

        # 既存レコードを再生成した値及び初期値で初期化
        game_status.update(current=random.randint(1,13), target=0)
        return game_status.first()


    def update_target(self, user_id):
        """
        判定処理を行えるようにするため、ゲームの状態を更新

        Parameters
        ----------
        self : Object
        user_id : int
            現在プレイ中のユーザのID

        Returns
        -------
        game_status : GameStatus
            更新後のゲーム状態Model
        """

        game_status = GameStatus.objects.filter(user_id=user_id)

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
            return 'draw...'

        if selected == 'High' and self.target > self.current:
            return 'you win!!'

        if selected == 'Low' and self.target < self.current:
            return 'you win!!'

        return 'you lose...'
        
