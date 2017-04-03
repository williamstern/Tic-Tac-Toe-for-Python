# Created by William Stern

def tieGame(Line1, Line2, Line3):
    '''
    Input: Line1, Line2, and Line3
    
    Output: True if there are no open spaces in any of the lines else False
    '''
    if ' ' not in Line1 and ' ' not in Line2 and ' ' not in Line3:
        return True
    else:
       return False

def gamewinPlayer(Line1, Line2, Line3):
    '''
    Input: Line1, Line2, and Line3
    
    Output:True if the player has won by getting 3 X's in 
    a row vertically, horizontally, or diagnoaly else false
    '''
    
    # Does the horizontal lines
    if Line1 == ['X', '|', 'X', '|', 'X'] \
    or Line2 == ['X', '|', 'X', '|', 'X'] \
    or Line3 == ['X', '|', 'X', '|', 'X']:
        return True
    
    # Does the columns
    if Line1[0] == 'X' and Line2[0] == 'X' and Line3[0] == 'X':
        return True
    if Line1[2] == 'X' and Line2[2] == 'X' and Line3[2] == 'X':
        return True
    if Line1[4] == 'X' and Line2[4] == 'X' and Line3[4] == 'X':
        return True
    
    # Does the diagnoal lines
    if Line1[0] == 'X' and Line2[2] == 'X' and Line3[4] == 'X':
        return True
    if Line1[4] == 'X' and Line2[2] == 'X' and Line3[0] == 'X':
        return True
    else:
        return False


def gamewinAI(Line1, Line2, Line3):
    '''
    Input: Line1, Line2, and Line3
    
    Output:True if the computer has won by getting 3 O's in 
    a row vertically, horizontally, or diagnoaly else false
    '''
    
    # Does the horizontal lines
    if Line1 == ['O', '|', 'O', '|', 'O'] \
    or Line3 == ['O', '|', 'O', '|', 'O'] \
    or Line3 == ['O', '|', 'O', '|', 'O']:
        return True
    
    # Does the columns
    if Line1[0] == 'O' and Line2[0] == 'O' and Line3[0] == 'O':
        return True
    if Line1[2] == 'O' and Line2[2] == '0' and Line3[2] == 'O':
        return True
    if Line1[4] == 'O' and Line2[4] == 'O' and Line3[4] == 'O':
        return True

    # Does the diagnoal lines
    if Line1[0] == 'O' and Line2[2] == 'O' and Line3[4] == 'O':
        return True
    if Line1[4] == 'O' and Line2[2] == 'O' and Line3[0] == 'O':
        return True
    else:
        return False

