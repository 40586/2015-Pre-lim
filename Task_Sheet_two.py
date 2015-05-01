# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

##def GetTypeOfGame(): #task one
##    cont = False
##    while cont == False:
##        TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
##        if TypeOfGame[0].upper() == 'Y':
##            cont = True
##            TypeOfGame = TypeOfGame[0].upper()
##        if TypeOfGame[0].upper() == 'N':
##            cont = True
##            TypeOfGame = TypeOfGame[0].upper()
##        else:
##            print('Please enter Y or N')
##    return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     _______________________")
    print('R{0}'.format(RankNo),end="  ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     _______________________")
  print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  range_check = ['17','27','37','47','57','67','77','87','12','22','32','42','52','62','72','82']
  #elif StartRank+StartFile in range_check:
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): #Task 17
  CheckNabuMoveIsLegal = False
  check_move = [1,2,3,4,5,6,7,8]
  if abs(FinishFile - StartFile) in check_move and abs(FinishRank - StartRank) in check_move:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): #Issue here i don't understand, some move that fit this dont work
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  elif (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) or (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  elif (0 > FinishRank > 9) or (0 > FinishFile > 9): #Task 2
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame): # Task 14
  if SampleGame == 'Y':
    initialise_sample_board(Board)
  else:
    initialise_new_board(Board)

def initialise_new_board(Board): # Task 14
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
      else:
        Board[RankNo][FileNo] = "  "

def initialise_sample_board(Board): # Task 14
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"
              
def GetMove(StartSquare, FinishSquare): # Task 3
  temp = False
  surr = False
  confirm = False # Task 4
  while confirm == False:
    cont = False
    while not cont:
      try:
        StartSquare = int(input("Enter coordinates of square containing piece to move (file first)(-1 to open menu): "))
        temp1 = StartSquare // 10
        if StartSquare == -1:
          in_game_menu() #Task 12 edits
          temp, surr = get_ingame_choice()
          cont = temp
        elif temp1 < 1:
          print('Please enter both the FILE and RANK ')
        elif ( '0' > str(StartSquare)[:1] > '9' ):
          cont = False
          print('Please enter a valid File (1-8)')
        elif ( '0' > str(StartSquare)[1:] > '9' ):
          cont = False
          print('Please enter a valid Rank (1-8)')
        else:
          cont = True
      except ValueError:
        print('Please enter a number')
    cont = temp
    while not cont:
      try:
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first)(-1 to open menu): "))
        temp1 = FinishSquare // 10
        if StartSquare == -1:
          in_game_menu()
          temp , surr = get_ingame_choice() #Task 12 edits
          cont = temp
        elif temp1 < 1:
          print('Please enter both the FILE and RANK ')
        elif ( '0' > str(FinishSquare)[:1] > '9' ):
          cont = False
          print('Please enter a valid File (1-8)')
        elif ( '0' > str(FinishSquare)[1:] > '9' ):
          cont = False
          print('Please enter a valid Rank (1-8)')
        else:
          cont = True
      except ValueError:
        print('Please enter a number')
      confirm = ConfirmMove(StartSquare, FinishSquare)
    if temp == True:
      confirm = True
  return surr, temp, StartSquare, FinishSquare ###

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if Board[FinishRank][FinishFile] !=' ':
    GetPieceName(Board,StartRank,StartFile,FinishRank,FinishFile)
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print('The White Redum has been promoted!') #Task 6
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print('The Black Redum has been promoted!')#Task 6
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

def ConfirmMove(StartSquare, FinishSquare): #Task 4
  print('Move from Rank {0}, File {1} to Rank {2}, File {3}?'.format(str(StartSquare)[:1] ,str(StartSquare)[1:] ,str(FinishSquare)[:1] ,str(FinishSquare)[1:]))
  cont = False
  while cont == False:
    temp = input('Confirm move?(Y/N): ')
    if temp[:1].lower() == 'y':
      cont = True
      confirm = True
    elif temp[:1].lower() == 'n':
      cont = True
      confirm = False
    else:
      print('Please enter a valid answer!')
  return confirm

