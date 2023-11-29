import pygame


def draw_board(board_to_display):
    window_size_x = 450
    window_size_y = 450
    offset_from_corner = 7

    scrn = pygame.display.set_mode((window_size_x, window_size_y))
    pygame.display.set_caption("CheckersBot Pro AI")

    board = pygame.image.load("image_files/board.png")
    white_piece = pygame.image.load("image_files/white_piece.png")
    black_piece = pygame.image.load("image_files/black_piece.png")

    scrn.blit(board, (0, 0))

    for i in range(len(board_to_display)):
        for j in range(len(board_to_display[0])):
            x = offset_from_corner + j * 56
            y = offset_from_corner + i * 56
            if board_to_display[i][j] == 1:
                scrn.blit(white_piece, (x, y))
            elif board_to_display[i][j] == 2:
                scrn.blit(black_piece, (x, y))

    pygame.display.flip()