def winningAI(Line1, Line2, Line3):
   '''
   Input: Line1, Line2, and Line3

   Output: If there are two X's in a row and the third slot is an open space 
   it changes the third slot into an X
   '''
   
   # Line1
   # Counts up the number of 'O' and ' ' in Line1.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   if True:
      counterO = 0
      counterSpace = 0
      for i in Line1:
         if i == 'O':
            counterO += 1
         if i == ' ':
            counterSpace += 1
      if counterO == 2 and counterSpace == 1:
         zom = Line1.index(' ')
         Line1[zom] = 'O'
         return Line1, Line2, Line3

   # Line2
   # Counts up the number of 'O' and ' ' in Line2.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   elif True:
      counterO = 0
      counterSpace = 0
      for i in Line2:
         if i == 'O':
               counterO += 1
         if i == ' ':
            counterSpace += 1
      if counterO == 2 and counterSpace == 1:
         zom = Line2.index(' ')
         Line2[zom] = 'O'
         return Line1, Line2, Line3
   
   # Line3
   # Counts up the number of 'O' and ' ' in Line3.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines.  
   elif True:
      counterO = 0
      counterSpace = 0
      for i in Line3:
         if i == 'O':
            counterO += 1
         if i == ' ':
            counterSpace += 1
      if counterO == 2 and counterSpace == 1:
         zom = Line3.index(' ')
         Line3[zom] = 'O'
         return Line1, Line2, Line3
         
   # DiagIncline
   #['X', '|', 'X', '|', 'X']
   # Counts up the number of 'O' and ' ' in DiagIncline
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   elif True:
      DiagIncline = Line3[0] + Line2[2] + Line1[4]
      counterSpace = 0
      counterO = 0
      spacePlace = 5
      for i in DiagIncline:
         if i == ' ':
            counterSpace += 1
         if i == 'O':
            counterO +=1
      if counterSpace == 1 and counterO == 2:
         spacePlace = DiagIncline.index(' ')

      if spacePlace == 0:
         Line3[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[4] = 'O'
         return Line1, Line2, Line3
         
      
         
   # DiagDecline
   #['X', '|', 'X', '|', 'X']
   # Counts up the number of 'O' and ' ' in DiagDecline
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   elif True:
      DiagDecline = Line3[4] + Line2[2] + Line1[0]
      counterSpace = 0
      counterO = 0
      spacePlace = 5
      for i in DiagDecline:
         if i == ' ':
            counterSpace += 1
         if i == 'O':
            counterO +=1
      if counterSpace == 1 and counterO == 2:
         spacePlace = DiagIncline.index(' ')

      if spacePlace == 0:
         Line3[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[0] = 'O'
         return Line1, Line2, Line3
         
       
   # columnLeft
   # Counts up the number of 'O' and ' ' in columnLeft.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   elif True:
      columnLeft = Line3[0] + Line2[0] + Line1[0]
      counterSpace = 0
      counterO = 0
      spacePlace = 5
      for i in columnLeft:
         if i == ' ':
            counterSpace += 1
         if i == 'O':
            counterO +=1
      if counterSpace == 1 and counterO == 2:
         spacePlace = columnLeft.index(' ')

      if spacePlace == 0:
         Line3[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[0] = 'O'
         return Line1, Line2, Line3
         
         
   # columnMid
   # Counts up the number of 'O' and ' ' in columnMid.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines.    
   elif True:
      columnMid = Line3[2] + Line2[2] + Line1[2]
      counterSpace = 0
      counterO = 0
      spacePlace = 5
      for i in columnMid:
         if i == ' ':
            counterSpace += 1
         if i == 'O':
            counterO +=1
      if counterSpace == 1 and counterO == 2:
         spacePlace = columnMid.index(' ')

      if spacePlace == 0:
         Line3[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[2] = 'O'
         return Line1, Line2, Line3
         
         
   # columnRight
   # Counts up the number of 'O' and ' ' in columnRight.
   # If there are two 'O's and one ' ' then changes the ' ' to 'O' and returns all three lines.  
   elif True:
      columnRight = Line3[4] + Line2[4] + Line1[4]
      counterSpace = 0
      counterO = 0
      spacePlace = 5
      for i in columnRight:
         if i == ' ':
            counterSpace += 1
         if i == 'O':
            counterO +=1
      if counterSpace == 1 and counterO == 2:
         spacePlace = columnRight.index(' ')

      if spacePlace == 0:
         Line3[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[4] = 'O'
         return Line1, Line2, Line3
      else:
         return False
   else:
       return False  

 
def blockAI(Line1, Line2, Line3):
   
   # Line1
   # Counts up the number of 'X' and ' ' in Line1.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   if True:
      counterX = 0
      counterSpace = 0
      for i in Line1:
         if i == 'X':
            counterX += 1
         if i == ' ':
            counterSpace += 1
      if counterX == 2 and counterSpace == 1:
         zom = Line1.index(' ')
         Line1[zom] = 'O'
         return Line1, Line2, Line3
            
   # Line2
   # Counts up the number of 'X' and ' ' in Line2.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   if True:
      counterX = 0
      counterSpace = 0
      for i in Line2:
         if i == 'X':
               counterX += 1
         if i == ' ':
            counterSpace += 1
      if counterX == 2 and counterSpace == 1:
         zom = Line2.index(' ')
         Line2[zom] = 'O'
         return Line1, Line2, Line3
         
   # Line3
   # Counts up the number of 'X' and ' ' in Line3.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   if True:
      counterX = 0
      counterSpace = 0
      for i in Line3:
         if i == 'X':
            counterX += 1
         if i == ' ':
            counterSpace += 1
      if counterX == 2 and counterSpace == 1:
         zom = Line3.index(' ')
         Line3[zom] = 'O'
         return Line1, Line2, Line3
         
   # DiagDecline
   # Counts up the number of 'X' and ' ' in DiagDecline
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   #['X', '|', 'X', '|', 'X']
   if True:
      DiagDecline = Line3[4] + Line2[2] + Line1[0]
      counterSpace = 0
      counterX = 0
      spacePlace = 5
      for i in DiagDecline:
         if i == ' ':
            counterSpace += 1
         if i == 'X':
            counterX +=1
      if counterSpace == 1 and counterX == 2:
         spacePlace = DiagDecline.index(' ')

      if spacePlace == 0:
         Line3[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[0] = 'O'
         return Line1, Line2, Line3
         
     
   # DiagIncline
   #['X', '|', 'X', '|', 'X']
   # Counts up the number of 'X' and ' ' in DiagIncline
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   if True:
      DiagIncline = Line3[0] + Line2[2] + Line1[4]
      counterSpace = 0
      counterX = 0
      spacePlace = 5
      for i in DiagIncline:
         if i == ' ':
            counterSpace += 1
         if i == 'X':
            counterX +=1
      if counterSpace == 1 and counterX == 2:
         spacePlace = DiagIncline.index(' ')
      
      if spacePlace == 0:
         Line3[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[4] = 'O'
         return Line1, Line2, Line3
         
   # columnLeft
   # Counts up the number of 'X' and ' ' in columnLeft.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   if True:
      columnLeft = Line3[0] + Line2[0] + Line1[0]
      counterSpace = 0
      counterX = 0
      spacePlace = 5
      for i in columnLeft:
         if i == ' ':
            counterSpace += 1
         if i == 'X':
            counterX +=1
      if counterSpace == 1 and counterX == 2:
         spacePlace = columnLeft.index(' ')

      if spacePlace == 0:
         Line3[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[0] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[0] = 'O'
         return Line1, Line2, Line3
         

   # columnMid
   # Counts up the number of 'X' and ' ' in columnMid.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines. 
   if True:
      columnMid = Line3[2] + Line2[2] + Line1[2]
      counterSpace = 0
      counterX = 0
      spacePlace = 5
      for i in columnMid:
         if i == ' ':
            counterSpace += 1
         if i == 'X':
            counterX +=1
      if counterSpace == 1 and counterX == 2:
         spacePlace = columnMid.index(' ')

      if spacePlace == 0:
         Line3[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[2] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[2] = 'O'
         return Line1, Line2, Line3
         
   
   # columnRight
   # Counts up the number of 'X' and ' ' in columnRight.
   # If there are two 'X's and one ' ' then changes the ' ' to 'O' and returns all three lines.
   if True:
      columnRight = Line3[4] + Line2[4] + Line1[4]
      counterSpace = 0
      counterX = 0
      spacePlace = 5
      for i in columnRight:
         if i == ' ':
            counterSpace += 1
         if i == 'X':
            counterX +=1
      if counterSpace == 1 and counterX == 2:
         spacePlace = columnRight.index(' ')

      if spacePlace == 0:
         Line3[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 1:
         Line2[4] = 'O'
         return Line1, Line2, Line3
      elif spacePlace == 2:
         Line1[4] = 'O'
         return Line1, Line2, Line3 
      else:
         return False


   # ['X', '|', 'X', '|', 'X']
   # [ 0    1    2    3    4 ] 
def normalAI(Line1, Line2, Line3):
   '''
   Input: Line1, Line2, and Line2
   
   Output: Line1, Line2, and Line3 with one ' ' made into an 'O'.
   It will do this by using a weighted randum number generator.
   '''
   # Generates a random number from 0 to 12
   from random import randint
   randomNum = randint(0, 12)
   sector = 0
   # The corner
   # If the number is 4 or less does this
   if randomNum <= 4:
      corner = [Line1[0], Line1[4], Line3[0], Line3[4]]
      if ' ' not in corner:
         normalAI(Line1, Line2, Line3)
      else:
         # Makes a random number and if that number corasponds  with an empty space changes it to 'O'
	 # Else restarts the function
         randnum = randint(0, 3)
         if corner[randnum] == ' ':
            zok = corner.index(' ')
            if zok == 0:
               Line1[0] = 'O'
            elif zok == 1:
               Line1[4] = 'O'
            elif zok == 2:
               Line3[0] = 'O'
            elif zok == 3:
               Line3[4] = 'O'
            return Line1, Line2, Line3
         else:
            normalAI(Line1, Line2, Line3)
   # The middle
   # If the number is between 5 and 7 and the middle's empty changes it to 'O'
   # Else restarts the function
   elif randomNum > 4 and randomNum <= 7:
      if Line2[2] == ' ':
         Line2[2] = 'O'
         return Line1, Line2, Line3
      else:
         normalAI(Line1, Line2, Line3)
   # The inside spaces
   # Same as above
   elif randomNum > 7:
      insideSpaces = [Line1[2], Line2[0], Line2[4], Line3[2]]
      if ' ' not in insideSpaces:
         normalAI(Line1, Line2, Line3)
      else:
         randnum = randint(0, 3)
         if insideSpaces[randnum] == ' ':
            zok = insideSpaces.index(' ')
            if zok == 0:
               Line1[2] = 'O'
            elif zok == 1:
               Line2[0] = 'O'
            elif zok == 2:
               Line2[4] = 'O'
            elif zok == 3:
               Line3[2] = 'O'
            return Line1, Line2, Line3
         else:
            normalAI(Line1, Line2, Line3)

# Define the Lines!
Line1 = [' ', '|', ' ', '|', ' ']
Line2 = [' ', '|', ' ', '|', ' ']
Line3 = [' ', '|', ' ', '|', ' ']
#GridLine = '-------------------------'


# Starts the game
def TicTacToe(Line1, Line2, Line3):
   ''' Starts a game of Tic Tac Toe'''
   try:
      while gamewinAI(Line1, Line2, Line3) == False \
      and gamewinPlayer(Line1, Line2, Line3) == False \
      and tieGame(Line1, Line2, Line3) == False:
         
         # This part makes it avaliable for the player to move
         foo = 1
         while foo == 1:
            openSpace = input("Please select a space: ")
            openSpace = openSpace.upper()
            
            if openSpace == 'A1' and Line1[0] == ' ':
               Line1[0] = 'X'
               foo = 0
            elif openSpace == 'A2' and Line1[2] == ' ':
               Line1[2] = 'X'
               foo = 0
            elif openSpace == 'A3' and Line1[4] == ' ':
               Line1[4] = 'X'
               foo = 0
            elif openSpace == 'B1' and Line2[0] == ' ':
               Line2[0] = 'X'
               foo = 0
            elif openSpace == 'B2' and Line2[2] == ' ':
               Line2[2] = 'X'
               foo = 0
            elif openSpace == 'B3' and Line2[4] == ' ':
               Line2[4] = 'X'
               foo = 0
            elif openSpace == 'C1' and Line3[0] == ' ':
               Line3[0] = 'X'
               foo = 0
            elif openSpace == 'C2' and Line3[2] == ' ':
               Line3[2] = 'X'
               foo = 0
            elif openSpace == 'C3' and Line3[4] == ' ':
               Line3[4] = 'X'
               foo = 0
            else:
               print("Please select a valid open space")
         

         # Says "You Won!" if you win   
         if gamewinPlayer(Line1, Line2, Line3) == True:
            print(Line1)
            print(Line2)
            print(Line3)
            print("Congratulations, you Won!")
            return
         

         # Runs the functions
         if winningAI(Line1, Line2, Line3):
            #winningAI(Line1, Line2, Line3)
            True
        
         elif blockAI(Line1, Line2, Line3):
            #blockAI(Line1, Line2, Line3)
            True
       
         else: 
            normalAI(Line1, Line2, Line3)
         
         # Says "You Lost" if you loose
         if gamewinAI(Line1, Line2, Line3) == True:
            print(Line1)
            print(Line2)
            print(Line3)
            print("Sorry, you Lost")
            return
            
            
         print(Line1)
         
         print(Line2)
         
         print(Line3)
   # This stops the tie game recursion error
   except RecursionError:
      print(Line1)
      print(Line2)
      print(Line3)
      print("Tie Game")
      return
# Starts the game
print('Welcome to Tic-tac-toe!')
print(Line1)
print(Line2)
print(Line3)
TicTacToe(Line1, Line2, Line3)

# Done!