def GetPieceName(Board,StartRank,StartFile,FinishRank,FinishFile):
  Print = True
  PieceType = Board[StartRank][StartFile][1]
  PieceColour = Board[StartRank][StartFile][0]
  PieceType1 = Board[FinishRank][FinishFile][1]
  PieceColour1 = Board[FinishRank][FinishFile][0]
  if PieceType == 'R':
    PrintPieceType = 'Redum'
  elif PieceType == 'S':
    PrintPieceType = 'Sarrum'
  elif PieceType == 'M':
    PrintPieceType = 'Marzaz'
  elif PieceType == 'G':
    PrintPieceType = 'Gigsgigir'
  elif PieceType == 'N':
    PrintPieceType = 'Nabu'
  elif PieceType == 'E':
    PrintPieceType = 'Etlu'
  if PieceColour == 'W':
    PrintPieceColour = 'White'
  elif PieceColour == 'B':
    PrintPieceColour = 'Black'
  else:
    Print = False
  if PieceType1 == 'R':
    PrintPieceType1 = 'Redum'
  elif PieceType1 == 'S':
    PrintPieceType1 = 'Sarrum'
  elif PieceType1 == 'M':
    PrintPieceType1 = 'Marzaz'
  elif PieceType1 == 'G':
    PrintPieceType1 = 'Gigsgigir'
  elif PieceType1 == 'N':
    PrintPieceType1 = 'Nabu'
  elif PieceType1 == 'E':
    PrintPieceType1 = 'Etlu'
  if PieceColour1 == 'W':
    PrintPieceColour1 = 'White'
  elif PieceColour1 == 'B':
    PrintPieceColour1 = 'Black'
  else:
    Print = False
  if Print == True:
    print('{0} {1} Takes {2} {3}'.format(PrintPieceColour,PrintPieceType,PrintPieceColour1,PrintPieceType1))

def display_menu():
  print('''

Main menu.
1.Start new game
2.Load existing game
3.Play sample game
4.View high scores
5.Settings
6.Quit Program
''')

def get_menu_selection():
  cont = False
  values = ['1','2','3','4','5','6']
  while not cont:
    value = input('Please make your choice: ')
    if value in values:
      cont = True
    else:
      print('Please make a valid choice!')
  return value

def play_game(SampleGame):
  temp = False
  surr = False
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    #SampleGame = GetTypeOfGame() #task one
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        surr, temp, StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare) ###
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = temp
        if not temp:
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      if not temp:
        MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if surr == True:
        GameOver = True
        DisplayWinner(WhoseTurn)
      if temp == True:
        GameOver = True
        PlayAgain = 'N'
      elif GameOver:
        DisplayWinner(WhoseTurn)
      elif WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    if surr == True:
      PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
      if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
        PlayAgain = chr(ord(PlayAgain) - 32)
        
  return temp


def make_selection(value):
  if value == '1':
    SampleGame = 'N'
    temp = play_game(SampleGame)
  elif value == '2':
    print('PLACEHOLDER')
  elif value == '3':
    SampleGame = 'Y'
    temp = play_game(SampleGame)
  elif value == '4':
    print('PLACEHOLDER')
  elif value == '5':
    print('PLACEHOLDER')
  elif value == '6':
    exit()
  return temp

def in_game_menu():
  print('''Menu:
1. Save game
2. Quit game
3. Return to game
4. Surrender
''')

def get_ingame_choice():
  cont = False
  values = ['1','2','3', '4']
  while not cont:
    value = input('Please enter selection: ')
    if value in values:
      temp, surr = perform_choice(value)
      cont = True
    else:
      print('Please choose a valid number!')
  return temp, surr
    

def perform_choice(value):
  if value == '1':
    print('PLACEHOLDER')
    temp = False
    surr = False
  if value == '2':
    temp = True
    surr = False
  if value == '3':
    print()
    temp = False
    surr = False
  if value == '4':
    surr = True
    temp = True
  return temp, surr
  
if __name__ == "__main__":
  temp = False
  while not temp:
    display_menu()
    value = get_menu_selection()
    temp1 = make_selection(value)
  
