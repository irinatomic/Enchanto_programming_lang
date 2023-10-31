from lexer.regexes import RegexCollection
from loader.loader import open_file
from lexer.lexer import lex

def main():
    file_path = "./examples/07.ench"
    file_contents = open_file(file_path)

    words = lex(file_contents)

if __name__ == "__main__":
    main()
