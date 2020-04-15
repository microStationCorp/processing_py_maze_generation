w = 30
cells = []
stack = []

class Cell:

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.visited = False
        self.wall = [True, True, True, True]

    def unvisitedAdj(self):
        adj = []
        if not self.isVisited(self.r - 1, self.c):
            adj.append(cells[(self.r - 1) * (height / w) + self.c])
        if not self.isVisited(self.r, self.c + 1):
            adj.append(cells[(self.r) * (height / w) + (self.c + 1)])
        if not self.isVisited(self.r + 1, self.c):
            adj.append(cells[(self.r + 1) * (height / w) + (self.c)])
        if not self.isVisited(self.r, self.c - 1):
            adj.append(cells[(self.r) * (height / w) + (self.c - 1)])

        if len(adj) != 0:
            return adj[floor(random(len(adj)))]

    def isVisited(self, r, c):
        global w, cells
        if r < 0 or c < 0 or r == (height / w) or c == (width / w):
            return True
        else:
            return cells[r * (height / w) + c].visited

    def show(self):
        global w
        if not self.visited:
            stroke(255)
            strokeWeight(1)
        else:
            stroke(255,200,100)
            strokeWeight(2)
        if self.wall[0]:
            line(self.c * w, self.r * w, self.c * w+w, self.r * w)
        if self.wall[1]:
            line(self.c * w + w, self.r * w, self.c * w + w, self.r * w + w)
        if self.wall[2]:
            line(self.c * w, self.r * w+w, self.c * w + w, self.r * w+w)
        if self.wall[3]:
            line(self.c * w, self.r * w, self.c * w, self.r * w + w)


def setup():
    global current
    frameRate(30)
    size(600, 600)
    for r in range(0, height / w):
        for c in range(0, width / w):
            cells.append(Cell(r, c))
    current = cells[0]
    current.visited = True


def draw():
    global current, w, cells,stack
    background(51)
    for c in cells:
        c.show()

    fill(255, 0, 255, 50)
    noStroke()
    rect(current.c * w, current.r * w, w, w)

    next = current.unvisitedAdj()

    if next is not None:
        next.visited = True
        stack.append(current)
        removeWall(current, next)
        current = next
    elif len(stack)!=0:
        current=stack.pop()

def removeWall(c, n):
    x = c.r - n.r
    if x > 0:
        c.wall[0] = False
        n.wall[2] = False
    elif x < 0:
        c.wall[2] = False
        n.wall[0] = False
    y = c.c - n.c
    if y > 0:
        c.wall[3] = False
        n.wall[1] = False
    elif y < 0:
        c.wall[1] = False
        n.wall[3] = False
