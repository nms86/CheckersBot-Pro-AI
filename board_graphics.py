import pygame


class Graphics:
    win = None
    window_size_x = 450
    window_size_y = 450
    offset_from_corner = 7
    board_square_size = 56

    def initialize_window():
        if Graphics.win is None:
            scrn = pygame.display.set_mode(
                (Graphics.window_size_x, Graphics.window_size_y)
            )
            Graphics.win = scrn
            pygame.display.set_caption("CheckersBot Pro AI")
    
    def draw_moves(moves):
        for x, y, _ in moves:
            pygame.draw.circle(Graphics.win, (255, 0, 0), (y * Graphics.board_square_size + 28 ,x * Graphics.board_square_size + 28), 10)
        pygame.display.flip()
        

    def draw_board(board_to_display):
        Graphics.initialize_window()
        offset_from_corner = 7
        board_square_size = 56

        board = pygame.image.load("image_files/board.png")
        white_piece = pygame.image.load("image_files/white_piece.png")
        black_piece = pygame.image.load("image_files/black_piece.png")
        white_king_piece = pygame.image.load("image_files/white_king_piece.png")
        black_king_piece = pygame.image.load("image_files/black_king_piece.png")

        Graphics.win.blit(board, (0, 0))
        for i in range(len(board_to_display)):
            for j in range(len(board_to_display[0])):
                x = offset_from_corner + j * board_square_size
                y = offset_from_corner + i * board_square_size

                if board_to_display[i][j] == 1:
                    Graphics.win.blit(white_piece, (x, y))
                elif board_to_display[i][j] == 2:
                    Graphics.win.blit(black_piece, (x, y))
                elif board_to_display[i][j] == 3:
                    Graphics.win.blit(white_king_piece, (x, y))
                elif board_to_display[i][j] == 4:
                    Graphics.win.blit(black_king_piece, (x, y))

        pygame.display.flip()

    