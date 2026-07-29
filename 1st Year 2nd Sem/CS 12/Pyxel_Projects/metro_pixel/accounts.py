

class Account:
    def __init__(self, username : str, pw : str):
        self._username : str = username
        self._pw : str = pw
        self._exp : int = 0
        self._lvl : int = 1

    def upd_exp(self, val : int):
        target_exp : int = 100 * (1 + self._lvl * 0.1)
        self._exp += val
        if self._exp >= target_exp:
            self._lvl += 1
            self._exp = target_exp - self._exp
        


account_repository : dict[str, Account] = {}