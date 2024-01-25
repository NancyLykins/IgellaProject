class TURN_CONTROL:  
    def __init__(self):
        self.turn = 0

    def increment(self):
        self.turn += 1

    def finish(self):
        self.turn = 0

    def get(self):
        return self.turn
    