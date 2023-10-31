from lexer.regexes import RegexCollection
from loader.loader import open_file
from lexer.lexer import lex

def main():
    file_path = "./examples/00.ench"
    file_contents = open_file(file_path)

    words = lex(file_contents)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
