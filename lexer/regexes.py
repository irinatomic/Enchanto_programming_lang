from .word_type import WordType
import re

class Regex:
    def __init__(self, regex, word_type):
        self.regex = regex
        self.word_type = word_type

    def matches(self, word):
        return self.regex.match(word)

class RegexCollection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_regex()
        return cls._instance

    def init_regex(self):
        regexes = [
            # first, check for 1 letter words
            Regex(re.compile(r'\('), WordType.OPEN_PARENTHESIS),
            Regex(re.compile(r'\)'), WordType.CLOSE_PARENTHESIS),
            Regex(re.compile(r'\['), WordType.OPEN_BRACKET),
            Regex(re.compile(r'\]'), WordType.CLOSE_BRACKET),
            Regex(re.compile(r'\{'), WordType.OPEN_BRACE),
            Regex(re.compile(r'\}'), WordType.CLOSE_BRACE),
            Regex(re.compile(r';'), WordType.SEMICOLON),
            Regex(re.compile(r'\n'), WordType.NEWLINE),
            Regex(re.compile(r'='), WordType.ASSIGN),
            Regex(re.compile(r'\+'), WordType.PLUS),
            Regex(re.compile(r'-'), WordType.MINUS),
            Regex(re.compile(r'\*'), WordType.MUL),
            Regex(re.compile(r'/'), WordType.DIV),
            Regex(re.compile(r'%'), WordType.MOD),
            Regex(re.compile(r'>'), WordType.GREATER_THAN),
            Regex(re.compile(r'<'), WordType.LESS_THAN),
            # second, check for 2 letter words
            Regex(re.compile(r'=='), WordType.EQUAL),
            Regex(re.compile(r'!='), WordType.NOT_EQUAL),
            Regex(re.compile(r'>='), WordType.GREATER_THAN_EQUAL),
            Regex(re.compile(r'<='), WordType.LESS_THAN_EQUAL),
            # third, check for constants
            Regex(re.compile(r'\bincantum\b'), WordType.INCANTUM),
            Regex(re.compile(r'\bdublatum\b'), WordType.DUBLATUM),
            Regex(re.compile(r'\bcharmax\b'), WordType.CHARMAX),
            Regex(re.compile(r'\bstringo\b'), WordType.STRINGO),
            Regex(re.compile(r'\barraygo\b'), WordType.ARRAYGO),
            Regex(re.compile(r'\benchanto\b'), WordType.ENCHANTO),
            Regex(re.compile(r'\bdeclaro\b'), WordType.DECLARO),
            Regex(re.compile(r'\bscriptum\b'), WordType.SCRIPTUM),
            Regex(re.compile(r'\brevelio\b'), WordType.REVELIO),
            Regex(re.compile(r'\bascendo\b'), WordType.ASCENDO),
            Regex(re.compile(r'\bdescendo\b'), WordType.DESCENDO),
            Regex(re.compile(r'\btribus\b'), WordType.TRIBUS),
            Regex(re.compile(r'\bandus\b'), WordType.ANDUS),
            Regex(re.compile(r'\borus\b'), WordType.ORUS),
            Regex(re.compile(r'\bnotus\b'), WordType.NOTUS),
            Regex(re.compile(r'\bmystime\b'), WordType.MYSTIME),
            Regex(re.compile(r'\bturntime\b'), WordType.TURNTIME),
            Regex(re.compile(r'\breturntime\b'), WordType.RETURNTIME),
            Regex(re.compile(r'\bforculus\b'), WordType.FORCULUS),
            Regex(re.compile(r'\bwhilegardium\b'), WordType.WHILEGARDIUM),
            # fourth, check for variables, characters, numbers and strings
            Regex(re.compile(r'[a-zA-Z_]\w*'), WordType.VARIABLE),
            Regex(re.compile(r'[a-zA-Z]'), WordType.CHARACTER),
            Regex(re.compile(r'\d+'), WordType.NUMBER),
            Regex(re.compile(r'\".*?\"'), WordType.STRING),
        ]
        return regexes
