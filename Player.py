#weijia
from Board import *
import random
class Player:
    """Class that defines a Connect 4 player."""

    def __init__(self, ox, tbt, ply):
        '''
        string ox will be either 'X' or 'O'
        tbt is a string representing the tiebreaking type of the player:either 'LEFT', 'RIGHT', or 'RANDOM'
        ply will be a nonnegative integer representing the number of moves that the player should look into the future
        '''
        self.symbol=ox
        self.tbt=tbt
        self.ply=ply

    def __repr__(self):
        output = ""
        output += "Player for " + self.symbol + "\n"
        output += "  with tiebreak: " + self.tieRule + "\n"
        output += "  and ply == " + str(self.ply) + "\n"
        return output
        
        
    def oppChar(self):
        """Return the opposite game piece character."""
        if self.symbol == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """Return the score for the given board b.
        100.0 if the board b is a win for self
        50.0 if it is neither a win nor a loss for self
        0.0 if it is a loss for self"""
        if self.symbol=='X':other='O'
        else:other='X'
        if b.winsFor(self.symbol)==True and b.winsFor(other)!=True: return 100.0
        elif b.winsFor(other)==True and b.winsFor(self.symbol)!=True: return 0.0
        else: return 50.0


    def tiebreakMove(self, scores):
        """Return column number of move based on self.tbt."""
        highest=max(scores)
        lst=[]
        for i in range(len(scores)):
            if scores[i]==highest: lst.append(i)
        if self.tbt== 'LEFT':
            return lst[0]
        if self.tbt==  'RIGHT':
            return lst[-1]
        if self.tbt==  'RANDOM':
            return random.choice(lst)

    def scoresFor(self, b):
        """Return a list of scores for board d, one score for each column
            of the board."""
        width=0
        for col in range(b.width):
            width+=1
        lst=[50.0]*width
        for col in range(b.width):
            if b.allowsMove(col)==False:
                lst[col]=-1.0
            elif self.scoreBoard(b)==100.0:
                lst[col]=100.0
            elif self.scoreBoard(b)==0.0:
                lst[col]=0.0
            elif self.ply==0:
                lst[col]=50.0
            else:
                b.addMove(col,self.symbol)
                if b.isFull()==True: 
                    lst[col]=50.0
                else:
                    lst_op_score=Player(self.oppChar(), self.tbt, self.ply-1).scoresFor(b)
                    lst[col]=100-max(lst_op_score)
                b.delMove(col)
        return lst

    def nextMove(self, b):
        """Accepts a board input and returns the next move for this player,
           where a move is a column in which the player should place its
           game piece."""
        scores=self.scoresFor(b)
        return self.tiebreakMove(scores)


	
