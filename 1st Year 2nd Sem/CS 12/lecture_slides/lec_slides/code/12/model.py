import pyxel


class PipePair:
    def __init__(self, init_x: int, init_y: int, w: int, h: int):
        self.x = init_x
        self.y = init_y
        self.w = w
        self.h = h


def overlap(int1: tuple[int, int], int2: tuple[int, int]) -> bool:
    l1, r1 = int1
    l2, r2 = int2

    return max(l1, l2) <= min(r1, r2)


class Bird:
    def __init__(self, init_x: int, init_y: int, r: int):
        self.x = init_x
        self.y = init_y
        self.r = r

    #
    # /---\
    # | c | -
    # \___/ r
    #       -

    def reached_bottom(self, sc_height: int) -> bool:
        return self.y + self.r >= sc_height

    def collides_with(self, pipepair) -> bool:
        # (self.x - self.r, self.x + self.r) overlaps with
        # (pipepair.x, pipepair.x + pipepair.w)
        # ------
        #   ------

        bird_xint = (self.x - self.r, self.x + self.r)
        pipepair_xint = (pipepair.x, pipepair.x + pipepair.w)

        bird_yint = (self.y - self.r, self.y + self.r)
        pipepair_yint = (0, pipepair.h)

        # print(bird_xint, bird_yint)
        # print("\t", pipepair_xint, pipepair_yint)
        # print(overlap(bird_xint, pipepair_xint), overlap(bird_yint, pipepair_yint))
        # print()

        return overlap(bird_xint, pipepair_xint) and overlap(bird_yint, pipepair_yint)


class Model:
    def __init__(self, sc_width: int, sc_height: int):
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.bird = Bird(sc_width // 2, sc_height // 2, 15)
        self.pipes = [
            PipePair(sc_width + i * (sc_width // 2), 0, 25, 60)
            for i in range(1, 15 + 1)
        ]
        self.score = 0

    def update(self, space_was_pressed: bool) -> None:
        # how does the game stop
        if self.bird.reached_bottom(self.sc_height):
            return

        if any(self.bird.collides_with(pipepair) for pipepair in self.pipes):
            return

        if space_was_pressed:
            self.bird.y -= 10
        else:
            self.bird.y += 1

        for pipe in self.pipes:
            pipe.x -= 2

            # how the score updates
            if pipe.x <= self.sc_width // 2 <= pipe.x + 2:
                self.score += 1
