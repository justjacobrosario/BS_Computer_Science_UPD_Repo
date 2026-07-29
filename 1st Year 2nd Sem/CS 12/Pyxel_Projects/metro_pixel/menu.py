from constants import GameError
import accounts
from accounts import Account, account_repository


class Menu:
    def __init__(self):
        self._selected_accs : dict[str, Account] = {}
        self._selected_mode : ModeConfig | None = None
        self._selected_map : MapInfo | None

    @property
    def selected_accs(self):
        return self._selected_accs

    @property
    def selected_mode(self):
        return self._selected_mode

    @property
    def selected_map(self):
        return self._selected_map

    def login_acc(self, acc_username : str, pw : str) -> GameError | None:
        if acc_username not in account_repository.keys():
            return GameError.ACC_NOT_EXISTING
        else:
            acc_obj = account_repository[acc_username]
            if acc_obj.pw != pw:
                return GameError.WRONG_PW
            if acc_username in self._selected_accs.keys():
                return GameError.ACC_ALREADY_LOGGED_IN
            else:
                self._selected_accs[acc_username] = acc_obj
                return None

    def logout_acc(self, acc_username : str, pw : str) -> GameError | None:
        if acc_username not in account_repository.keys():
            return GameError.ACC_NOT_EXISTING
        else:
            acc_obj = account_repository[acc_username]
            if acc_obj.pw != pw:
                return GameError.WRONG_PW
            elif acc_username not in self._selected_accs.keys():
                return GameError.ACC_NOT_LOGGED_IN
            else:
                self._selected_accs.pop(acc_username, None)
                return None

    def signin_acc(self, acc_username : str, pw : str) -> GameError | None:
        if acc_username in account_repository.keys():
            return GameError.ACC_EXISTS
        else:
            account_repository[acc_username] = Account(username = acc_username, pw = pw)
            return None

    def delete_acc(self, acc_username : str, pw : str) -> GameError | None:
        if acc_username not in account_repository.keys():
            return GameError.ACC_NOT_EXISTING
        else:
            acc_obj = account_repository[acc_username]
            if acc_obj.pw != pw:
                return GameError.WRONG_PW
            else:
                account_repository.pop(acc_username)
                return None

    