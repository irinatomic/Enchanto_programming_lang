from lexer.regexes import RegexCollection

# RegexCollection -> holds list of regexes
regex_collection = RegexCollection()
regexes = regex_collection.init_regex()

def preprocess_code(code):
    code = code.replace("(", " ( ")
    code = code.replace(")", " ) ")
    code = code.replace("{", " { ")
    code = code.replace("}", " } ")
    code = code.replace("[", " [ ")
    code = code.replace("]", " ] ")
    code = code.replace(";", " ; ")
    code = code.replace("\n", " ")
    return code

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
    file_path = "./examples/01.ench"
    file_contents = open_file(file_path)

    if file_contents is not None:
        code = preprocess_code(file_contents)
        code = code.split(" ")
        for word in code:
            for regex in regexes:
                if regex.matches(word):
                    print(f"{word} : {regex.word_type}")
                    break

    # test_code = 'incantum x = "malo_sasavo" ; mystime ( x > 10 ) { scriptum x ; }'

if __name__ == "__main__":
    main()
