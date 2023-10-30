from lexer.regexes import RegexCollection

# RegexCollection -> holds list of regexes
regex_collection = RegexCollection()
regexes = regex_collection.init_regex()

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

    # if file_contents is not None:
    #     print(file_contents)

    test_code = "incantum x = 42 ; mystime ( x > 10 ) { scriptum x ; }"
    words = test_code.split(" ")
    for word in words:
        for regex in regexes:
            if regex.matches(word):
                print(f"Found {word} : {regex.word_type}")
                break

if __name__ == "__main__":
    main()
