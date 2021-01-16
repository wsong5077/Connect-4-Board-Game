# Connect 4 Game Board
#weijia

class Board:
    """Class that defines a Connect 4 Board."""

    def __init__(self, width = 7, height = 6):
        """The constructor for objects of type Board"""
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board
        """
        s = ''                  # The string to return
        for row in range(self.height):
            s += '|'            # Add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # Add the bottom of the board
        s += '-\n'
        for col in range(self.width):
            s += ' ' + str(col%10)
        s += '\n'
        return s                # The board is complete, return it

    def addMove(self, col, ox):
        """Add the game piece ox (either 'X' or 'O') to column col."""
        for i in range(self.height):
            if self.data[self.height-1-i][col]==' ':
                self.data[self.height-1-i][col]=ox
                break

    def clear(self):
        """Clear the game board of all game pieces."""
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col]!=' ':
                    self.data[row][col]=' '

    def setBoard(self, moves):
        """Set the board using an input string representation."""
        for i in range(0,len(moves)):
            indice=int(moves[i])
            if i%2==0: self.addMove(indice, 'X')
            elif i%2==1: self.addMove(indice, 'O')

    def allowsMove(self, col):
        """Return True if adding a game piece in the given column is 
           permitted and return False otherwise."""
        row=self.height-1
        while True:
            row-=1
            if row==-1: 
                return False
                break
            elif self.data[row][col]!=' ': 
                continue
            elif self.data[row][col]==' ': 
                return True
                break

    def isFull(self):
        """Return True if the game board is full and False otherwise."""
        s=0
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col]==' ':
                    s+=1
        if s>0: return False
        else: return True

    def delMove(self, col):
        """Delete the topmost game piece from the given column."""
        for row in range(self.height):
            if self.data[row][col]!=' ': 
                self.data[row][col]=' '
                break

    def winsFor(self, ox):
        """Return True if the game has been won by player ox where ox
           is either 'X' or 'O'."""
        for col in range(self.width):
            for row in range(self.height-3):
                if self.data[row][col]==ox and self.data[row+1][col]==ox and self.data[row+2][col]==ox and self.data[row+3][col]==ox:
                    return True
                
        for row in range(self.height):
            for col in range(self.width-3):
                if self.data[row][col]==ox and self.data[row][col+1]==ox and self.data[row][col+2]==ox and self.data[row][col+3]==ox:
                    return True
                
        for row in range(self.height-3):
            for col in range(3, self.width):
                if self.data[row][col]==ox and self.data[row+1][col-1]==ox and self.data[row+2][col-2]==ox and self.data[row+3][col-3]==ox:
                    return True
                
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[row][col]==ox and self.data[row+1][col+1]==ox and self.data[row+2][col+2]==ox and self.data[row+3][col+3]==ox:
                    return True

        return False
        
        
        
        