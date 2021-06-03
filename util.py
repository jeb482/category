from typing import Any

def id(x: Any): 
    """Identity function
    """
    return x

def compose(f, g):
    """Returns the composition of functions f and g

    Args:
        f (B->C): function applied second
        g (A->B): function applied first

    Return 
        f_of_g (A->C)
    """
    return lambda *args, **kwargs: f(g(*args, **kwargs))
