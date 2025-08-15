class GrammarStats:
    def __init__(self):
        self.pass_check = 0
        self.fail_check = 0

    def check(self, text):
        if text[0].isupper() and text[-1] in ".?!":
            self.pass_check += 1
            print('pass')
            return True
        else:
            self.fail_check += 1
            return False

    def percentage_good(self):
        total = self.pass_check + self.fail_check
        return int((100 / total) * self.pass_check)