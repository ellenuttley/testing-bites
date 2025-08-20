# File: lib/diary.py

class Diary:
    def __init__(self, contents):
        if not isinstance(contents, str):
            raise Exception('This diary needs contents!')

        self.contents = contents

    def read(self):
        return self.contents
