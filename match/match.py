from typing import Dict, List, Any, Callable, Union

class Ob:    
    def __init__(self, value : Any):
        if callable(value):
            raise SyntaxError("Do not wrap functions. Use Fn object instead!")

        self.value = value

    def execution(self):
        return self.value

class Fn:
    def __init__(self, action : Callable, *args, **kwargs):
        def process():
            return action(*args, **kwargs)
        self.process = process

    def execution(self):
        return self.process()

class Case:
    def __init__(self, condition : bool):
        self.condition = condition

class Pattern:
    def __init__(self, condition : bool, result, *args, **kwargs):
        self.case = Case(condition)
        self.result = Fn(result, *args, **kwargs) if callable(result) else Ob(result)

def match(senarios : Union[List[Pattern], Dict[Case, Union[Ob, Fn]]]):
    """
    CAUTION: This code is intended for python 3.7 and the newer.
             That is because, dict order is not preserved before 3.6.
    """
    if type(senarios) is list:
        happenable_senarios = {pattern.case : pattern.result for pattern in senarios}.items()
    else:
        happenable_senarios = senarios.items()

    for case, result in happenable_senarios:
        if case.condition == False:
            continue
        return result.execution()