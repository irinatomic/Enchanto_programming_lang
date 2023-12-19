# if we leave a comma at the end of the enum, it will be a 1 element tuple

class WordType:
    # data types
    INCANTUM = 'intcantum'
    DUBLATUM = 'dublatum'
    CHARMAX = 'charmax'
    STRINGO = 'stringo'
    ARRAYGO = 'arraygo'
    # basic functions
    ENCHANTO = 'main'     
    DECLARO = 'declaro' 
    SCRIPTUM = 'scriptum'           
    REVELIO = 'revelio'   
    # operators         
    ASSIGN = '='
    VARIABLE = 'variable'
    CHARACTER = 'char'
    NUMBER = 'number'
    STRING = 'string'
    # arithmetic operators
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'
    # unary operators
    ASCENDO = 'ascendo'
    DESCENDO = 'descendo'
    # ternary operator
    TRIBUS = 'tribus'
    # relational operators
    EQUAL = '=='
    NOT_EQUAL = '!='
    GREATER_THAN = '>'
    LESS_THAN = '<'
    GREATER_THAN_EQUAL = '>='
    LESS_THAN_EQUAL = '<='
    # logical operators
    ANDUS = 'andus'
    ORUS = 'orus'
    NOTUS = 'notus'
    # flow controls
    MYSTIME = 'mystime'             
    TURNTIME = 'turntime'                
    RETURNTIME = 'returntime'           
    FORCULUS = 'forculus'                  
    WHILEGARDIUM = 'whilegardium'
    # other
    OPEN_PARENTHESIS = '('
    CLOSE_PARENTHESIS = ')'
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    TERNARY_THEN = '?'
    TERNARY_ELSE = ':'
    SEMICOLON = ';'
    NEWLINE = 'newline'
    DU = 'du'   
    TU = 'tu'
    COMMA = ','
    # special case -> 
    LENGTH_FUNCTION = 'length_function'              # for array and string
    ARRAY_SIZE = 'array_size'                        # when declaring the array
    ARRAY_ELEMENT = 'array_element'                  # when getting the i'th element
