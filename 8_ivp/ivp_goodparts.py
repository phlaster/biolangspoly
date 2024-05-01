import numpy as np

def extract_function(code_str):
    mini_namespace = {'np': np}    
    initial_keys = set(mini_namespace.keys())
    initial_keys.add('__builtins__')

    exec(code_str, mini_namespace)
    
    new_keys = set(mini_namespace.keys()) - initial_keys
    
    if len(new_keys) == 1:
        new_key = new_keys.pop()
        if callable(mini_namespace[new_key]):
            return mini_namespace[new_key]
    return None


def read_input():
    t_0 = float(input())
    T = float(input())
    h_0 = float(input())
    N_x = int(input())
    eps = float(input())
    n = int(input())
    
    code_with_func = "\n".join([input() for i in range(n + 3)])
    foo = extract_function(code_with_func)
    initial_conditions = np.array(list(map(float, input().split())))

    return t_0, T, h_0, N_x, eps, foo, initial_conditions