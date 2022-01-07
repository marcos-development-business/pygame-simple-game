

class Score:
    __score = 0

    def increment(self, to=1):
        self.__score += to

    def decrement(self, by=1):
        self.__score -= by

    def reset(self):
        self.__score = 0

    def lose(self, total=10):
        if self.__score > total:
            self.decrement(total)
        else:
            self.reset()

    def __str__(self):
        return str(self.__score).rjust(3, '0')
