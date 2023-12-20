from loader.loader import open_file
from lexer.lexer import lex
from grammar.main import process_grammar
from parser.parser import check_syntax


def main():

    # Load
    file_path = "./examples/simple/00.txt"
    file_contents = open_file(file_path)

    # Lexer
    words = lex(file_contents)
    words = [word.word_type for word in words]

    # Generate grammar states
    grammar_path = "./grammar/example/grammar.txt"
    states = process_grammar(grammar_path)

    # Check syntax
    # check_syntax(words, states)

if __name__ == "__main__":
    main()
