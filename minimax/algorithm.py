from copy import deepcopy
import pygame

def minimax(board, depth, max_player, game):
  if depth == 0 or board.winner() != None:
    return board.evaluate(), board


  if max_player:
    maxEval = float('-inf')
    best_move = None
    for move in get_all_moves(board, 1):      # May be able to replace get_all_moves with get_valid_boards
      evaluation = minimax(move, depth-1, False)[0]
      maxEval = max(maxEval, evaluation)
      if maxEval == evaluation:
        best_move = move

    return maxEval, best_move
  
  else:
    minEval = float('inf')
    best_move = None
    for move in get_all_moves(board, 2):      # May be able to replace get_all_moves with get_valid_boards
      evaluation = minimax(move, depth-1, True)[0]
      minEval = min(maxEval, evaluation)
      if minEval == evaluation:
        best_move = move

    return minEval, best_move


"""
Given a board, a piece location, a move location, and a capture list, simulates the move 
on a copy of the board and returns it, with captured pieces removed.
"""

def sim_move(x, y, move, board, capture):
  board.move_piece(x, y, move[0], move[1])
  if capture:
    for x,y in capture:               # Dependent on change to incorporate doubles/triples in get_valid_moves
      board.remove_piece(x,y)
  return board


"""
Given a board and a color, returns a list of all possible moves in the form of
new boards.
"""

def get_all_moves(board, color):          #May be able to replace with get_valid_boards
  moves = []

  for x,y in board.get_piece_locations(color):
    valid_moves = board.get_valid_moves(x, y, board)
    for move, capture in valid_moves.items():     # May need to change this for doubles/triples
      temp_board = deepcopy(board)
      new_board = sim_move(x, y, move, temp_board, capture)
      moves.append(new_board)

  return moves

