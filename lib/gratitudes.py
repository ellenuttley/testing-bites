class Gratitudes:
    def __init__(self):
        self.gratitudess = []

    def add(self, gratitude):
        self.gratitudess.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudess)
        return formatted
