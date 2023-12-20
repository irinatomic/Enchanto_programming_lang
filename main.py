from loader.loader import open_file
from lexer.lexer import lex
from grammar.main import process_grammar
from parser.parser import check_syntax

def main():

    # Load
    file_path = "./examples/00.ench"
    file_contents = open_file(file_path)

    # Lexer
    words = lex(file_contents)
    words = [word.word_type for word in words]
    words.append('#')

    # Test on a simple grammar for grammar/example/grammar.txt
    # words = ['if', '(', 'cond', 'and', 'cond', ')', 'body', 'else', 'body', '#']

    # Generate grammar states
    grammar_path = "./grammar/enchanto/grammar.txt"
    states = process_grammar(grammar_path)

    # Check syntax
    correct = check_syntax(words, states)
    print(correct)

if __name__ == "__main__":
    main()
