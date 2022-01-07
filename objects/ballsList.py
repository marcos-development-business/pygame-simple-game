from .ball import Ball


class BallsList:
    __list_of_balls = []

    def add_ball(self, ball: Ball):
        self.__list_of_balls.append(ball)

    def remove_ball(self, ball_id: str):
        new_list_of_balls = []

        for ball in self.__list_of_balls:
            if ball.id != ball_id:
                new_list_of_balls.append(ball)

        self.__list_of_balls = new_list_of_balls

    def get_balls(self):
        return self.__list_of_balls
