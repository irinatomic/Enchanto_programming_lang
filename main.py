from loader.loader import open_file
from lexer.lexer import lex
from grammar.main import process_grammar

def main():
    file_path = "./examples/00.ench"
    file_contents = open_file(file_path)

    # Lexer
    words = lex(file_contents)

    # Generate grammar states
    states = process_grammar()


if __name__ == "__main__":
    main()
