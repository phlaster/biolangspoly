#!/usr/bin/env python3
import numpy as np

def show_step(t, h, R, counter, y):
    print("%6f\t%6f\t%6e\t%d\t%s\t" % (t, h, R, counter[0], '\t'.join('%6f' % y_i for y_i in y)))

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
    if h_0 <= 0 or eps <= 0 or T <= t_0:
        raise ValueError("Invalid input values: ensure h_0 > 0, eps > 0, and T > t_0")
    if len(initial_conditions) != n:
        raise ValueError("Number of initial conditions does not match the number of equations")
    return t_0, T, h_0, N_x, eps, foo, initial_conditions

def heun_step(f, t, y, h, counter):
    k1 = f(t, y, counter)
    v_predictor = y + h * k1
    k2 = f(t + h, v_predictor, counter)
    v_corrected = y + 0.5 * h * (k1 + k2)
    return v_corrected

def solve_ode(method, t_0, T, h_0, N_x, eps, rhs, initial_conditions, THETA, ostream=True):
    t = t_0
    y = initial_conditions
    h = h_0
    kounter = [0]
    R = 0.0

    memo_h = None
    memo_h_12 = None

    history_counter = []
    history_h = []
    history_t = []
    history_R = []

    ostream and show_step(t, h, R, kounter, y)
    
    history_counter.append(kounter[0])
    history_h.append(h)
    history_t.append(t)
    history_R.append(R)

    while t+h/2 < T:
        if kounter[0] >= N_x:
            print(f"Maximum number of function calls ({N_x}) reached.")
            break
        h2 = h / 2
        y_next    = method(rhs, t,    y,         h,  kounter) if memo_h    is None else memo_h
        y_next_12 = method(rhs, t,    y,         h2, kounter) if memo_h_12 is None else memo_h_12
        y_next_22 = method(rhs, t+h2, y_next_12, h2, kounter)

        R = THETA * np.linalg.norm(y_next - y_next_22, 2)
        if R > eps:
            h = h2
            memo_h = y_next_12
            memo_h_12 = None
        elif R < eps / 64:
            h *= 2
            memo_h_12 = y_next
            memo_h = None
        else:
            t += h
            y = y_next_22
            memo_h = None
            memo_h_12 = None
            ostream and show_step(t, h, R, kounter, y)

            history_counter.append(kounter[0])
            history_h.append(h)
            history_t.append(t)
            history_R.append(R)
    return y, history_counter, history_h, history_t, history_R

def main():
    t_0, T, h_0, N_x, eps, fs, iconds = read_input()
    THETA = 2.0
    heun = solve_ode(heun_step, t_0, T, h_0, N_x, eps, fs, iconds, THETA)

if __name__ == "__main__":
    main()
