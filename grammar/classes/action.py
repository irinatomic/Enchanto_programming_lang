class Action:
    def __init__(self, action_name):
        self.actionName = action_name

class Error(Action):
    def __init__(self):
        super().__init__('Error')

    def __str__(self) -> str:
        return 'err'

class Accept(Action):
    def __init__(self):
        super().__init__('Accept')

    def __str__(self) -> str:
        return 'acc'

class Shift(Action):
    def __init__(self, into_state):
        super().__init__('Shift')
        self.intoState = into_state
    
    def __str__(self) -> str:
        return f's{self.intoState}'

class Reduce(Action):
    def __init__(self, rule_index):
        super().__init__('Reduce')
        self.ruleIndex = rule_index

    def __str__(self) -> str:
        return f's{self.ruleIndex}'

