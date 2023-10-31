from lexer.regexes import RegexCollection
import re

# RegexCollection -> holds list of regexes
regex_collection = RegexCollection()
regexes = regex_collection.init_regex()

def preprocess_code(input_string):
    
    # need spaces to the left and right
    target_chars = ['+', '-', '*', '/', '%', '!=', '==', '<=', '>=', '<', '>', '=', '(', ')', '{', '}', '[', ']', ';']

    # regex that matches any of the target chars or chars sequences
    pattern = '|'.join(re.escape(char) for char in target_chars)
    pattern = f"(?:{pattern})"
    single_quoted = r"'[^']*'"

    # replace matched characters with spaces to the left and right
    result = re.sub(pattern, r' \g<0> ', input_string)

    # exclude spaces within single quotes
    result = re.sub(single_quoted, lambda match: match.group(0).replace(' ', ''), result)

    result = result.replace("\n", " ")
    result = result.replace("\t", "")
    return result

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read() 
        return file_contents
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None 
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    file_path = "./examples/20.ench"
    file_contents = open_file(file_path)

    # input = "whilegardium broj > 1 andus c >= d du"

    if file_contents is not None:
        code = preprocess_code(file_contents)
        words = code.split(" ")
        for word in words:
            for regex in regexes:
                if regex.matches(word):
                    print(f"{word} : {regex.word_type}")
                    break

if __name__ == "__main__":
    main()
