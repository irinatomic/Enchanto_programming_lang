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