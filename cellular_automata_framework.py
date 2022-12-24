#a framework for implementing cellular automata of different rulesets
#2D
#for now, simple 1 or 0 values

import copy

class cellular_automata:
    
    def __init__(self, width, height, function, board = None, wraparound = False, boundary = 0, history = False, check_history = False):
            self.width = width
            self.height = height
            self.function = function
            self.terminated = False
            #maybe check if cycling as well?
            self.wraparound = wraparound
            self.boundary = boundary
            self.iteration = 0
            self.cycle = -1
            self.cycling = False

            if board != None:
                self.loadBoard(board)
            else:
                self.board = [[0 for x in range(0, self.width)] for y in range(0, self.height)]
            
            self.input = copy.deepcopy(self.board)

            self.history = history
            self.check_history = check_history
            self.previous_states = []

    def loadBoard(self, board):
        if len(board) == self.height:
            if len(board[0]) == self.width:
                self.board = board
                self.board = [[board[y][x] for y in range(len(board[0]))] for x in range(len(board))]
    
    def iterate(self):
        if not self.terminated and not self.cycling:
            currentBoard = copy.deepcopy(self.board)

            for y in range(0, len(self.board)):
                for x in range(0, len(self.board[y])):
                    currentBoard[y][x] = self.function(x, y, self)

            if self.history:
                self.previous_states.insert(0, self.board)

            if currentBoard == self.board:
                    self.terminated = True
                
            if self.check_history and not self.terminated:
                for i in range(len(self.previous_states)):
                    if currentBoard == self.previous_states[i]:
                        self.cycling = True
                        self.cycle = i + 1
                        break
                
            self.board = currentBoard
            self.iteration += 1

    def getBoard(self):
        return self.board

    def getPrintableBoardString(self):
        bs = ''
        
        for y in range(0, len(self.board)):
            bs += f'{y}:\t'
            for x in range(0, len(self.board[y])):
                bs += str(self.board[y][x])
            bs += '\n'
        
        return bs
    
    def printBoard(self):
        print(self.getPrintableBoardString())

    def getCell(self, x, y):
        if self.wraparound:
            x = x % self.width
            y = y % self.height
            return self.board[y][x]
        else:
            if x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1:
                return self.boundary
            else:
                return self.board[y][x]

    def isComplete(self):
        return self.cycling or self.terminated