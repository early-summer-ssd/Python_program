class Module:
    Blank = 'N'

    def __init__(self):
        self.ThisColumn = None
        self.BlankFound = None
        self.Valid = None
        self.ColumnNumber = None
        self.Board = None
        self.WinnerFound = None
        self.ThisPlayer = None
        self.ThisRow = None
        self.ValidColumn = None
        self.GameFinished = None
        self.ValidRow = None

        self.InitialiseBoard()
        self.SetUpGame()
        self.OutPutBoard()
        while not self.GameFinished:
            self.PlayerMakesMove()
            self.OutPutBoard()
            self.CheckGameFinished()
            if not self.GameFinished:
                self.SwapThisPlayer()

    def InitialiseBoard(self):
        self.Board = [[Module.Blank for _ in range(7)] for _ in range(6)]

    def SetUpGame(self):
        self.ThisPlayer = 'O'
        self.GameFinished = False

    def OutPutBoard(self):
        for Row in range(5, -1, -1):
            for Column in range(7):
                print(self.Board[Row][Column], end=' ')
            print("")

    def PlayerMakesMove(self):
        self.ValidColumn = self.PlayerChoosesColum()
        self.ValidRow = self.FindFreeRow()
        self.Board[self.ValidRow][self.ValidColumn] = self.ThisPlayer

    def PlayerChoosesColum(self):
        print(f"Player {self.ThisPlayer}'s turn")
        while True:
            self.ColumnNumber = int(input('Enter a valid column number: '))
            if self.ColumnNumberValid():
                break
        return self.ColumnNumber

    def ColumnNumberValid(self):
        self.Valid = False
        if 0 <= self.ColumnNumber <= 6:
            if self.Board[5][self.ColumnNumber] == Module.Blank:
                self.Valid = True
        return self.Valid

    def FindFreeRow(self):
        self.ThisRow = 0
        while self.Board[self.ThisRow][self.ValidColumn] != Module.Blank:
            self.ThisRow += 1
        return self.ThisRow

    def CheckGameFinished(self):
        self.WinnerFound = False
        self.CheckIfPlayerHasWon()
        if self.WinnerFound:
            self.GameFinished = True
            print(f"{self.ThisPlayer} is the winner")
        else:
            self.CheckForFullBoard()

    def CheckIfPlayerHasWon(self):
        self.WinnerFound = False
        self.CheckHorizontalLine()
        if not self.WinnerFound:
            self.CheckVerticalLine()

    def CheckHorizontalLine(self):
        for i in range(4):
            if self.Board[self.ValidRow][i] == self.ThisPlayer and self.Board[self.ValidRow][
                i + 1] == self.ThisPlayer and self.Board[self.ValidRow][i + 2] == self.ThisPlayer and \
                    self.Board[self.ValidRow][i + 3] == self.ThisPlayer:
                self.WinnerFound = True

    def CheckVerticalLine(self):
        if self.ValidRow == 3 or self.ValidRow == 4 or self.ValidRow == 5:
            if self.Board[self.ValidRow][self.ValidColumn] == self.ThisPlayer and self.Board[self.ValidRow - 1][
                self.ValidColumn] == self.ThisPlayer and self.Board[self.ValidRow - 2][
                self.ValidColumn] == self.ThisPlayer and self.Board[self.ValidRow - 3][
                self.ValidColumn] == self.ThisPlayer:
                self.WinnerFound = True

    def CheckForFullBoard(self):
        self.BlankFound = False
        self.ThisRow = -1
        while True:
            self.ThisColumn = 0
            self.ThisRow += 1
            while True:
                self.ThisColumn += 1
                if self.Board[self.ThisRow][self.ThisColumn] == Module.Blank:
                    self.BlankFound = True
                # Until
                if self.ThisColumn == 6 or self.BlankFound:
                    break
            if self.ThisRow == 5 or self.BlankFound:
                break
        if not self.BlankFound:
            print("It is a draw")
            self.GameFinished = True

    def SwapThisPlayer(self):
        if self.ThisPlayer == 'O':
            self.ThisPlayer = 'X'
        else:
            self.ThisPlayer = 'O'


if __name__ == '__main__':
    Module()
