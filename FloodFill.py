class FloodFill():

    theMap = None
    find = None
    replace = None
    steps = 0
    stepCallback = None

    def __init__(self, m, stepcb):
        self.theMap = m
        self.stepCallback = stepcb

    def doFill(self, pos):
        if self.theMap[pos[1]][pos[0]] == self.find:
            self.theMap[pos[1]][pos[0]] = self.replace
            return True
        return False

    def Run(self, startx, starty, findvalue, replacevalue):
        self.find = findvalue
        self.replace = replacevalue
        self.steps = 0

        if self.theMap[starty][startx] == self.replace:
            print("A")
            return

        if self.theMap[starty][startx] != self.find:
            print("B")
            return

        if self.theMap[starty][startx] == self.find:
            self.theMap[starty][startx] = self.replace
        
        q = []
        q.append((startx, starty))

        while len(q) > 0:
            curx = q[0][0]
            cury = q[0][1]
            q = q[1:]

            west = (curx + 1, cury)
            east = (curx - 1, cury)
            north = (curx, cury - 1)
            south = (curx, cury + 1)

            filledSome = False
            if self.doFill(west):
                q.append(west)
                filledSome = True
            if self.doFill(east):
                q.append(east)
                filledSome = True
            if self.doFill(north):
                q.append(north)
                filledSome = True
            if self.doFill(south):
                q.append(south)
                filledSome = True

            if filledSome:            
                self.steps += 1

            if self.stepCallback != None:
                self.stepCallback(curx, cury)

    def Run2(self, startx, starty, findvalue, replacevalue):
        ''' Special Oxygen Fill '''
        self.find = findvalue
        self.replace = replacevalue
        self.steps = 0

        if self.theMap[starty][startx] == self.replace:
            print("A")
            return

        if self.theMap[starty][startx] != self.find:
            print("B")
            return

        if self.theMap[starty][startx] == self.find:
            self.theMap[starty][startx] = self.replace
        
        q = []
        q.append((startx, starty))

        while True:

            newposses = []
            filledSome = False
            for qq in q:
                curx = qq[0]
                cury = qq[1]

                west = (curx + 1, cury)
                east = (curx - 1, cury)
                north = (curx, cury - 1)
                south = (curx, cury + 1)

                if self.doFill(west):
                    newposses.append(west)
                    filledSome = True
                if self.doFill(east):
                    newposses.append(east)
                    filledSome = True
                if self.doFill(north):
                    newposses.append(north)
                    filledSome = True
                if self.doFill(south):
                    newposses.append(south)
                    filledSome = True

            if self.stepCallback != None:
                self.stepCallback(curx, cury)

            q = q + newposses

            if filledSome:            
                self.steps += 1
            else:
                break

