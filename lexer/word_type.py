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
    OPEN_PARENTHESIS = '('
    CLOSE_PARENTHESIS = ')'
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    SEMICOLON = ';'
    NEWLINE = 'newline'
    DU = 'code_block'                             