class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def increse_score(self):
        self.score= self.score + 1
        return self.score


class PaidUser(User):
    def __init__(self, paid_user, paid_score, account_balance):
        super().__init__(paid_user, paid_score)
        self.account_balance = account_balance

    def increse_balance(self):
        self.account_balance = self.account_balance + 1
        return self.account_balance


user1 = User('Phil', 5)
paidUser1 = PaidUser('Tim', 8, 25)
print(f"USER: {user1.name} {user1.score} = SCORE: {user1.increse_score()}")
print(f"USER: {paidUser1.name} {paidUser1.score} {paidUser1.account_balance} = "
      f"BALANCE: {paidUser1.increse_balance()}  SCORE: {paidUser1.increse_score()}")

