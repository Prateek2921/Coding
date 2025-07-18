import cv2
import chess
import chess.engine
import numpy as np

# Path to stockfish binary
STOCKFISH_PATH = "/path/to/stockfish"

# Load the image from camera or file
def get_chessboard_image():
    cap = cv2.VideoCapture(0)
    print("Press 's' to capture chessboard image.")
    while True:
        ret, frame = cap.read()
        cv2.imshow("Camera - Chessboard View", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cap.release()
            cv2.destroyAllWindows()
            return frame

# Dummy function for detecting board state (to be replaced with ML/CV detection)
def get_fen_from_image(image):
    # For now, return default FEN (start position)
    return chess.STARTING_FEN

# Get move from stockfish
def get_ai_move(fen, ai_color):
    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    result = engine.play(board, chess.engine.Limit(time=1.0))
    move = result.move
    engine.quit()
    return move

# Main flow
def main():
    print("🎥 Capturing chessboard...")
    image = get_chessboard_image()

    print("🧠 Detecting board position...")
    fen = get_fen_from_image(image)
    print("Current FEN:", fen)

    color = input("Which color is the AI? (white/black): ").strip().lower()
    ai_color = chess.WHITE if color == 'white' else chess.BLACK

    board = chess.Board(fen)
    if board.turn == ai_color:
        move = get_ai_move(fen, ai_color)
        print(f"🤖 AI ({color}) recommends move: {move.uci()}")
        board.push(move)
        print(board)
    else:
        print("It's your turn! Make your move and then capture again.")

if __name__ == "__main__":
    main()
