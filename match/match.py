from typing import Dict, List, Any, Callable, Union

class Ob: 
    """
    This class is a wrapper class for non-functional objects.
    It is used as a value in the dictionary with Case key.
    """   
    def __init__(self, value : Any):
        if callable(value):
            raise SyntaxError("Do not wrap functions. Use Fn object instead!")

        self.value = value

    def execution(self):
        return self.value

class Fn:
    """
    This class is a wrapper class for functions with their full set of parameters.
    It is used as a value in the dictionary with Case key.
    """
    def __init__(self, action : Callable, *args, **kwargs):
        def process():
            """
            The actual process is wrapped in the inner function.
            It is evaluated inside the match function
            when the corresponding Case key returns True.
            """
            return action(*args, **kwargs)
        self.process = process

    def execution(self):
        return self.process()

class Case:
    """
    This class is a wrapper class of bool.
    The purpose to create this class is to enable bool-returning expressions
    to become separate keys in a dictionary
    even if the returned bool value is same.
    """
    def __init__(self, condition : bool):
        self.condition = condition

class Pattern:
    """
    This class is a wrapper class of a pair of Case and Fn/Ob objects.
    The purpose to create this class is to enable match function
    to accept list data.
    """
    def __init__(self, condition : bool, result, *args, **kwargs):
        self.case = Case(condition)

        if callable(result):
            self.result = Fn(result, *args, **kwargs)
        else:
            self.result = Ob(result)

def match(senarios : Union[List[Pattern], Dict[Case, Union[Ob, Fn]]]):
    """
    CAUTION: This code is intended for python 3.7 and the newer.
             That is because, dict order is not preserved before 3.6.
    """
    if type(senarios) is list:
        happenable_senarios = {
            pattern.case : pattern.result 
            for pattern in senarios
        }.items()
    else:
        happenable_senarios = senarios.items()

    for case, result in happenable_senarios:
        if case.condition == False:
            continue
        return result.execution()