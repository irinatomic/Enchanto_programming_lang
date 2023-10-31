# if we leave a comma at the end of the enum, it will be a 1 element tuple

class WordType:
    # data types
    INCANTUM = 'int'
    DUBLATUM = 'double'
    CHARMAX = 'char'
    STRINGO = 'string'
    ARRAYGO = 'array'
    # basic functions
    ENCHANTO = 'main'     
    DECLARO = 'declaration' 
    SCRIPTUM = 'input'                   
    REVELIO = 'print'   
    # operators         
    ASSIGN = 'assign'
    VARIABLE = 'variable'
    CHARACTER = 'character'
    NUMBER = 'number'
    STRING = 'full_string'
    # arithmetic operators
    PLUS = 'plus'
    MINUS = 'minus'
    MUL = 'mul'
    DIV = 'div'
    MOD = 'mod'
    # unary operators
    ASCENDO = 'increment'
    DESCENDO = 'decrement'
    # ternary operator
    TRIBUS = 'ternary'
    # relational operators
    EQUAL = 'equal'
    NOT_EQUAL = 'not_equal'
    GREATER_THAN = 'greater_than'
    LESS_THAN = 'less_than'
    GREATER_THAN_EQUAL = 'greater_than_equal'
    LESS_THAN_EQUAL = 'less_than_equal'
    # logical operators
    ANDUS = 'and'
    ORUS = 'or'
    NOTUS = 'not'
    # flow controls
    MYSTIME = 'if'             
    TURNTIME = 'elif'                
    RETURNTIME = 'else'           
    FORCULUS = 'for'                  
    WHILEGARDIUM = 'while'
    # other
    OPEN_PARENTHESIS = 'open_parenthesis'
    CLOSE_PARENTHESIS = 'close_parenthesis'
    OPEN_BRACE = 'open_curly_brace'
    CLOSE_BRACE = 'close_curly_brace'
    OPEN_BRACKET = 'open_bracket'
    CLOSE_BRACKET = 'close_bracket'
    TERNARY_THEN = 'ternary_then'
    TERNARY_ELSE = 'ternary_else'
    SEMICOLON = 'semicolon'
    NEWLINE = 'newline'
    DU = 'code_block'   
    TU = 'to'
    # special case -> 
    LENGTH_FUNCTION = 'length_function' 
    ARRAY_SIZE = 'array_size'
    ARRAY_ELEMENT = 'array_element'
