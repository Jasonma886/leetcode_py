class Solution(object):
    def __init__(self):
        self.direction = 0
        self.pos_x = 0
        self.pos_y = 0
        self.obstacles = []

    def changeDirection(self, di):
        # turn left
        if di % 2 == 0:
            self.direction -= 1
        # turn right
        else:
            self.direction += 1

    def forwardByDi(self, route):
        direction = self.direction % 4
        x, y = self.pos_x, self.pos_y

        if direction == 0:
            x += route
        elif direction == 1:
            y += route
        elif direction == 2:
            x -= route
        else:
            y -= route

        self.isObstacles((x, y))

    # check if the obstacles are on robot's way
    def isObstacles(self, after):
        obstacles = self.obstacles
        before = [self.pos_x, self.pos_y]


    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.obstacles = obstacles[:]
        for item in commands:
            if item < 0:
                self.changeDirection(item)
                continue
            self.forwardByDi(item)

        return (self.pos_x ** 2) + (self.pos_y ** 2)


def robotSim(commands, obstacles):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    ans = 0

    for cmd in commands:
        if cmd == -2:  #left
            di = (di - 1) % 4
        elif cmd == -1:  #right
            di = (di + 1) % 4
        else:
            for k in range(cmd):
                if (x+dx[di], y+dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x*x + y*y)

    return ans

if __name__ == '__main__':
    test = Solution()
    print(robotSim([4, -1, 3], [[2, 4]]))
