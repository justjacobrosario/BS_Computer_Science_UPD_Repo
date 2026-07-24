from random import choice
from enum import Enum

'''
Cases:
- start, ask input
- if lose, add point to bot
- if win, add point to user
- if bot got highest, you lose
- if not, you win
'''

class PointTo(Enum):
    Tie = 0
    Bot = 1
    User = 2

def rand_rps() -> str:
    return choice(('R', 'P', 'S'))

def rps_logic(u: str, b: str) -> PointTo  :
    if u == b:
        return PointTo.Tie
    elif (u == 'R' and b =='P') or (u == 'P' and b == 'S') or (u == 'S' and b == 'P'):
        return PointTo.Bot
    else:
        return PointTo.User


class rps_model:
    user: str
    bot: str
    user_score: int
    bot_score: int
    limit: int

    def __init__(self, user: str = '0', bot: str = '0', user_score: int = 0, bot_score: int = 0, limit: int = 10) -> None:
        self.user = user    
        self.bot = bot
        self.user_score = user_score    
        self.bot_score  = bot_score 
        self.limit = limit

    def bot_action(self) -> str:
        self.bot = rand_rps()

    def nanalo_ka_ba(self) -> PointTo:
        return rps_logic(self.user, self.bot)

    def add_user(self) -> None:
        self.user_score += 1

    def add_bot(self) -> None:
        self.bot_score += 1

    def is_done(self) -> PointTo | bool:
        if self.user_score >= self.limit:
            return PointTo.User
        elif self.bot_score >= self.limit:
            return PointTo.Bot
        else:
            return False

class rps_view:
    model: rps_model

    def __init__(self, model: rps_model):
        self.model = model

    

    def set_limit(self):
        self.model.limit = int(input('Up to how many points to win: '))

    def action(self):
        self.model.user = input('R, P, S, Go!: ')

    def point_stats(self):
        print(f'You got {self.model.user_score} points against {self.model.bot_score}.')

    def partial_res(self, point_to: PointTo):
        dic = {'S':'✂️', 'R':'🪨', 'P':'📃'}
        if point_to == PointTo.User:
            self.model.add_user()
            print(f"✅ Nice! Your {dic[self.model.user]} beats {dic[self.model.bot]}!")
        elif point_to == PointTo.Bot:
            self.model.add_bot()
            print(f"❌ Dang! Your {dic[self.model.user]} got lost from {dic[self.model.bot]}")
        else:
            print(f"🟰 Phew! Tied from {dic[self.model.user]}.")



    def res(self):
        dic = {'S':'✂️', 'R':'🪨', 'P':'📃'}
        verdict = self.model.is_done()
        if verdict:
            if verdict == PointTo.User:
                print("🏆 Yehey! You Won!")
            else:
                print("❗ Aww! You Lost!")

class rps_controller:
    model: rps_model
    view: rps_view

    def __init__(self, model: rps_model, view: rps_view):
        self.model = model
        self.view = view

    def run(self):
        self.view.set_limit()

        while self.model.is_done() == False:
            self.model.bot_action()
            self.view.action()
            point_to = self.model.nanalo_ka_ba()
            self.view.partial_res(point_to)
            self.view.point_stats()
        self.view.res()


model = rps_model()
view = rps_view(model)
controller = rps_controller(model, view)
controller.run()